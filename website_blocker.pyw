import time
from datetime import datetime as dt
ip_localmachine="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]
hosts_path="C:\Windows\System32\drivers\etc\hosts"
starttime="9.0.0"
endtime="18.0.0"
now=dt.now()
current_time=now.strftime("%H:%M:%S")
print(current_time)
while True:
    if start_time<=current_time and current_time<+end_time
    print("WORKING HOURS")
    with open(hosts_path,"r+") as file:
        content=file.read()
        for website in website_list:
            if website in content:
            pass
            else:
                file.write(ip_localmachine+" "+website+"\n")
                else:
                    print("NON WORKING HOURS")
                    with open(hosts_path,"r+")as file:
                        content=file.readlines()
                        file.seek(0)
                        if not any(website in line for website in website_list):
                            file.write(line)
                            file.truncate()
                            time.sleep(10)
