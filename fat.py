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


paragraph = "Life is beautiful, but not always. It has lots of problems you have to face every day. Dont worry though!All these problems make you strong, it gives you courage to stand alone in future. Life is full ofmoments of joy, pleasure, success and comfort punctuated by misery, defeat, failures and problems.There is no human being on Earth, strong, powerful, wise or rich, who has not experienced, struggle,suffering or failure. You have to work hard to reach to the highest position. Life is full of paths, youjust have to choose the right one. Life is interesting and amazing like the stars up in the skies.With no doubt, Life is beautiful and full of celebrations. However you should always be ready to faceadversity and challenges. There are difficult situations in life as well. Be careful!! You might get hurttoo hard. Life is sometimes too selfish to think about yourself. Then life is too hard to handle. Fallingin love! People tend to fall in love nowadays but i personally think the right time has to come... Youmight also get hurt in Love. You might be broken-hearted as the people say."
stop = set(stopwords.words('english'))
listop = [i for i in paragraph.lower().split() if i not in stop]
m = term_freq(listop)
vowel = [word for word in listop if word[0] in 'ase']
vowel_freq = term_freq(vowel)
vowel1 = [word for word in listop if word[0] in 'aeiou']
print("Stopwords removed:")
print(listop)
print("\n")
print("term freq:")
print(m)
print("\n")
print("Number of words starting with ase and maximum frequency word:")
print(len(vowel))
print(max(vowel_freq))
print(vowel1)