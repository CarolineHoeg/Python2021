import requests
from concurrent.futures import ThreadPoolExecutor
import multiprocessing

class NotFoundException(Exception):
    pass
        
        
class TextComparer():
    
    def __init__(self, url_list):
        """Initiates the TextComparer with a list of URLs and a file names list"""
        self.url_list = url_list
        self.file_names = []
    
    def download(self, url, file_name):
        """Stores the file on disk and raises NotFoundException when the URL returns 404"""
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
        """Uses threads to download multiple URLs as text and stores filenames on a property of the TextComparer class object"""
        i = 0
        max_workers = multiprocessing.cpu_count()
        with ThreadPoolExecutor(max_workers) as exc:
            for url in self.url_list:
                file_name = 'download' + str(i) + '.txt'
                self.file_names.append(file_name)
                #exc.submit(self.download, url, file_name)
                i += 1
    
    def __iter__(self):
        """Returns an iterator"""
        self.current_id = 0
        return self
        
    def __next__(self):
        """Returns the next filename (and stops when there are no more)"""
        if self.current_id >= len(self.url_list):
            raise StopIteration
        else:
            self.current_id += 1
            return self.file_names[self.current_id - 1]

    def url_list_generator(self):
        """Returns a generator to loop through the URLs"""
        for url in self.url_list:
            yield url

    def avg_vowels(self, text):
        """Returns average number of vowels in the words of the text"""
        vowel_count = 0
        word_count = 0
        for word in text.split():
            vowel_count += sum(x in 'aeiou' for x in word.lower()) 
            word_count += 1
        return vowel_count / word_count
    
    def hardest_read(self):
        """Reads all text from files in filenames and returns the filename of the text with the highest vowel score"""
        highest_vowel_count = ''
        return highest_vowel_count