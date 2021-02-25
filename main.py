import requests
import sys
import time
import flask
from flask import request, jsonify, render_template

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
        response_status_code = str(response.status_code)
        check_result = (content_requirement in response.text)
        if check_result == True: 
            page_status = "OK"
        else:
            if response_status_code in range(400, 499):
                page_status = "User's error"
            elif response_status_code in range(500, 599):
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
        if split_line[0] == url:
            split_line.pop(1)
            line = split_line[0] + "    " + new_status
    f.close()
    return line

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def test():
    response_info = display_response_progress()
    url = response_info[0]
    status = response_info[1]
    time = response_info[2]
    output_text = "" 
    for i in range(len(url)):
        line = url[i] + "----" + status[i] + "----" + time[i] + "\n"
        output_text = output_text + line 
    return render_template('index.html', )


def display_response_progress():
    site_list = open("websiteList.txt", "r")
    url_address_list = []
    page_status_list = []
    request_time_list = []
    for line in site_list:
        url_address = line.split(",")[0]
        content_requirement = line.split(",")[1]
        page_status = "Waiting"
        response = requests.get(url_address)
        request_time = str(response.elapsed)
        response_status_code = str(response.status_code)
        check_result = (content_requirement in response.text)
        if check_result == True: 
            page_status = "OK"
        else:
            if response_status_code in range(400, 499):
                page_status = "User's error"
            elif response_status_code in range(500, 599):
                page_status = "Server is down!"
        url_address_list.append(url_address)
        page_status_list.append(page_status)
        request_time_list.append(request_time)
        response_content = (url_address_list, page_status_list, request_time_list)
    return response_content

if __name__ == '__main__':
    app.run()