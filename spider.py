import urllib
from bs4 import BeautifulSoup as BS
from pypinyin import pinyin, lazy_pinyin, Style, load_phrases_dict, load_single_dict
import os, time, math, string, json, re
from zhon.hanzi import punctuation

re_punc = "[{}]+".format(punctuation + string.punctuation)

#os.chdir("E:\大二下ver2\人智导\大作业1\spider")
URL = "https://baike.baidu.com/item" 
#URL = "https://baike.baidu.com/item" + "/" + urllib.parse.quote("钢之炼金术师")

lines = open("bufan.txt", "r").readlines()
bufan = list(map(lambda x: re.sub("\n", "", x), lines))

def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


f = open("bufan_data.txt", "w", encoding = "utf-8")
for fan in bufan:
    print(fan)
    time_start = time.time()
    html = str(urllib.request.urlopen(URL + "/" + urllib.parse.quote(fan)).read(), "UTF-8")
    soup = BS(html, "html.parser")
    divs = soup.find_all("div", {"class": "para"})
    for div in divs:
        text = re.split(re_punc, div.text)
        for s in text:
            s = "".join((list(filter(lambda x: is_Chinese(x), s))))
            if(len(s) < 2):
                continue
            p = " ".join(lazy_pinyin(s))
            f.write(s + "\n")
            f.write(p + "\n")
    time_end = time.time()
    print("Cost time: " + str(time_end - time_start))
    
f.close()

