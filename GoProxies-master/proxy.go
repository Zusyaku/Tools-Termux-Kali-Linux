package main

import (
	"fmt"
	"log"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

type Proxy map[string]string

type Proxies struct {
	_proxies   []Proxy
	_url       string
	_index     int
	_ipIndex   int
	_portIndex int
}

func newProxies(url string, ipIndex int, portIndex int) *Proxies {
	return &Proxies{
		_proxies:   []Proxy{},
		_url:       url,
		_index:     0,
		_ipIndex:   ipIndex,
		_portIndex: portIndex,
	}
}

func (p *Proxies) getProxy() (Proxy, error) {
	if p._index >= p.count() {
		p._collect()
		p._index = 0
	}

	if p.count() == 0 {
		return Proxy{}, fmt.Errorf("Failed to collect proxies")
	}

	proxy := p._proxies[p._index]
	p._index++

	return proxy, nil
}

func (p Proxies) count() int {
	var total int

	for _, element := range p._proxies {
		if element != nil {
			total++
		}
	}

	return total
}

func (p Proxies) contains(proxy Proxy) bool {
	for _, v := range p._proxies {
		if v["ip"] == proxy["ip"] && v["port"] == proxy["port"] {
			return true
		}
	}
	return false
}

func (p *Proxies) _collect() {
	doc, err := goquery.NewDocument(p._url)

	if err != nil {
		log.Fatal(err)
	}

	doc.Find("tbody > tr").Each(func(index int, item *goquery.Selection) {
		ip := item.Find("td").Eq(p._ipIndex).Text()
		port := item.Find("td").Eq(p._portIndex).Text()
		proxy := Proxy{"ip": ip, "port": port}

		if strings.Contains(ip, ".") && !p.contains(proxy) {
			p._proxies = append(p._proxies, proxy)
		}
	})
}
