package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

type Payload struct {
	Key string `json:"key"`
}

func sendRequest(url string, payload Payload) {
	for {
		jsonPayload, _ := json.Marshal(payload)
		resp, err := http.Post(url, "application/json", bytes.NewBuffer(jsonPayload))
		if err != nil {
			fmt.Println("Error:", err)
			continue
		}
		defer resp.Body.Close()

		// Process the response if needed

		time.Sleep(time.Second) // Pause between each request
	}
}

func main() {
	url := "http://example.com/your-endpoint"
	payload := Payload{Key: "value"}

	for i := 0; i < 10; i++ {
		go sendRequest(url, payload)
	}

	for {
		continue
	}
}
