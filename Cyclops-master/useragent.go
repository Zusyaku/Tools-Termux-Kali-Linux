package main

import (
	"fmt"
)

func getWinVer() float64 {
	return 10.0
}

func getChromeVer() string {
	a := randint(40, 96)
	b := randint(2987, 3497)
	c := randint(80, 140)

	return fmt.Sprintf("%d.0.%d.%d", a, b, c)
}

func getUseragent() string {
	a := fmt.Sprintf("Mozilla/5.0 (Windows NT %f; Win64; x64)", getWinVer())
	b := fmt.Sprintf("AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Safari/537.36", getChromeVer())
	return fmt.Sprintf("%s %s", a, b)
}
