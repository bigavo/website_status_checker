def read_file():
    site_list = open("websiteList.txt", "r")
    for line in site_list: 
        address = line.split(",")[0]
        content_requirement = line.split(",")[1]
    site_list.close()

read_file()
