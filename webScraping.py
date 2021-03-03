import csv
from bs4 import BeautifulSoup
from newspaper import Article
import nltk
nltk.download('punkt')
import string
from nltk.tokenize import RegexpTokenizer
import re

source = "https://shiftdelete.net/"
soup_list = ["https://shiftdelete.net/p"]

N = 100
webpage_list = [i+1 for i in range(N)] #sayfa numaralarının listesini döndürür
webpage_list.remove(11)
webpage_list.remove(17)
webpage_list.remove(33)
webpage_list.remove(44)
webpage_list.remove(48)
webpage_list.remove(51)
webpage_list.remove(59)#hatalı sayfaları çekmemesini sağlar
word_count = 0

with open('news.csv', 'a', encoding='utf-8', newline='') as news_output:
    csv_print = csv.writer(news_output)
    csv_print.writerow(['url', 'segment_no', 'cumle_icerigi', 'sozcuk_sayisi']) #csv dosyasının başlıkları

    for number in webpage_list:
        url ="https://shiftdelete.net/p" + str(number)
        i = 0
        article_name = Article(url,language="tr")
        article_name.download()
        article_name.parse()
        article_name.nlp()

        print("url: \n" + article_name.url)

        segmented_text = article_name.text

        segmented_text = re.sub(r"\[\d+\]"," ",segmented_text) #metin temizleme
        segmented_text = re.sub(r"\["," ",segmented_text)
        segmented_text = re.sub(r"\]"," ",segmented_text)
        segmented_text = re.sub(r"\("," ",segmented_text)
        segmented_text = re.sub(r"\)"," ",segmented_text)
        segmented_text = re.sub(r"[:,'\"-]"," ",segmented_text)
        segmented_text = re.sub(r"\s+"," ",segmented_text)
        segmented_text = segmented_text.strip()

        sentences = nltk.sent_tokenize(segmented_text) #sent_tokenize işlemi
        for sentence in sentences:
            i = i+1
            print(str(i) + ".word: " + sentence)
            res = sum([i.strip(string.punctuation).isalpha() for i in sentence.split()])
            print("Word Count: " + str(res))
            word_count += res
            print()

            csv_print.writerow([article_name.url, str(i), sentence, str(res)]) # çıktıları csv dosyasına yazdırır








