import requests

def main():
    r = requests.get("http://api.open-notify.org/astros.json")
    
    print("People in space: " + str(r.json().get("number")))
    
    for data in r.json()["people"]:
        
        print(data.get("name") + " on the " + data.get("craft"))

    



main()
