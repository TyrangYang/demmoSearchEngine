import json
import string
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from invertedFile import invertFile

def readfile():
    invert_File = invertFile()
    MAP_PATH = "file_link_map.json"  ## THIS JSON STORE ALL PAGE ADDRESS. THE WEB CRAWLER SHOULD MAINTAIN THIS JSON WHEN ADD NEW PAGE
    LEN_SHORT_WORD = 2 ## THIS USED TO FILTER THE WORD SMALLER THAN THIS LENGTH.  
    SPECIAL_PUNCTUATION = "¶" ## THIS USED TO FILTER SOME SPECIAL PUNCTUATION.

    ####### READ ALL PAGES #######
    f = open(MAP_PATH,'r')
    temp_string = ""
    temp_array = f.readlines()
    file_link_string = temp_string.join(temp_array)
    file_link_map = json.loads(file_link_string)
    ##############################

    print(file_link_map)
    pageSeqence = 1
    for fileAddress in file_link_map:
        f = open(fileAddress)
        pageAddress = file_link_map[fileAddress]
        ####### USE BEAUTIFUL SOUP TO ANALYSIS HTML #######
        soup=BeautifulSoup(f.read(),'html5lib') ## html5lib is a better parser
        text = soup.get_text(strip=True)

        ####### CREAT THE STOP WORD LIST. THIS LIST CONTAIN ALL COMMON STOP WORD. SUCH AS: I, AM, THE, WHEN
        stopWords = stopwords.words('english') 

        ####### REPLACE ALL PUNCTUATION AND DIGIT TO SPACE #######
        del_estr = string.punctuation + string.digits + SPECIAL_PUNCTUATION
        replace = " "*len(del_estr)
        tran_tab = str.maketrans(del_estr, replace)
        text = text.translate(tran_tab)
        ##########################################################

        token = word_tokenize(text) ## use NLTK to split the text. we can use split() to saperate the string as well, however, NLTK is more better

        token = [word.lower() for word in token if word.lower() not in stopWords and len(word)>LEN_SHORT_WORD] ## change every word into lower and remove stop words and short words
        
        freqDist = nltk.FreqDist(token) ## get the freqency of all key that used to rank the sort result.

        ####### CREATE THE INVERT FILE #######
        for key,freq in freqDist.items(): 
            invert_File.put(key,freq,pageSeqence,fileAddress,pageAddress)
        pageSeqence += 1

        print("webside:",fileAddress,"web:",pageAddress)
        #######################################

        f.close()

    ####### SAVE THE INVERT FILE #######
    invert_File.saveInvertFile()
    
    return invert_File.keyTrie

# readfile()