package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"
)

const openProxiesURL = "https://api.openproxy.space/free-proxy-list"

type respContainer struct {
	Proxies []json.RawMessage `json:"proxies"`
}

type proxyContainer struct {
	Ip   string `json:"ip"`
	Port int    `json:"port"`
}

type OpenProxies struct {
	_proxies []Proxy
	_index   int
	_client  *http.Client
}

func newOpenProxies() *OpenProxies {
	return &OpenProxies{
		_proxies: []Proxy{},
		_index:   0,
		_client:  &http.Client{},
	}
}

func (p OpenProxies) contains(proxy Proxy) bool {
	for _, v := range p._proxies {
		if v["ip"] == proxy["ip"] && v["port"] == proxy["port"] {
			return true
		}
	}
	return false
}

func (p *OpenProxies) getProxy() (Proxy, error) {
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

func (p OpenProxies) count() int {
	var total int

	for _, element := range p._proxies {
		if element != nil {
			total++
		}
	}

	return total
}

func (p *OpenProxies) _collect() {
	client := p._client

	// Make GET requests
	proxyURL, _ := http.NewRequest("GET", openProxiesURL, nil)
	getResp, getErr := client.Do(proxyURL)

	if getErr != nil {
		log.Fatalln("Error encounter while making a GET request. ", getErr)
	}

	defer getResp.Body.Close()

	body, readErr := ioutil.ReadAll(getResp.Body)

	if readErr != nil {
		log.Fatal("Error while posting for the third time. ", readErr)
	}

	jsonResp := respContainer{}
	err := json.Unmarshal(body, &jsonResp)

	if err != nil {
		log.Fatalln("Error unmashalling data. ", err)
	}

	for _, k := range jsonResp.Proxies {
		_proxy := proxyContainer{}
		err2 := json.Unmarshal(k, &_proxy)

		if err2 != nil {
			log.Fatalln("Error unmashalling data. ", err2)
		}

		proxy := Proxy{"ip": _proxy.Ip, "port": strconv.Itoa(_proxy.Port)}

		if !p.contains(proxy) {
			p._proxies = append(p._proxies, proxy)
		}
	}
}
