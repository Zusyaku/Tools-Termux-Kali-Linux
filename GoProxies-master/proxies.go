package main

import "log"

const (
	// https://www.sslproxies.org/
	sSLProxiesURL       = "https://www.sslproxies.org/"
	sSLProxiesIPIndex   = 0
	sSLProxiesPortIndex = 1

	// https://www.socks-proxy.net/
	socksProxiesURL       = "https://www.socks-proxy.net/"
	socksProxiesIPIndex   = 0
	socksProxiesPortIndex = 1

	// https://free-proxy-list.net/
	freeProxiesURL       = "https://free-proxy-list.net/"
	freeProxiesIPIndex   = 0
	freeProxiesPortIndex = 1

	// Limits
	maxHistorySize = 512
)

type IProxier interface {
	count() int
	getProxy() (Proxy, error)
	contains(proxy Proxy) bool
}

func getProxy(p IProxier) (Proxy, error) {
	return p.getProxy()
}

func count(p IProxier) int {
	return p.count()
}

func contains(p IProxier, proxy Proxy) bool {
	return p.contains(proxy)
}

type ProxiesList struct {
	_proxiesHistory []Proxy
	_proxies        []IProxier
	_index          int
}

func newProxyList() *ProxiesList {
	OpenProxies := newOpenProxies()
	SSLProxies := newProxies(sSLProxiesURL, sSLProxiesIPIndex, sSLProxiesPortIndex)
	FreeProxies := newProxies(freeProxiesURL, freeProxiesIPIndex, freeProxiesPortIndex)
	SocksProxies := newProxies(socksProxiesURL, socksProxiesIPIndex, socksProxiesPortIndex)

	return &ProxiesList{
		_proxies:        []IProxier{SSLProxies, SocksProxies, OpenProxies, FreeProxies},
		_proxiesHistory: []Proxy{},
		_index:          0,
	}
}

func (p *ProxiesList) count() int {
	var total int

	for _, v := range p._proxies {
		total += v.count()
	}

	return total
}

func (p *ProxiesList) getProxy() (Proxy, error) {

	var proxy Proxy
	var err error

	defer func() {
		if err := recover(); err != nil {
			log.Println(err)
		}
	}()

	for {
		if p._index >= len(p._proxies) {
			p._index = 0
		}

		proxy, err = getProxy(p._proxies[p._index])
		p._index++

		if err != nil {
			log.Fatal(err)
		}

		if err == nil && !p._recentProxy(proxy) {
			p._addToHistory(proxy)
			break
		}
	}

	return proxy, err
}

func (p *ProxiesList) _recentProxy(proxy Proxy) bool {
	for _, v := range p._proxiesHistory {
		if v["ip"] == proxy["ip"] && v["port"] == proxy["port"] {
			return true
		}
	}
	return false
}

func (p *ProxiesList) _addToHistory(proxy Proxy) {
	p._proxiesHistory = append(p._proxiesHistory, proxy)

	if len(p._proxiesHistory) >= maxHistorySize {
		p._proxiesHistory = p._proxiesHistory[1:]
	}
}

func (p *ProxiesList) expiredProxy(proxy Proxy) {
	if !p._recentProxy(proxy) {
		p._addToHistory(proxy)
	}
}
