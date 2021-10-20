package GoTelegram

import(
	"time"
	//log "./golang/src/github.com/r4y/GoTelegram/log"
	logging "github.com/R4yGM/GoTelegram/logging"
	"fmt"
	"net/http"
	"io/ioutil"
    	"encoding/json"	
	
	"log"
)
type Token struct {

     Key string
     Debug bool
}
type GetMe struct {
	Ok bool `json:"ok"`
	Result struct {
		Id int `json:"id"`
		Username string `json:"username"`
		First_name string `json:"first_name"`
	}

}
type GetUpdates struct {
	Ok bool `json:"ok"`
	Result []struct {
		Update_id int `json:"update_id"`
		Message struct {
			Message_id int `json:"message_id"`
			From struct {
				Id int `json:"id"`
				Is_bot bool `json:"is_bot"`
				First_name string `json:"first_name"`
				Username string `json:"username"`
				Language_code string `json:"language_code"`
			}`json:"from"`
			Chat struct{
				Id int `json:"id"`                                   
				First_name string `json:"first_name"`
                                Username string `json:"username"`            
                                Type string `json:"type"`
			

			}`json:"chat"`
			Date int `json:"date"`
			Text string `json:"text"`
			
			
		}`json:"message"`
	}`json:"result"`


}


func (t Token) GetMe() {
	res, err := http.Get("https://api.telegram.org/bot"+t.Key+"/getMe")
		if err != nil {
    		panic(err.Error())
	    	return
		}
	var g GetMe
	//	var result map[string]interface{}
	//fmt.Println(result["ok"])
    	responseData, err := ioutil.ReadAll(res.Body)
	json.Unmarshal(responseData, &g)
	if g.Ok == false{
		logger := logging.New(time.RFC3339, t.Debug)                                             
		 logger.Log("error", "error in the request, check if your token is right")
		return
	}
	if g.Ok == true{

		//response, err := ioutil.ReadAll(res.Body)                                              
//        	fmt.Println(string(response))                                                             
	        //json.Unmarshal(response, &g)
		if err != nil {
		panic(err)
		}
		//fmt.Println(g.Result.Id)
		logger := logging.New(time.RFC3339, t.Debug)
		fmt.Println("Bot name : "+g.Result.First_name)
		fmt.Println("Bot username : "+g.Result.Username)
		fmt.Println("Bot id : ", g.Result.Id)
		logger.Log("info" , "Bot successfully initialized")
	}

	return
}
//var i = 1
//var increment = 0
var updateIds []int
func (t Token) GetMessages(i int)(Text string){
	

	res, err := http.Get("https://api.telegram.org/bot"+t.Key+"/getUpdates")                    
                if err != nil {                                                                      
                panic(err.Error())                                                                 
                return   
                }
	var g GetUpdates
	responseData, err := ioutil.ReadAll(res.Body)                                                                                    
	json.Unmarshal(responseData, &g)

	if g.Ok == false{
	logger := logging.New(time.RFC3339, t.Debug)                                                                                 
               logger.Log("error", "error in the request, check if your token is right")                                  
                return	
	}
	if g.Ok == true{
		count := len(g.Result)
	fmt.Println("a111")
	fmt.Printf("%+q\n", updateIds)
	fmt.Println(count)
	//file, err := ioutil.ReadFile("file.txt")
	//file = binary.BigEndian.Uint64(file)
	//i := 0
	fmt.Println(i)
   	 if err != nil {
        log.Fatal(err)
	    }
	//i = file
	if i >= count{
	 fmt.Println("catch!")
	i = 0
	}
	_, found := Find(updateIds, g.Result[i].Update_id)
	if found {
		fmt.Println(i)
		fmt.Println(updateIds)
		fmt.Println("a222")
		return
	}
	if !found {
		fmt.Println("NOT FOUND")
	updateIds = append(updateIds, g.Result[i].Update_id)                                                               
       Text = g.Result[i].Message.Text
       fmt.Println(g.Result[i].Message.Text)
	 }
	}
	//updateIds = append(updateIds, g.Result.Update_id)
	//Text = g.Result[increment].Message.Text
	//increment = increment + 1 
	
	return
}
func Hello() {
    fmt.Println("Hello, World!")
}

func (t Token) InitializeBot(){                                                              
 logger := logging.New(time.RFC3339, t.Debug)                                                         
 logger.Log("info", "Building the bot")                                                           
 t.GetMe()                                                                                           
//return fmt.Sprintf("here is the token: %d ", t.Key)                                                 
}
func Find(slice []int, val int) (int, bool) {
    for i, item := range slice {
        if item == val {
            return i, true
        }
    }
    return -1, false
}
