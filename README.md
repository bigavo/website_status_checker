
## General info
This is a Python program that read lists of Http URLs and corresponding requirements from a configuration file(websiteList.txt) then verify if it fulfills a defined requirement. Progress of the request as well as its reponse time is displayed into a log file name log_file.txt
	
## Work flow
Program follows synchronous work flow as following:
* Loop through websiteList.txt and extract url addresses and its requirement
* A http request is sent to url address which was extracted from the previous step
* Write to log_file.txt a line including url address and it's status which is now "Waiting" 
* Extract page content, response time, response status code from request's response
* Check if server is up or down base on response status code. Return "Client Error" ( if response status code is from 400-499). Return "Server is down!" (if response status is from 400-499). Otherwise, checking if the response contains requirement string or not. If yes return "OK", if not return "The content requirements were not fulfilled"
* Remove the last line of log_file.txt and add a new line which contains the url address, page status and response time to it. 
* Set timer using time.sleep(sys.argv[1]). The program is automatically run every 5 second (Defaut setting in launch.json file)

