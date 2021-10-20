package gonion

import (
	"fmt"
	"net/url"
	"strings"
)

//Params : see https://metrics.torproject.org/onionoo.html#parameters for further info
type Params struct {
	Type string

	Running bool

	Search string

	Lookup string

	Country string

	As string

	AsName string

	Flag string

	FirstSeenDays string

	LastSeenDays string

	Contact string

	Family string

	Version string

	Os string

	HostName string

	RecommendedVersion bool

	Fields []string

	Order []string

	Offset int

	Limit int
}

func validOrder(s []string) bool {
	for _, v := range s {
		if v != "consensus_weight" && v != "first_seen" {
			return false
		}
	}
	return true
}

//QueryParams : parse parameters and creates a url
func (args Params) QueryParams() (url.Values, error) {
	q := make(url.Values)

	if args.Type != "" {
		if args.Type == "relay" || args.Type == "bridge" {
			q.Add("type", args.Type)
		}
	}

	q.Add("running", fmt.Sprintf("%t", args.Running))

	if args.Search != "" {
		q.Add("search", args.Search)
	}

	if args.Lookup != "" {
		if len([]rune(args.Lookup)) == 40 {
			q.Add("lookup", args.Lookup)
		} else {
			return nil, fmt.Errorf("Error : invalid fingerprint on lookup parameter")
		}
	}

	if args.Country != "" {
		if len([]rune(args.Country)) == 2 {
			q.Add("country", args.Country)
		} else {
			return nil, fmt.Errorf("Error : Country code cannot be more than 2 characters on country parameter")
		}
	}

	if args.As != "" {
		q.Add("as", args.As)
	}

	if args.AsName != "" {
		q.Add("as_name", args.AsName)
	}

	if args.Flag != "" {
		q.Add("flag", args.Flag)
	}

	if args.FirstSeenDays != "" {
		q.Add("first_seen_days", args.FirstSeenDays)
	}

	if args.LastSeenDays != "" {
		q.Add("last_seen_days", args.LastSeenDays)
	}

	if args.Contact != "" {
		q.Add("contact", args.Contact)
	}

	if args.Family != "" {
		if len([]rune(args.Family)) == 40 {
			q.Add("family", args.Family)
		} else {
			return nil, fmt.Errorf("Error : invalid fingerprint on family parameter")
		}
	}

	if args.Version != "" {
		q.Add("version", args.Version)
	}

	if args.Os != "" {
		q.Add("os", args.Os)
	}

	if args.HostName != "" {
		q.Add("host_name", args.HostName)
	}

	q.Add("recommended_version", fmt.Sprintf("%t", args.RecommendedVersion))

	if len(args.Fields) > 0 {
		q.Add("fields", strings.Join(args.Fields, ","))
	}

	if len(args.Order) > 0 {
		if validOrder(args.Order) {
			q.Add("order", strings.Join(args.Order, ","))
		}
	}

	if args.Offset != 0 {
		q.Add("offset", fmt.Sprintf("%d", args.Offset))
	}

	if args.Limit != 0 {
		q.Add("limit", fmt.Sprintf("%d", args.Limit))
	}

	return q, nil
}
