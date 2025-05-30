import argparse
import json
import requests

# Initialize parser
parser = argparse.ArgumentParser(description="Save IP address input.")

# Add optional argument (like -8.8.8.8)
parser.add_argument("ip", help="The IP address to save as a string")
args = parser.parse_args()
IP = args.ip

try:
    req_api = requests.get(f"http://ipwho.is/{IP}")
    ip_data = json.loads(req_api.text)
    lat = ip_data['latitude']
    lon = ip_data['longitude']
    print(f"Tracking IP: {IP}\n")
    #location details
    print(f"=====Location=====\n")
    print(f"Latitude: {lat}\n")
    print(f"Longitude: {lon}\n")
    print(f"Maps: https//www.google.com/maps/@{lat},{lon},8z\n")
    #general location like continent, country, city
    
    print(f"\n====General Location ===\n")
    print(f"City: {ip_data['city']}\n")
    print(f"Country: {ip_data['country']}\n")
    print(f"Continent: {ip_data['continent']}\n")
    print(f"Continent Code: {ip_data['continent_code']}\n")
    print(f"Region: {ip_data['region']}\n")
    # Time Zone details
    print(f"\n======Time Zone ======\n")
    print(f"Time Zone: {ip_data['timezone']}\n")
    print(f"Time Zone ID: {ip_data['timezone']['id']}\n")
    print(f"Time Zone Offset: {ip_data['timezone']['offset']}\n")
    print(f"Time Zone Abbr: {ip_data['timezone']['abbr']}\n")
    print(f"Is Daylight Saving Time: {ip_data['timezone']['is_dst']}\n")
    print(f"current Time : {ip_data['timezone']['current_time']}\n")
    print(f"UTC: {ip_data['timezone']['utc']}\n")
    #connection
    print(f"\n===========Connection============\n")
    print(f"ASN: {ip_data['connection']['asn']}\n")
    print(f"ORG: {ip_data['connection']['org']}\n")
    print(f"ISP: {ip_data['connection']['isp']}\n")
    print(f"Domain: {ip_data['connection']['domain']}\n")
    

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit(1)
except KeyError:
    print("Invalid IP address\n")
except json.JSONDecodeError:
    print( "Error decoding JSON response\n")
except Exception as e:
    print(f"An unexpected error occurred: {e}\n")
