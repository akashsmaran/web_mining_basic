import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import operator
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

def term_freq(list1):
	freqt = dict()
	for word in list1:
		if word in freqt:
			freqt[word] += 1
		else:
			freqt[word] = 1
	return freqt

paragraph = input("Enter the paragraph \n")
para = ""
for i in paragraph:
    if not i in '.,!?():':
        para += i
print(para+ "\n \n \n")
stop = set(stopwords.words('english'))
listop = [i for i in para.lower().split() if i not in stop]
print(listop)
print("\n")
ps = nltk.stem.PorterStemmer()
listopandstem = [ps.stem(i) for i in listop]
print(listopandstem)
print("\n \n")
fdist =  FreqDist(listopandstem)
#print(fdist)
vowel = [word for word in listop if word[0] in 'aeiou']
m = term_freq(vowel)
print(m)
print("\n")
x = input("Enter search word")
print(m[x], x)
li_term = m.keys()
li_freq = m.values()

df = pd.DataFrame({'li_freq':li_freq,
                   'li_term':li_term})
 
writer = ExcelWriter('abc.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()