from readfile import readfile
import linecache
import string

OCCURENCE_LIST_PATH = "./Occurence_List.dat" ## occurence list save address

if __name__ == '__main__':
    keyTrie = readfile()
    print("FILE LOAD FINISH.")
    print("##################################")
    print("INPUT -h FOR HELP")
    print("INPUT -q TO QUIT THE SEARCH ENGINE")
    print("This search engine support multiple search. If you want to search multiple keyword, you should use space to separate the keywords.")
    print("Ex: 'nltk data'") 
    print("This search engine also support prefix search.")
    print("Ex: We have 'data', 'database' and 'dat' in trie. We input 'da', algorithm will return the most frequently in data, database and dat.")
    print("##################################\n")
    lastSearchKey = ""
    lastSearchResult = []
    while(True):
        inputString = input("\nWhat key word you want to search now:  ")
        inputString = inputString.strip()
        ###### INSTRUCTION ######
        if inputString == "-h" or inputString == "-H" or inputString == "-help":
            print("------- HELP LIST: -------")
            print("-h -H -help ======> HELP")
            print("-q -Q -quit ======> TO QUIT THE SEARCH ENGINE")
            print("-s -S -save ======> SAVE THE LAST SEARCH RESULT")
            print("--------------------------\n")
            continue
        if inputString == "-q" or inputString == "-Q" or inputString == "-quit":
            print("QUIT SEARCH ENGINE")
            break
        if inputString == "-s" or inputString == "-S" or inputString == "-save":
            if lastSearchKey == "":
                print ("No record!")
                continue
            f  = open('./output/output.txt','a')
            for element in lastSearchKey:
                print(element + " ")
                f.write(element + " ")
            f.write("\n")
            for (i,j,x,y) in lastSearchResult:
                f.write(i + " " + str(j) + " " + str(x) + " " + y + "\n")
            f.close
            print("Saved\n")
            continue
        #########################

        ###### PROCESS THE INPUT INTO SEVERAL KEYS ######
        inputString = "".join((char for char in inputString if char not in string.punctuation))
        inputKey = inputString.lower().split()
        inputKey = list(set(inputKey))
        key_occurence_list = []  ## store all occurence list
        if inputKey == []:
            print("You input is empty!")
            continue
        #################################################

        ###### SEARCH EVERY KEY IN YOUR LIST AND RETRUN EVERY KEY OCCURENCE LIST ######
        for key in inputKey:
            trieValue = keyTrie.searchValue(key)
            if trieValue == None: ## No such key
                pass
            elif trieValue == False: ## Part of this key in trie. Ex. we have data, database and dat in trie. We input "da", algorithm will return the most frequently in data, database and dat.
                node = keyTrie.getTrieNode(key)
                result = keyTrie.dfs(node)
                resultNew =[]
                for word in result:
                    s = key + word
                    resultNew.append(s)
                large_freq = 0
                large_freq_word = ""
                large_freq_word_value = 0
                for word in resultNew:
                    temp_value = keyTrie.searchValue(word)
                    line = linecache.getline(OCCURENCE_LIST_PATH, temp_value + 1)
                    l = line.split("|||")
                    if int(l[1]) > int(large_freq):
                        large_freq = l[1]
                        large_freq_word = word
                        large_freq_word_value = temp_value

                print("You may want to find: ",large_freq_word)
                line = linecache.getline(OCCURENCE_LIST_PATH, large_freq_word_value + 1)
                l = line.split("|||")
                if l.pop(0) != large_freq_word:
                    print("Search failed!")
                    break
                
                key_freq = l.pop(0)

                one_list = []
                while l[0] != "\n":
                    currentPair = (l.pop(0),l.pop(0),l.pop(0),l.pop(0))
                    one_list.append(currentPair)
                
                key_occurence_list.append(one_list)

            else: ## The key is in trie
                line = linecache.getline(OCCURENCE_LIST_PATH, trieValue + 1)
                l = line.split("|||")
                if l.pop(0) != key:
                    print("Search failed!")
                    break
                
                key_freq = l.pop(0)

                one_list = []
                while l[0] != "\n":
                    currentPair = (l.pop(0),l.pop(0),l.pop(0),l.pop(0))
                    one_list.append(currentPair)
                
                key_occurence_list.append(one_list)
        ###############################################################################

        ####### SHOW THE SEARCH RESULT ######
        if key_occurence_list == []:
            print("There are no result!")
            continue
        ## merge the occurence list
        while len(key_occurence_list) != 1:
            tempList = []
            list1 = key_occurence_list.pop(0)
            list2 = key_occurence_list.pop(0)
            while len(list1) != 0 or len(list2) != 0:
                if len(list1) != 0 and len(list2) == 0:
                    tempList.append(list1.pop(0))
                elif len(list2) != 0 and len(list1) == 0:
                    tempList.append(list2.pop(0))
                elif list1[0][2] < list2[0][2]:
                    tempList.append(list1.pop(0))
                elif list1[0][2] > list2[0][2] :
                    tempList.append(list2.pop(0))
                else:
                    freq1 = int(list1[0][1]) 
                    freq2 = int(list2[0][1])
                    temp = list(list1.pop(0))
                    temp[1] = freq1 + freq2
                    tempList.append(tuple(temp))
                    list2.pop(0)
            key_occurence_list.append(tempList)
        
        showList = key_occurence_list[0]
        showList.sort(key = lambda x:int(x[1]), reverse = True)
        
        print("Search result: ")
        numSeqence = 1
        for element in showList:
            print(str(numSeqence)+". File address: "+element[0]+"\tweb address: "+element[3])
            numSeqence += 1
        lastSearchKey = inputKey
        lastSearchResult = showList
        
        ######################################