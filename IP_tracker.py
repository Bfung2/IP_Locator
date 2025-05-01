import json
import requests
import time
import os

Bl = '\033[30m'  # VARIABLE BUAT WARNA CUYY
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'
def commands():
    command = (input(f"{Cy}input-->"))
    
    if "1" in command:
        clear()
        IP_Tracking()
    elif "2" in command:
        clear()
        showIP()
    elif "3" in command:
        clear()
        print(f"{Re} bye")
        time.sleep(1)
        print(f"{Wh}")
        exiting()
    else:
        for x in range(1,4):
            clear()
            print(f"{Re} re-type your option in " )
            print(x)
            time.sleep(1)
        clear()
        main()
        

    


def IP_Tracking():
    try:

        print(f"{Wh}-----------------{Re}IP Tracker{Wh}----------------")
        command = (input(f"{Re}Input IP{Cy}: "))# INPUT IP ADDRESS
        ip = command  
        print()
        print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
        req_api = requests.get(f"http://ipwho.is/{ip}")  # API IPWHOIS.IS
        ip_data = json.loads(req_api.text)
        lat = int(ip_data['latitude'])
        lon = int(ip_data['longitude'])
        time.sleep(2)
        print(f"{Gr}==========={Re}Location{Gr}============")
        print(f"{Wh} Latitude        :{Gr}", ip_data["latitude"])
        print(f"{Wh} Longitude       :{Gr}", ip_data["longitude"])
        print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
        time.sleep(2)
        print(f"{Gr}==========={Re}General Location{Gr}============")
        print(f"{Wh} Country         :{Gr}", ip_data["country"])
        print(f"{Wh} Country Code    :{Gr}", ip_data["country_code"])
        print(f"{Wh} City            :{Gr}", ip_data["city"])
        print(f"{Wh} Continent       :{Gr}", ip_data["continent"])
        print(f"{Wh} Continent Code  :{Gr}", ip_data["continent_code"])
        print(f"{Wh} Region          :{Gr}", ip_data["region"])
        print(f"{Wh} Region Code     :{Gr}", ip_data["region_code"])
        print(f"{Wh} Country Flag    :{Gr}", ip_data["flag"]["emoji"])
        time.sleep(2)
        print(f"{Gr}==========={Re}Time-Zone{Gr}============")
        print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
        print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
        print(f"{Wh} DST             :{Gr}", ip_data["timezone"]["is_dst"])
        print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])
        print(f"{Wh} UTC             :{Gr}", ip_data["timezone"]["utc"])
        print(f"{Wh} Current Time    :{Gr}", ip_data["timezone"]["current_time"])
        time.sleep(2)
        print(f"{Gr}==========={Re}Connection{Gr}============")
        print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
        print(f"{Wh} ORG             :{Gr}", ip_data["connection"]["org"])
        print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
        print(f"{Wh} Domain          :{Gr}", ip_data["connection"]["domain"])
        time.sleep(2)
        print(f"{Gr}==========={Re}Other Information{Gr}============")
        print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
        print(f"{Wh} EU              :{Gr}", ip_data["is_eu"])
        print(f"{Wh} Postal          :{Gr}", ip_data["postal"])
        print(f"{Wh} Calling Code    :{Gr}", ip_data["calling_code"])
        print(f"{Wh} Capital         :{Gr}", ip_data["capital"])
        print(f"{Wh} Borders         :{Gr}", ip_data["borders"])
        print("")
        print(f"{Gr}[{Bl}Press enter to continue{Gr}]")
        Execute()
    except requests.exceptions.RequestException as e:
        print(f"{Re}Error: {e}")
    except KeyError:
        print(f"{Re}Invalid IP address")
    except json.JSONDecodeError:
        print(f"{Re}Error decoding JSON response")
    except Exception as e:
        print(f"{Re}An unexpected error occurred: {e}")
    finally:
        print(f"{Wh}Exiting IP Tracker...")
        time.sleep(2)
        clear()
        main()
def exiting():
    clear()
    exit()
def Execute():
    try:
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to continue')
        clear()
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')
def showIP():
    try:
        respone = requests.get('https://api.ipify.org/')
        Show_IP = respone.text

        print(f"\n {Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========")
        print(f"\n {Wh}[{Gr} + {Wh}] Your IP Adrress : {Gr}{Show_IP}")
        print(f"\n {Wh}==============================================")
        print("")
        print(f"{Wh}======={Cy} would you like to see your IP info? {Wh}=======")
        command = (input(f"{Cy} input--->"))

        if "yes" in command:
            clear()
            IP_With_Info()
        else:
            clear()
            main() 
    except requests.exceptions.RequestException as e:
        print(f"{Re}Error: {e}")
    except KeyError:
        print(f"{Re}xould not find your IP address")
    except json.JSONDecodeError:
        print(f"{Re}Error decoding JSON response")
    except Exception as e:
        print(f"{Re}An unexpected error occurred: {e}")
    finally:
        print(f"{Wh}Exiting IP Tracker...")

    
    

def IP_With_Info():
    try:

        respone = requests.get('https://api.ipify.org/')
        Show_IP = respone.text
        ip = Show_IP
        print()
        print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
        req_api = requests.get(f"http://ipwho.is/{ip}")  # API IPWHOIS.IS
        ip_data = json.loads(req_api.text)
        lat = int(ip_data['latitude'])
        lon = int(ip_data['longitude'])
        time.sleep(2)
        print(f"{Gr}==========={Re}Location{Gr}============")
        print(f"{Wh} Latitude        :{Gr}", ip_data["latitude"])
        print(f"{Wh} Longitude       :{Gr}", ip_data["longitude"])
        print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
        time.sleep(2)
        print(f"{Gr}==========={Re}General Location{Gr}============")
        print(f"{Wh} Country         :{Gr}", ip_data["country"])
        print(f"{Wh} Country Code    :{Gr}", ip_data["country_code"])
        print(f"{Wh} City            :{Gr}", ip_data["city"])
        print(f"{Wh} Continent       :{Gr}", ip_data["continent"])
        print(f"{Wh} Continent Code  :{Gr}", ip_data["continent_code"])
        print(f"{Wh} Region          :{Gr}", ip_data["region"])
        print(f"{Wh} Region Code     :{Gr}", ip_data["region_code"])
        print(f"{Wh} Country Flag    :{Gr}", ip_data["flag"]["emoji"])
        time.sleep(2)
        print(f"{Gr}==========={Re}Time-Zone{Gr}============")
        print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
        print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
        print(f"{Wh} DST             :{Gr}", ip_data["timezone"]["is_dst"])
        print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])
        print(f"{Wh} UTC             :{Gr}", ip_data["timezone"]["utc"])
        print(f"{Wh} Current Time    :{Gr}", ip_data["timezone"]["current_time"])
        time.sleep(2)
        print(f"{Gr}==========={Re}Connection{Gr}============")
        print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
        print(f"{Wh} ORG             :{Gr}", ip_data["connection"]["org"])
        print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
        print(f"{Wh} Domain          :{Gr}", ip_data["connection"]["domain"])
        time.sleep(2)
        print(f"{Gr}==========={Re}Other Information{Gr}============")
        print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
        print(f"{Wh} EU              :{Gr}", ip_data["is_eu"])
        print(f"{Wh} Postal          :{Gr}", ip_data["postal"])
        print(f"{Wh} Calling Code    :{Gr}", ip_data["calling_code"])
        print(f"{Wh} Capital         :{Gr}", ip_data["capital"])
        print(f"{Wh} Borders         :{Gr}", ip_data["borders"])
        print("")
        print(f"{Gr}[{Bl}Press enter to continue{Gr}]")
        Execute()
    except requests.exceptions.RequestException as e:
        print(f"{Re}Error: {e}")
    except KeyError:
        print(f"{Re}Invalid IP address")
    except json.JSONDecodeError:
        print(f"{Re}Error decoding JSON response")
    except Exception as e:
        print(f"{Re}An unexpected error occurred: {e}")
    finally:
        print(f"{Wh}Exiting IP Tracker...")

def main():
    clear()
    print(f"{Wh}-----------{Bl}Options{Wh}--------------")
    print(f"{Gr}[{Wh} 1{Gr}]{Bl}Track Any IP Address")
    print(f"{Gr}[{Wh} 2{Gr}]{Bl}Show your IP Address")
    print(f"{Gr}[{Wh} 3{Gr}]{Bl}exit")
    
    print(f"{Wh} =========={Gr}What can I do for you?{Wh}==========")
    commands()


        


if __name__ == '__main__':
    try:
        
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()