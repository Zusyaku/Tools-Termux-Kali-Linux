package main

import "fmt"

func main() {
	proxies := newProxyList()

	for i := 0; i < 5; i++ {
		p, _ := proxies.getProxy()
		fmt.Printf("proxy: %s\ntotal: %d\nindex: %d\nrecent: %d\n\n", p, proxies.count(), proxies._index, len(proxies._proxiesHistory))
	}

}
