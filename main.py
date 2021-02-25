import requests
import sys
import time

def check_page_status():
    site_list = open("websiteList.txt", "r")
    output = ""
    for line in site_list:
        url_address = line.split(",")[0]
        content_requirement = line.split(",")[1]
        page_status = "Waiting"
        loading_text = output + url_address + "---" + page_status + "---"
        write_log_file(loading_text)
        response = requests.get(url_address)
        request_time = str(response.elapsed)
        request_status = str(response.status_code)
        check_result = (content_requirement in response.text)
        if check_result == True: 
            # print(page_name + ": OK. Request time: "  + request_time + "s")
            # output = output + url_address + ": OK. Request time: "  + request_time + "s" + "\n"
            page_status = "OK"
            # log_file = open("log_file.txt","r")
            # for line in log_file:
            #     line.replace('Wait', output)
            # log_file.close()
        else:
            if request_status in range(400, 499):
                # print("Request fail, user's error") 
                # output = output + "User's error"
                # return output
                page_status = "User's error"
            elif request_status in range(500, 599):
                # print("Server is down!")
                # output = output + url_address + "Server is down"
                # return output
                page_status = "Server is down!"

        update_text = update_page_status(page_status, url_address)
        output = output + update_text + "     " + request_time + "s" + "\n"
        write_log_file(output)
    site_list.close()
    return output

def timer():
    while True:
        check_page_status()
        time.sleep(int(sys.argv[1]))

# timer()

def write_log_file(content):
    log_file = open("log_file.txt","w")
    log_file.write(content)
    log_file.close()

def read_file():
    f = open("log_file.txt","r")
    content = f.read
    print(content)
    f.close()

def update_page_status(new_status, url):
    f = open("log_file.txt", "r+")
    lines = f.readlines()
    f.close()
    for line in lines:
        split_line = line.split("---")
        if line.split("---")[0] == url:
            split_line.pop(1)
            line = split_line[0] + "    " + new_status
    f.close()
    return line

check_page_status()
   