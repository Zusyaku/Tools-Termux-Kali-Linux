package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"os/signal"
	"runtime"
	"strconv"
	"strings"
	"sync"
	"syscall"
)

var (
	cls   string
	isWin = false
)

const defaultThreads = 2048

func init() {
	if runtime.GOOS == "windows" {
		isWin = true
	}
}

func main() {
	wg := sync.WaitGroup{}
	defer wg.Wait()

	ip, port, threads := userInput()

	botManager := newBotManager(ip, port, threads, &wg)
	botManager.start()

	clear()
	fmt.Printf("Target: %s:%s\nThreads: %d\n\n(Ctrl + C) to quit\n", ip, port, threads)

	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)

	go func() {
		<-c
		botManager.stop()
	}()

}

func userInput() (ip string, port string, threads int) {

	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("Enter IP: ")
	scanner.Scan()
	ip = scanner.Text()

	fmt.Print("Enter Port: ")
	scanner.Scan()
	port = scanner.Text()

	fmt.Printf("Enter Threads (default: %d): ", defaultThreads)
	scanner.Scan()
	strThreads := scanner.Text()

	if len(strings.TrimSpace(strThreads)) != 0 {
		threads, _ = strconv.Atoi(strThreads)
	} else {
		threads = defaultThreads
	}

	return
}

func clear() {
	var cmd *exec.Cmd

	if isWin {
		cmd = exec.Command("cmd", "/c", "cls")
	} else {
		cmd = exec.Command("clear")
	}

	cmd.Stdout = os.Stdout
	cmd.Run()
}
