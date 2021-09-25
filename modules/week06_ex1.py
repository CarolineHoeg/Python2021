import requests
from concurrent.futures import ThreadPoolExecutor

class NotFoundException(Exception):
    pass
        
        
class TextComparer():
    
    def __init__(self, url_list):
        self.url_list = url_list
    
    def download(self, url, filename):
        try:
            r = requests.get(url)
            with open('./downloads/' + filename, 'wb') as file_object:
                for chunk in r.iter_content(chunk_size=1024):
                    file_object.write(chunk)
        except ConnectionError:
            raise NotFoundException
    
    def multi_download(self):
        i = 1
        with ThreadPoolExecutor() as exc:
            for url in self.url_list:
                filename = 'download' + str(i) +'.txt'
                exc.submit(self.download, url, filename)
                i += 1
    
#    def __iter__(self):  
        
#    def __next__(self):

    def avg_vowels(self, text):
        vowels = 0
        words = 0
        
        return vowels