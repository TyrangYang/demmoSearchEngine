# Search Engine

Implement the simplified Search Engine described in Section 23.5.4 for the pages of a small Web site. Use all the words in the pages of the site as index terms, excluding stop words such as articles, prepositions, and pronouns.


## Dependencies
1. python 3.7.1 
2. beatifulsoup 
3. nltk 
4. VSCode 1.29.1

## Start Search Engine
1. Please make sure that you have python 3.
2. install beatifulsoup4 and nltk by using pip3.
```
sudo pip3 install beautifulsoup4
sudo pip3 install nltk
```
3. cd to the document where searchEngine.py is.
4. run searchEngine.py. 
```
python3 searchEngine.py
(DO NOT RUN "python searchEngine.py")
```

## Search
This search engine support multiple search. If you want to search multiple keyword, you should use space to separate the keywords.
> Ex: "nltk data" 

This search engine also support prefix search. 

> Ex: We have "data", "database" and "dat" in trie. We input "da", algorithm will return the most frequently in data, database and dat.

## Idea description
* Read all web pages from ./input.  Use beatifulsoup to extract all text.
* Use nltk to split the text and calcualate every word freqency.
* Use keyword-freqency to create inverted file. Save the occurence list on disk and keep trie in memory.
* User input the keywords. Read occurence list of these keywords by using the trie.
More detail is in code comment

## Inverted file data structure
Inverted file have a trie which constructed by keywords and a occurence list that contain a keyword information.

Trie is saved in memory and occurence lists are saved in a file on disk.

When you search a key in trie, that will return a number which associate to column of file of occurence list.

The structure of each column is like: 
```
[keyword, totalFreq, [(fileAddress, freq, pageSeq, webAddress),...,...]].
keyword - a key word.
totalFreq - how many times that this keyword appear in all page.
page detail:(fileAddress, freq, pageSeq, webAddress)
fileAddress - where this page store in disk
freq - how many times that this keyword appear in this page.
pageSeq - the sequence number of this page
webAddress - web address of this page
```

## Rank algorithm
All rank are based on the freqency. More times that a keyword appear in a web page, the higher ranking of the web page.

If using multiple search, we merge all occurence list of keyword. Add up all page freqency. 

The higher ranking means this page have the most amount of these keywords.

When you input a keyword that is not in trie but it is prefix of a exist keyword, the algorithm will find all keywords with this prefix，and use most frequent keyword to search.

## Input file rescourse

The input file is download from website. All page is from about NLTK 3.4 documentation. 

## Reference

* [Beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc)
* [NLTK](https://www.nltk.org)
* [NLTK example code](https://blog.csdn.net/hzp666/article/details/79373720)
* [Replace English punctuation with spaces](https://blog.csdn.net/hang916/article/details/83832381)
* [Linecache — Random access to text lines](https://docs.python.org/3.7/library/linecache.html#module-linecache)
* [Sort the tuple by certain element](https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples)