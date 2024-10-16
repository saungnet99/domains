import requests
import os
import re
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, Style, init

init(autoreset=True)

def MrClay_TeamleetsDomain(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        response = requests.get('https://api.reverseipdomain.com/?ip=' + url, headers=headers, timeout=30)
        x = response.content.decode('utf-8')
        if 'Domain Name' in x:
            regex = re.findall('<a href="/domain/(.*?)">', x)
            for domain_name in regex:
                website_url = 'http://' + domain_name
                print(f"Fucked Domain: {website_url}")
                with open('FuckedDomains.txt', 'a') as file:
                    file.write(website_url + '\n')
        else:
            print(f"IP IS GOOD - GRABBING ALL DOMAIN {url}")
    except Exception as e:
        print(f"Error: {e}")
        pass

def ClayTeamleets_dns(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        response = requests.get('https://rapiddns.io/s/' + url + '?full=1&down=1#result/', headers=headers, timeout=30)
        x = response.content.decode('utf-8')
        if '<th scope="row ">' in x:
            regex = re.findall('<td>(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}</td>', x)
            for domain_name in regex:
                website_url = 'http://' + domain_name.replace('<td>', '').replace('</td>', '').replace('ftp.', '').replace('images.', '').replace('cpanel.', '').replace('cpcalendars.', '').replace('cpcontacts.', '').replace('webmail.', '').replace('webdisk.', '').replace('hostmaster.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '').replace('autodiscover.', '')
                print(f"IP GOOD DOMAIN GRABBED: {website_url}")
                with open('DOMAINSZAZA.txt', 'a') as file:
                    file.write(website_url + '\n')
        else:
            print(f"BAD IP {url}")
    except Exception as e:
        print(f"Error: {e}")
        pass

def Teamleets_lookup(url):
    try:
        ClayTeamleets_dns(url)
        MrClay_TeamleetsDomain(url)
    except Exception as e:
        print(f"Error: {e}")
        pass

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        ip_list = input("Enter Your List: ")
        urls = open(ip_list, 'r').read().splitlines()
        num_threads = input("Enter Your Threads: ")
        pool = ThreadPool(int(num_threads))
        pool.map(Teamleets_lookup, urls)
    except Exception as e:
        print(f"Error: {e}")
        pass

if __name__ == '__main__':
    main()
