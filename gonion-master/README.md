# gonion

Lightweight Golang wrapper for querying Tor network data using the Onionoo service.

[![GoDoc](https://godoc.org/github.com/R4yGM/gonion/gonion?status.svg)](http://godoc.org/github.com/R4yGM/gonion)
[![Go Report Card](https://goreportcard.com/badge/github.com/R4yGM/gonion)](https://goreportcard.com/report/github.com/R4yGM/gonion)

```go
package main

import (
        "github.com/R4yGM/gonion"
        "net/http"
        "time"
        "fmt"
)

func main(){

        var netClient = &http.Client{
                Timeout: time.Second * 10,
        }

        g := gonion.Client{HttpClient: netClient}
        res := g.Details(gonion.Params{Search : "R4y", Running: true, RecommendedVersion: true})
        fmt.Println(res.Relays[0].Nickname)
}
```

## Installation

The Golang wrapper has been tested with Golang 1.6+. It may worker with older versions although it has not been tested.

To use it, just include it to your ``import`` and run ``go get``:
```bash
go get github.com/R4yGM/gonion
```

```go
import (
	...
	"github.com/R4yGM/gonion"
)
```

# Usage

gonion contains a function for each method available on the onionoo service, check them here https://metrics.torproject.org/onionoo.html#methods

which are :
```
Summary()
Details()
Bandwidth()
Weights()
Clients()
Uptime()
```
and all the results are put inside on the respective structs inside the file structs.go, you can also check the responses here https://metrics.torproject.org/onionoo.html#responses that are the same of the structs

**Parameters**

you can insert all the parameters you want that are listed here https://metrics.torproject.org/onionoo.html#parameters inside the `gonion.Params{}` struct
