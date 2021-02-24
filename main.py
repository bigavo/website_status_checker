import requests
import sys
import time
from django.shortcuts import render_to_response

def read_file():
    site_list = open("websiteList.txt", "r")
    for line in site_list:
        page_name = line.split(",")[0]
        url_address = line.split(",")[1]
        content_requirement = line.split(",")[2]
        response = requests.get(url_address)
        request_time = response.elapsed
        request_status = str(response.status_code)
        check_result = True
        if content_requirement in response.text:
            check_result = True
        else:
            check_result = False
        if check_result == True: 
            print(page_name + ": OK")
            print(request_time) 
        else:
            if request_status[0] == 4:
                print("Request fail, user's error") 
            elif request_status[0] == 5:
                print("Server is down!")
            else:
                print(page_name + ": Error. Request time: ")
                print(request_time) 
    site_list.close()

def timer():
    while True:
        read_file()
        time.sleep(10)

timer()

   