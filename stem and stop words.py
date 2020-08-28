#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
nltk.download()


# In[7]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
port=PorterStemmer()
example_sentence="My name is Rama Raman. I am 19 years old. i like ice creams and chocolates."
words=word_tokenize(example_sentence)
stop_words=set(stopwords.words("english"))
filtered_sentence= [w for w in words if not w in stop_words]
print (filtered_sentence)
for x in words:
    print(port.stem(x))


# In[ ]:




