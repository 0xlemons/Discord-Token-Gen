import os, random, string, time, json, sys, ctypes
from data.solver import Solver
import faker
from faker import Faker
fake = Faker()
import random
from random import randint
from kopeechka import KopeechkaApiError, MailActivations
try:
    import requests
    import httpx
    import bs4
    import pystyle
    import colorama
    import threading
    import datetime
    import tls_client
    import websocket
    from websocket import create_connection

except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install httpx")
    os.system("pip install bs4")
    os.system("pip install pystyle")
    os.system("pip install colorama")
    os.system("pip install threading")
    os.system("pip install datetime")
    os.system("pip install tls_client")
    os.system("pip install websocket")

from colorama import Fore
from pystyle import Write, System, Colors, Colorate, Anime
from bs4 import BeautifulSoup
from threading import Lock
from random import choice
from tls_client import Session
from json import dumps
from websocket import WebSocket
with open ("config.json") as f:
    data = json.load(f)
    kop_key = data.get('kopeechka_key')
    domain = data.get('email')
api = MailActivations(api_token=kop_key)

red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pink = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.YELLOW
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET

generated = 0
failed = 0
cap_solved = 0
proxy_error = 0
errors = 0
fingerprint = 0

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee


def generate_members():
    global generated, failed, cap_solved, proxy_error, errors
    url = "https://discord.com/api/v9/experiments"
    output_lock = threading.Lock()
    try:
        session = tls_client.Session(
        client_identifier="safari_ios_16_0"
        )


        session.proxies = {
            "http": proxy,
            "https": proxy,
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'https://discord.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'X-Track': 'eyJvcyI6IklPUyIsImJyb3dzZXIiOiJTYWZlIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKElQaG9uZTsgQ1BVIEludGVybmFsIFByb2R1Y3RzIFN0b3JlLCBhcHBsaWNhdGlvbi8yMDUuMS4xNSAoS0hUTUwpIFZlcnNpb24vMTUuMCBNb2JpbGUvMTVFMjQ4IFNhZmFyaS82MDQuMSIsImJyb3dzZXJfdmVyc2lvbiI6IjE1LjAiLCJvc192IjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfZG9tYWluX2Nvb2tpZSI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOiJzdGFibGUiLCJjbGllbnRfZXZlbnRfc291cmNlIjoic3RhYmxlIn0',
        }

        response = session.get('https://discord.com/api/v9/experiments', headers=headers)
        if response.status_code == 200:
            data = response.json()
            fingerprint = data["fingerprint"]
            with output_lock:
                time_rn = get_time_rn()
                print(f"{reset}[ {yellow}{time_rn}{reset} ] {gray}({lightblue}@{gray}) {pink}Got Fingerprint {gray}: {magenta}{fingerprint}")
        else:
            with output_lock:
                time_rn = get_time_rn()
                print(f"{reset}[ {yellow}{time_rn}{reset} ] {gray}({red}-{gray}) {pink}Failed Getting Fingerprint {gray}| {red}Bad Gateaway")
            errors += 1
            generate_members()
        captcha_code = 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hKdwYXNza2V5xQbV'
        cap = Solver.solve_capmonster(site_key='4c672d35-0701-42b2-88c3-78380b0db560', page_url='https://discord.com/')
        cap_solved += 1
        with output_lock:
            time_rn = get_time_rn()
            print(f"{reset}[ {yellow}{time_rn}{reset} ] {gray}({yellow}!{gray}) {pink}Solved Captcha {gray}: {magenta}{captcha_code}")
        
        def get_email():
            try:
                response = api.mailbox_get_email(site='discord.com', mail_type=domain, soft_id=99)
                if response.status == 'OK':
                    return response
                else:
                    raise Exception('Failed to get email.')
            except KopeechkaApiError as e:
                raise Exception(e)    


        
        def create_payload():
            url = "https://raw.githubusercontent.com/TahaGorme/100k-usernames/main/usernames.txt"
            response = requests.get(url)
            lines = response.text.splitlines()
            random_user = random.choice(lines)
           # print(random_user)
            username = fake.user_name() + '.ihbik' + str(randint(1, 9))
           # print(username)
            password = 'Lemons' + str(randint(1, 9)) + '_iscool'
           # print(password)
            test_email= get_email()
           # print(test_email)
            email = test_email.mail
           # print (email)
            #print (test_email.id)


            payload = {
                'consent': True,
                'fingerprint': fingerprint,
                'captcha_key': cap,
                'email': email,
                'password': password,
                'date_of_birth' : '2002-03-01',
                'global_name' : random_user,
                'username' : username,
                'promotional_email_opt_in' : True
            }
            return payload, test_email.id, username


        payload, taskid, username,= create_payload()
       
        password = payload['password']
        email = payload['email']
        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9',
            'referer': 'https://discord.com/',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            'x-track': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
            'x-fingerprint': fingerprint
        }
        response = session.post('https://discord.com/api/v9/auth/register', headers=headers, json=payload)
       






        if "token" not in response.text:
            if "retry_after" in response.text:
                with output_lock:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {yellow}{time_rn}{reset} ] {gray}({red}-{gray}) {pink}Ratelimit {gray}| {red}{response.json().get('retry_after')}s")
                errors += 1
                proxy_error += 1
                failed += 1
        token = response.json().get('token')
        if token == None:
            errors += 1
            generate_members()
        else:
            with output_lock:
                time_rn = get_time_rn()
                print(f"{reset}[ {yellow}{time_rn}{reset} ] {gray}({green}+{gray}) {pink}Generated {gray}: ", end='')
                sys.stdout.flush()
                Write.Print(token + "\n", Colors.purple_to_blue, interval=0.000)
                generated += 1

                


                with open("tokens.txt", "a") as f:
                        f.write(f"{token}:{email}:{password}:{username}\n")



                
                def get_token_by_link(link: str):
                   # print ('get_token_by_link')
                    return str(httpx.get(link, follow_redirects=True).url).split('https://discord.com/verify#token=')[1]

                def get_verification_token(task_id):
                   # print ('get_verification_token')
                    tries = 0
                    while tries < 300:
                        response = httpx.get(f"http://api.kopeechka.store/mailbox-get-message?id={task_id}&token={kop_key}&api=2.0")
                       # print ('sent request')
                        if 'OK' in response.text:
                            token = get_token_by_link(response.json()['value'])

                            #print (token)
                            return token
                        else:
                       #     print(tries)
                            tries += 1
                            time.sleep(1)
                            
                    api.mailbox_cancel(task_id)     
                    
                    print (f"{reset}[ {yellow}{time_rn}{reset} ] {gray}({red}-{gray}) {red}Failed to Verify {gray}| {red}{token}")



                print(f"{reset}[ {yellow}{time_rn}{reset} ] {gray}({red}-{gray}) {pink}Attempting to Verify eMail {gray}: ", end='')
                sys.stdout.flush()
                Write.Print(token + "\n", Colors.purple_to_blue, interval=0.000)   
                vtoken = get_verification_token(taskid)
                
                def verify(vtoken):
                   # print ('verify')
                    cap = Solver.solve_capmonster(site_key='f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34', page_url=f'https://discord.com/')
                    payload = {'token': vtoken, "captcha_key": cap}
                    
                    response = session.post(f'https://discord.com/api/v9/auth/verify',json=payload, headers=headers)
                    if response.status_code == 200:
                        print (f"{reset}[ {yellow}{time_rn}{reset} ] {gray}({green}+{gray}) {pink}Succesfully Verified eMail{gray} : ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_blue, interval=0.000)
                        return 'Verified'
                        
                    else:
                        
                    
                        return 'Not Verified'
                    


               
                gg = verify(vtoken)
                
                
                
                            
                            
                
                
                generate_members()
    except:
        proxy_error += 1
        failed += 1
        generate_members()

Write.Print(f"""
\t\t  _______    _                 _____             
\t\t |__   __|  | |               / ____|            
\t\t    | | ___ | | _____ _ __   | |  __  ___ _ __   
\t\t    | |/ _ \| |/ / _ \ '_ \  | | |_ |/ _ \ '_ \  
\t\t    | | (_) |   <  __/ | | | | |__| |  __/ | | | 
\t\t    |_|\___/|_|\_\___|_| |_|  \_____|\___|_| |_| 
""", Colors.purple_to_blue, interval=0.000)
print(f"\n\n")
proxy = input(f"{reset}[ {yellow}{get_time_rn()}{reset} ] {gray}({lightblue}?{gray}) {pink}Enter Proxy {gray}: {reset}")
time.sleep(1)
def run():
    while True:
        generate_members()

with open("config.json") as f:
    data = json.load(f)

num_threads = data.get('threads', 100)
threads = []
for i in range(int(num_threads)):
    thread = threading.Thread(target=run, name=f"BOOSTER-{i+1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
