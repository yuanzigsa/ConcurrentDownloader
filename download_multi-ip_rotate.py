#!/usr/bin/python
#coding=utf-8
import os, time, random, threading

# IP列表
ip_list = ['221.233.216.14', '221.233.216.15', '221.233.216.16', '221.233.216.17', '221.233.216.18']

current_ip = None
last_hour = None

def wget():
    global current_ip, last_hour
    while True:
        time.sleep(1)
        urls = open('./soft.txt').readlines()
        random.shuffle(urls)
        if 'http' in urls[0]:
            url = 'http' + urls[0].replace('\n', '').replace('\r\n', '').split('http')[-1]
            localtime = time.localtime(time.time())
            hour = int(time.strftime("%H", localtime))
            
            # 如果当前小时与上次的小时不同，选择一个新的随机IP
            if hour != last_hour:
                current_ip = random.choice(ip_list)
                last_hour = hour

            cmd = "wget  --bind-address=" + current_ip + " -q --user-agent='Mozilla/5.0' -O /dev/null '" + url + "'"
            os.popen(cmd)

def kill_wget():
    while True:
        os.popen('pkill  wget')
        print('pkill  wget')
        sec = random.randint(10, 20)
        time.sleep(sec)

kill_wget_thread = threading.Thread(target=kill_wget)
kill_wget_thread.start()

for _ in range(100):  # 创建线程，所创建的线程数量根据机器性能决定
    threading.Thread(target=wget).start()

time.sleep(999999999999999)