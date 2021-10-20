package gonion

//SDetails : for more info https://metrics.torproject.org/onionoo.html#details
type SDetails struct {
	Version         string `json:"version"`
	BuildRevision   string `json:"build_revision"`
	RelaysPublished string `json:"relays_published"`
	Relays          []struct {
		Nickname                 string   `json:"nickname"`
		Fingerprint              string   `json:"fingerprint"`
		OrAddresses              []string `json:"or_addresses"`
		LastSeen                 string   `json:"last_seen"`
		LastChangedAddressOrPort string   `json:"last_changed_address_or_port"`
		FirstSeen                string   `json:"first_seen"`
		Running                  bool     `json:"running"`
		Flags                    []string `json:"flags"`
		Country                  string   `json:"country,omitempty"`
		CountryName              string   `json:"country_name,omitempty"`
		As                       string   `json:"as,omitempty"`
		ConsensusWeight          int      `json:"consensus_weight"`
		LastRestarted            string   `json:"last_restarted"`
		BandwidthRate            int      `json:"bandwidth_rate"`
		BandwidthBurst           int      `json:"bandwidth_burst"`
		ObservedBandwidth        int      `json:"observed_bandwidth"`
		AdvertisedBandwidth      int      `json:"advertised_bandwidth"`
		ExitPolicy               []string `json:"exit_policy"`
		ExitPolicySummary        struct {
			Reject []string `json:"reject"`
		} `json:"exit_policy_summary,omitempty"`
		Contact                 string   `json:"contact,omitempty"`
		Platform                string   `json:"platform"`
		Version                 string   `json:"version"`
		VersionStatus           string   `json:"version_status"`
		EffectiveFamily         []string `json:"effective_family"`
		ConsensusWeightFraction float64  `json:"consensus_weight_fraction,omitempty"`
		GuardProbability        float64  `json:"guard_probability,omitempty"`
		MiddleProbability       float64  `json:"middle_probability,omitempty"`
		ExitProbability         float64  `json:"exit_probability,omitempty"`
		RecommendedVersion      bool     `json:"recommended_version"`
		Measured                bool     `json:"measured"`
		ExitAddresses           []string `json:"exit_addresses,omitempty"`
		DirAddress              string   `json:"dir_address,omitempty"`
		VerifiedHostNames       []string `json:"verified_host_names,omitempty"`
	} `json:"relays"`
	BridgesPublished string `json:"bridges_published"`
	Bridges          []struct {
		Nickname                 string   `json:"nickname"`
		HashedFingerprint        string   `json:"hashed_fingerprint"`
		OrAddresses              []string `json:"or_addresses"`
		LastSeen                 string   `json:"last_seen"`
		FirstSeen                string   `json:"first_seen"`
		Running                  bool     `json:"running"`
		Flags                    []string `json:"flags"`
		LastRestarted            string   `json:"last_restarted"`
		AdvertisedBandwidth      int      `json:"advertised_bandwidth"`
		Platform                 string   `json:"platform"`
		Version                  string   `json:"version"`
		VersionStatus            string   `json:"version_status"`
		RecommendedVersion       bool     `json:"recommended_version"`
		BridgedbDistributor      string   `json:"bridgedb_distributor,omitempty"`
		Transports               []string `json:"transports,omitempty"`
		OverloadGeneralTimestamp int64    `json:"overload_general_timestamp,omitempty"`
	} `json:"bridges"`
}

//SSummary : for more info https://metrics.torproject.org/onionoo.html#summary
type SSummary struct {
	Version         string `json:"version"`
	BuildRevision   string `json:"build_revision"`
	RelaysPublished string `json:"relays_published"`
	Relays          []struct {
		N string   `json:"n"`
		F string   `json:"f"`
		A []string `json:"a"`
		R bool     `json:"r"`
	} `json:"relays"`
	BridgesPublished string `json:"bridges_published"`
	Bridges          []struct {
		N string `json:"n"`
		H string `json:"h"`
		R bool   `json:"r"`
	} `json:"bridges"`
}

//SBandwidth : for more info https://metrics.torproject.org/onionoo.html#bandwidth
type SBandwidth struct {
	Version         string `json:"version"`
	BuildRevision   string `json:"build_revision"`
	RelaysPublished string `json:"relays_published"`
	Relays          []struct {
		Fingerprint  string `json:"fingerprint"`
		WriteHistory struct {
			OneMonth struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"1_month"`
			SixMonths struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"6_months"`
			OneYear struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"1_year"`
			FiveYears struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"5_years"`
		} `json:"write_history,omitempty"`
		ReadHistory struct {
			OneMonth struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"1_month"`
			SixMonths struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"6_months"`
			OneYear struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"1_year"`
			FiveYears struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"5_years"`
		} `json:"read_history,omitempty"`
	} `json:"relays"`
	RelaysTruncated  int           `json:"relays_truncated"`
	BridgesPublished string        `json:"bridges_published"`
	Bridges          []interface{} `json:"bridges"`
	BridgesTruncated int           `json:"bridges_truncated"`
}

//SWeights : for more info https://metrics.torproject.org/onionoo.html#weights
type SWeights struct {
	Version         string `json:"version"`
	BuildRevision   string `json:"build_revision"`
	RelaysPublished string `json:"relays_published"`
	Relays          []struct {
		Fingerprint             string `json:"fingerprint"`
		ConsensusWeightFraction struct {
			OneMonth struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"1_month"`
			SixMonths struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"6_months"`
			OneYear struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"1_year"`
			FiveYears struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"5_years"`
		} `json:"consensus_weight_fraction,omitempty"`
		GuardProbability struct {
			OneMonth struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"1_month"`
			SixMonths struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"6_months"`
			OneYear struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"1_year"`
			FiveYears struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"5_years"`
		} `json:"guard_probability,omitempty"`
		MiddleProbability struct {
			OneMonth struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"1_month"`
			SixMonths struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"6_months"`
			OneYear struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"1_year"`
			FiveYears struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"5_years"`
		} `json:"middle_probability,omitempty"`
		ExitProbability struct {
			OneMonth struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"1_month"`
			SixMonths struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"6_months"`
			OneYear struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"1_year"`
			FiveYears struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"5_years"`
		} `json:"exit_probability,omitempty"`
		ConsensusWeight struct {
			OneMonth struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"1_month"`
			SixMonths struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"6_months"`
			OneYear struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"1_year"`
			FiveYears struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"5_years"`
		} `json:"consensus_weight,omitempty"`
	} `json:"relays"`
	RelaysTruncated  int           `json:"relays_truncated"`
	BridgesPublished string        `json:"bridges_published"`
	Bridges          []interface{} `json:"bridges"`
}

//SClients : for more info https://metrics.torproject.org/onionoo.html#clients
type SClients struct {
	Version          string        `json:"version"`
	BuildRevision    string        `json:"build_revision"`
	RelaysPublished  string        `json:"relays_published"`
	Relays           []interface{} `json:"relays"`
	BridgesPublished string        `json:"bridges_published"`
	Bridges          []struct {
		Fingerprint    string `json:"fingerprint"`
		AverageClients struct {
			OneMonth struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"1_month"`
			SixMonths struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"6_months"`
			OneYear struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"1_year"`
			FiveYears struct {
				First    string        `json:"first"`
				Last     string        `json:"last"`
				Interval int           `json:"interval"`
				Factor   float64       `json:"factor"`
				Count    int           `json:"count"`
				Values   []interface{} `json:"values"`
			} `json:"5_years"`
		} `json:"average_clients"`
	} `json:"bridges"`
	BridgesTruncated int `json:"bridges_truncated"`
}

//SUptime : for more info https://metrics.torproject.org/onionoo.html#uptime
type SUptime struct {
	Version         string `json:"version"`
	BuildRevision   string `json:"build_revision"`
	RelaysPublished string `json:"relays_published"`
	Relays          []struct {
		Fingerprint string `json:"fingerprint"`
		Uptime      struct {
			OneMonth struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"1_month"`
			SixMonths struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"6_months"`
			OneYear struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"1_year"`
			FiveYears struct {
				First    string  `json:"first"`
				Last     string  `json:"last"`
				Interval int     `json:"interval"`
				Factor   float64 `json:"factor"`
				Count    int     `json:"count"`
				Values   []int   `json:"values"`
			} `json:"5_years"`
		} `json:"uptime,omitempty"`
		Flags struct {
			Exit struct {
				OneMonth struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_month"`
				SixMonths struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"6_months"`
				OneYear struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_year"`
				FiveYears struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"5_years"`
			} `json:"Exit"`
			Fast struct {
				OneMonth struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_month"`
				SixMonths struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"6_months"`
				OneYear struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_year"`
				FiveYears struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"5_years"`
			} `json:"Fast"`
			Guard struct {
				OneMonth struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_month"`
				SixMonths struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"6_months"`
				OneYear struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_year"`
				FiveYears struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"5_years"`
			} `json:"Guard"`
			HSDir struct {
				OneMonth struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_month"`
				SixMonths struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"6_months"`
				OneYear struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_year"`
				FiveYears struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"5_years"`
			} `json:"HSDir"`
			Running struct {
				OneMonth struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_month"`
				SixMonths struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"6_months"`
				OneYear struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_year"`
				FiveYears struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"5_years"`
			} `json:"Running"`
			Stable struct {
				OneMonth struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_month"`
				SixMonths struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"6_months"`
				OneYear struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_year"`
				FiveYears struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"5_years"`
			} `json:"Stable"`
			StaleDesc struct {
				OneMonth struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_month"`
				SixMonths struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"6_months"`
				OneYear struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_year"`
				FiveYears struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"5_years"`
			} `json:"StaleDesc"`
			V2Dir struct {
				OneMonth struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_month"`
				SixMonths struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"6_months"`
				OneYear struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_year"`
				FiveYears struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"5_years"`
			} `json:"V2Dir"`
			Valid struct {
				OneMonth struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_month"`
				SixMonths struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"6_months"`
				OneYear struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"1_year"`
				FiveYears struct {
					First    string  `json:"first"`
					Last     string  `json:"last"`
					Interval int     `json:"interval"`
					Factor   float64 `json:"factor"`
					Count    int     `json:"count"`
					Values   []int   `json:"values"`
				} `json:"5_years"`
			} `json:"Valid"`
		} `json:"flags,omitempty"`
	} `json:"relays"`
	RelaysTruncated  int           `json:"relays_truncated"`
	BridgesPublished string        `json:"bridges_published"`
	Bridges          []interface{} `json:"bridges"`
	BridgesTruncated int           `json:"bridges_truncated"`
}
