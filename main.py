import requests
import time, threading
import sys

def read_file():
    site_list = open("websiteList.txt", "r")
    for line in site_list:
        page_name = line.split(",")[0]
        url_address = line.split(",")[1]
        content_requirement = line.split(",")[2]
        response = requests.get(url_address)
        request_time = response.elapsed
        request_status = str(response.status_code)
        check_result = response.text.lower().find(content_requirement.lower())
        if check_result == True: 
            return "Website's content requirement is fulfilled!"
        else:
            if request_status[0] == 4:
                print("Request fail, user's error") 
            elif request_status[0] == 5:
                print("Server is down!")
            else:
                print(page_name + ": Website's content requirement is not fulfilled. Request time: ")
                print(request_time) 
    site_list.close()

read_file()


   