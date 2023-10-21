try:
    import requests
except ImportError:
    print("Please install the requests module.")
    exit()
import json
from pprint import pprint

url = "https://raw.githubusercontent.com/MaximumADHD/Roblox-Client-Tracker/roblox/API-Dump.json"
r = requests.get(url)
data = r.json()

Version = data["Version"]
Classes = data["Classes"]
Enums = data["Enums"]

def render(creator):
    file = ""
    file += creator.Section.format(Name="Enums")
    for i in Enums:
        Name = i["Name"]
        Data = i["Items"]
        
        file += creator.EnumCore.format(Name=Name)
        for item in Data:
            file += creator.EnumItem.format(Name=item["Name"], Value=item["Value"])
        file += creator.EnumEnd.format(Name=Name)
        
    return file

class Creator: # C++ Example
    Section = """// {Name}\n"""
    
    EnumCore = """namespace {Name} {{\n\tenum RobloxEnum {{\n"""
    EnumItem = """\t\t{Name} = {Value},\n"""
    EnumEnd = """\t}};\n}}\n\n"""
    
def main():
    file = render(Creator)
    print(file)
        
if __name__ == "__main__":
    main()