import io,sys,os,argparse
import json
import requests
from datetime import datetime

from pushbullet import Pushbullet

class WebAlert:

    def __init__(self,url):
        print(f"WebAlert: {url}")
        self.load_parameters()
        d = requests.get(url)
        if d.status_code != 200:
            self.notificationCount += 1
            self.lastStatus = "DOWN"
            if self.notificationCount <= self.maxNotificationCount:
                self.send_alert(url)
        else:
            self.notificationCount = 0
            self.lastStatus = "UP"
        self.save_parameters()
    
    def send_alert(self,url):
        print("Its down")
        pb = Pushbullet(self.api_key)
        push = pb.push_note("Down",f"{url} its down")

    def save_parameters(self):
        print("Updated count!")
        with open(self.filename, "w") as jsonFile:
            self.parameter["lastCheck"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.parameter["lastStatus"] = self.lastStatus
            self.parameter["notificationCount"] = self.notificationCount
            json.dump(self.parameter, jsonFile)
        jsonFile.close()

    def load_parameters(self):
        self.filename = os.environ.get('CONFIGURATION_FILE')

        self.api_key = os.environ.get('APIKEY_PUSBULLET')

        if os.path.isfile(self.filename):
            with open(self.filename) as json_file:
                self.parameter = json.load(json_file)
                self.lastCheck = self.parameter["lastCheck"]
                self.notificationCount = self.parameter["notificationCount"]
                self.maxNotificationCount = self.parameter["maxNotificationCount"]
                self.lastStatus = self.parameter["lastStatus"]
        else:
            print("There is not configuration file")
            sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This script allow to send notification if url is down')
    
    parser.add_argument("url", help="URL to check")
    
    args = parser.parse_args()
    webAlert = WebAlert(args.url)