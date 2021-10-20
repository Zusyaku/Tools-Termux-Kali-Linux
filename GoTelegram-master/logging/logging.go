package logging

import (
    "fmt"
    "strings"
    "time"
)

type Logger struct {
    timeFormat string
    debug      bool
}

func New(timeFormat string, debug bool) *Logger {
    return &Logger{
        timeFormat: timeFormat,
        debug:      debug,
    }
}

func (l *Logger) Log(level string, s string) {
    level = strings.ToLower(level)
    switch level {
    case "info", "warning":
        if l.debug {
            l.write(level, s)                                                                                                                                                                                                                        }                                                                                                                                                                                                                                        default:                                                                                                                                                                                                                                         l.write(level, s)
    }
}

func (l *Logger) write(level string, s string) {
    fmt.Printf("[%s] %s %s\n", level, time.Now().Format(l.timeFormat), s)
}
