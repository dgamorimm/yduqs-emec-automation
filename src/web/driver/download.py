import requests
import wget
import zipfile
import os

class Driver:
    def __init__(self) -> None:
        # get the latest chrome driver version number
        self.url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        self.response = requests.get(self.url)
        self.version_number = self.response.text

        # build the donwload url
        self.download_url = "https://chromedriver.storage.googleapis.com/" + self.version_number +"/chromedriver_win32.zip"

    def download_chromedriver_latest_release(self):
        # download the zip file using the url built above
        latest_driver_zip = wget.download(self.download_url,'chromedriver.zip')
        print(latest_driver_zip)
        return latest_driver_zip

    def extract_chromedriver_zip(self, chromedriver_zip):
        # extract the zip file
        with zipfile.ZipFile(chromedriver_zip, 'r') as zip_ref:
            zip_ref.extractall('.') # you can specify the destination folder path here
        # delete the zip file downloaded above
        os.remove(chromedriver_zip)
    
    def get_driver(self):
        _zip = self.download_chromedriver_latest_release()
        self.extract_chromedriver_zip(_zip)
        
if __name__ == '__main__':
    driver = Driver()
    
    driver.get_driver()