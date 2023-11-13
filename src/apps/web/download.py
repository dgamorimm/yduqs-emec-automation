import requests
import wget
import zipfile
import os

class DownloadDriver:
    
    def __init__(self) -> None:
        self.url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        self.response = requests.get(self.url)
        self.version_number = self.response.text
        self.download_url = "https://chromedriver.storage.googleapis.com/" + self.version_number +"/chromedriver_win32.zip"
        self.path_browser = os.path.join(os.path.abspath('.'),'src','apps','web','chromedriver')

    def download_chromedriver_latest_release(self):
        latest_driver_zip = wget.download(self.download_url,os.path.join(self.path_browser,'chromedriver.zip'))
        print(latest_driver_zip)
        return latest_driver_zip

    def extract_chromedriver_zip(self, chromedriver_zip):
        with zipfile.ZipFile(chromedriver_zip, 'r') as zip_ref:
            zip_ref.extractall(self.path_browser)
        os.remove(chromedriver_zip)
    
    def get_driver(self):
        _zip = self.download_chromedriver_latest_release()
        self.extract_chromedriver_zip(_zip)
        
if __name__ == '__main__':
    driver = DownloadDriver()
    driver.get_driver()