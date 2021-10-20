package gonion

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
)

//Client : initialize the client for gonion
type Client struct {
	UserAgent  string
	HttpClient *http.Client
}

//Summary : returns results from https://onionoo.torproject.org/summary
func (c *Client) Summary(args Params) SSummary {
	req, err := c.SendRequest("/summary", args)
	if err != nil {
		log.Fatal(err)
	}

	resp, err := c.HttpClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	defer resp.Body.Close()
	var Sum SSummary
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	json.Unmarshal([]byte(body), &Sum)
	return Sum
}

//Details : returns results from https://onionoo.torproject.org/details
func (c *Client) Details(args Params) SDetails {

	req, err := c.SendRequest("/details", args)
	if err != nil {
		log.Fatal(err)
	}
	resp, err := c.HttpClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	defer resp.Body.Close()

	var Det SDetails
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	json.Unmarshal([]byte(body), &Det)
	return Det

}

//Bandwidth : returns results from https://onionoo.torproject.org/bandwidth
func (c *Client) Bandwidth(args Params) SBandwidth {

	req, err := c.SendRequest("/bandwidth", args)
	if err != nil {
		log.Fatal(err)
	}
	resp, err := c.HttpClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	defer resp.Body.Close()
	var Ban SBandwidth
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	json.Unmarshal([]byte(body), &Ban)
	return Ban

}

//Weights : returns results from https://onionoo.torproject.org/bandwidth
func (c *Client) Weights(args Params) SWeights {

	req, err := c.SendRequest("/weights", args)
	if err != nil {
		log.Fatal(err)
	}
	resp, err := c.HttpClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	defer resp.Body.Close()
	var Wei SWeights
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	json.Unmarshal([]byte(body), &Wei)
	return Wei

}

//Clients : returns results from https://onionoo.torproject.org/bandwidth
func (c *Client) Clients(args Params) SClients {

	req, err := c.SendRequest("/clients", args)
	if err != nil {
		log.Fatal(err)
	}
	resp, err := c.HttpClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	defer resp.Body.Close()
	var Cli SClients
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	json.Unmarshal([]byte(body), &Cli)
	return Cli

}

//Uptime : returns results from https://onionoo.torproject.org/bandwidth
func (c *Client) Uptime(args Params) SUptime {

	req, err := c.SendRequest("/uptime", args)
	if err != nil {
		log.Fatal(err)
	}
	resp, err := c.HttpClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	defer resp.Body.Close()

	var Upt SUptime
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	json.Unmarshal([]byte(body), &Upt)
	return Upt

}

//SendRequest : creates the request ready to be sent with the client, parameters and path
func (c *Client) SendRequest(path string, args Params) (*http.Request, error) {
	BaseURL, err := url.Parse("https://onionoo.torproject.org")
	if err != nil {
		log.Fatal(err)
	}
	rel := &url.URL{Path: path}
	u := BaseURL.ResolveReference(rel)
	req, err := http.NewRequest("GET", u.String(), nil)
	if err != nil {
		log.Fatal(err)
	}
	req.Header.Set("Accept", "application/json")
	req.Header.Set("User-Agent", c.UserAgent)
	q, err := args.QueryParams()
	if err != nil {
		log.Fatal(err)
	}
	req.URL.RawQuery = q.Encode()

	return req, nil
}
