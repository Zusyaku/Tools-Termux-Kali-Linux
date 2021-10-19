package main

func asciilowercase() string {
	p := make([]byte, 26)

	for i := range p {
		p[i] = 'a' + byte(i)
	}

	return string(p)
}

func asciiuppercase() string {
	p := make([]byte, 26)

	for i := range p {
		p[i] = 'A' + byte(i)
	}

	return string(p)
}
