import requests
from concurrent.futures import ThreadPoolExecutor
import multiprocessing

class NotFoundException(Exception):
    pass
        
        
class TextComparer():
    
    def __init__(self, url_list):
        self.url_list = url_list
        self.file_names = []
    
    def download(self, url, file_name):
        try:
            r = requests.get(url)
            if (r.status_code == 404):
                raise NotFoundException
            else:
                with open('./outputs/' + file_name, 'wb') as file_object:
                    for chunk in r.iter_content(chunk_size=1024):
                        file_object.write(chunk)
        except NotFoundException:
            print("The site you were looking for wasn't found")
    
    def multi_download(self):
        i = 0
        max_workers = multiprocessing.cpu_count()
        with ThreadPoolExecutor(max_workers) as exc:
            for url in self.url_list:
                file_name = 'download' + str(i) + '.txt'
                self.file_names.append(file_name)
                exc.submit(self.download, url, file_name)
                i += 1
    
    def __iter__(self):
        self.current_id = 0
        return self
        
    def __next__(self):
        if self.current_id >= len(self.url_list):
            raise StopIteration
        else:
            self.current_id += 1
            return self.file_names[self.current_id - 1]

    def url_list_generator(self):
        for url in self.url_list:
            yield url

    def avg_vowels(self, text):
        return 0
    
    def hardest_read(self):
        return 0