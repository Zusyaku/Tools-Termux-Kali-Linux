package main

import (
	"sync"
)

type BotManager struct {
	IP      string
	port    string
	threads int
	bots    []*Bot
	isAlive bool
	wg      *sync.WaitGroup
	_       struct{}
}

func newBotManager(ip, port string, threads int, wg *sync.WaitGroup) *BotManager {
	return &BotManager{
		IP:      ip,
		port:    port,
		threads: threads,
		isAlive: true,
		wg:      wg,
		bots:    []*Bot{},
	}
}

func (bm *BotManager) start() {
	for i := 0; i < bm.threads; i++ {
		bot := newBot(bm.IP, bm.port, bm.wg)

		if bm.isAlive {
			bm.wg.Add(1)
			bm.bots = append(bm.bots, bot)
			go bot.start()
		}
	}
}

func (bm *BotManager) stop() {
	for _, bot := range bm.bots {
		bot.stop()
	}
}
