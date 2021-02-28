import requests
import sys
import time
import flask
from flask import request, jsonify, render_template
from flask_socketio import SocketIO, send

def update_page_status(new_status, url):
    f = open("log_file.txt", "r+")
    for line in f:
        split_line = line.split("---")
        if line.split("---")[0] == url:
            split_line.pop(1)
            line = split_line[0] + "    " + new_status
    return line

def write_log_file(content):
    log_file = open("log_file.txt","w")
    log_file.write(content)
    log_file.close()

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
timer()
        