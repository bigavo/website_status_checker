import requests
import sys
import time

def read_file():
    site_list = open("websiteList.txt", "r")
    output = ""
    for line in site_list:
        page_name = line.split(",")[0]
        url_address = line.split(",")[1]
        content_requirement = line.split(",")[2]
        response = requests.get(url_address)
        request_time = str(response.elapsed)
        request_status = str(response.status_code)
        check_result = (content_requirement in response.text)
        if check_result == True: 
            # print(page_name + ": OK. Request time: "  + request_time + "s")
            output = output + url_address + ": OK. Request time: "  + request_time + "s" + "\n"
            # return output
        else:
            if request_status in range(400, 499):
                # print("Request fail, user's error") 
                output = output + "User's error"
                # return output
            elif request_status in range(500, 599):
                # print("Server is down!")
                output = output + url_address + "Server is down"
                # return output
            else:
                # print(page_name + ": Error. Request time: ")
                output = output + url_address + ": Error. Request time: "
                # return output
    site_list.close()
    return output

def timer():
    while True:
        read_file()
        time.sleep(int(sys.argv[1]))

timer()

def print_log_file():
    log_file_content = read_file()
    log_file = open("log_file.txt","w")
    log_file.write(log_file_content)
    log_file.close()
# print_log_file()

   