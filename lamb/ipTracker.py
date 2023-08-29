from rich import print as rprint
import json
from urllib.request import urlopen

def it():
    
    ip = input("\nIP For Track : ")
    response = urlopen(f"https://extreme-ip-lookup.com/json/{ip}?key=demo2")
    geo = json.load(response)
    x = "[green bold][[red]+[/red]][/green bold]"

    rprint(x+"[magenta2]Hostaname : [/magenta2]"+ ip)
    rprint(x+"[magenta1]asn : [/magenta1]"+geo["asn"])
    rprint(x+"[magenta2]asnOrg : [/magenta2]"+geo["asnOrg"])
    rprint(x+"[magenta1]Business : [/magenta1]"+geo["businessName"])
    rprint(x+"[magenta2]Website : [/magenta2]"+geo["businessWebsite"])
    rprint(x+"[magenta1]City : [/magenta1]"+geo["city"])
    rprint(x+"[magenta2]Continent : [/magenta2]"+geo["continent"])
    rprint(x+"[magenta1]Country : [/magenta1]"+geo["country"])
    rprint(x+"[magenta2]Country Code : [/magenta2]"+geo["countryCode"])
    rprint(x+"[magenta1]IP Name : [/magenta1]"+geo["ipName"])
    rprint(x+"[magenta2]IP Type : [/magenta2]"+geo["ipType"])
    rprint(x+"[magenta1]isp : [/magenta1]"+geo["isp"])
    rprint(x+"[magenta2]Latitude : [/magenta2]"+geo["lat"])
    rprint(x+"[magenta1]Longitude : [/magenta1]"+geo["lon"])
    rprint(x+"[magenta2]Organisation : [/magenta2]"+geo["org"])
    rprint(x+"[magenta1]Query : [/magenta1]"+geo["query"])
    rprint(x+"[magenta2]Region : [/magenta2]"+geo["region"])
    rprint(x+"[magenta1]Status : [/magenta1]"+geo["status"])
    rprint(x+"[magenta2]Timezone : [/magenta2]"+geo["timezone"])
    rprint(x+"[magenta1]utcOffset : [/magenta1]"+geo["utcOffset"])
    input("Press Enter To Continue")

