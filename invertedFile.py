from trie import Trie

class invertFile():

    def __init__(self):
        self.keyTrie = Trie()
        self.occurence_list = []
        self.list_length = 0

    def put(self,key,freq,seq,fileAddress,pageAddress): ## PUT ELEMENT INTO INVERTFILE
        if self.keyTrie.isWordExist(key): ## THIS IS A EXIST KEY
            occurence_list_index = self.keyTrie.searchValue(key)
            self.occurence_list[occurence_list_index][1] += freq
            self.occurence_list[occurence_list_index][2].append((fileAddress,freq,seq,pageAddress))
            self.occurence_list[occurence_list_index][2].sort(key = lambda x:x[2])

        else: ## THIS IS A NEW KEY
            ## CREATE OCCURENCE_LIST
            self.occurence_list.append([key,freq,[(fileAddress,freq,seq,pageAddress)]])
            ## PUT IT IN TRIE
            self.keyTrie.insert(key,self.list_length)
            self.list_length += 1
    
    def get(self,key): ## GET A OCCURENCE LIST OF A GIVEN KEY
        return self.occurence_list[self.keyTrie.searchValue(key)]
    
    def showDictionary(self): ## PRINT ALL INVERTFILE. THIS IS A METHOD FOR TEST
        allkey = self.keyTrie.showAllKey()
        for key in allkey:
            print(key,self.keyTrie.searchValue(key),self.get(key))

    def saveInvertFile(self,fileName = "Occurence_List.dat"): ## SAVE THE ALL OCCURENCE LIST
        f = open(fileName,'w')
        for [keyName,keyfreqency,Occurence_List] in self.occurence_list:
            f.write(keyName+"|||"+str(keyfreqency)+"|||")
            for (fileAddress,freqInPage,pageSeq,pageAddress) in Occurence_List:
                f.write(fileAddress+"|||"+str(freqInPage)+"|||"+str(pageSeq)+"|||"+pageAddress+"|||")
            f.write("\n")
        f.close()


# inf = invertFile()
# inf.put("nltk",10,"1.html",1,"www.q")
# inf.put("language",6,"1.html",1,"www.q")
# inf.put("nltk",10,"2.html",2,"www.e")
# print(inf.get("nltk"))
# inf.showDictionary()