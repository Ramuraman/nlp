#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.corpus import stopwords
stopwords.words('english')


# In[8]:


import nltk
entries=nltk.corpus.cmudict.entries()
len(entries)
for i in entries:
    print(i)


# In[3]:


from nltk.corpus import wordnet as wn
wn.synsets('desktop')


# In[4]:


wn.synset('desktop.n.01').lemma_names()


# In[5]:


wn.synset('background.n.07').lemma_names()


# In[11]:


import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
print(stemmerporter.stem('happiness'))
from nltk.stem import LancasterStemmer
stemmerlanc=LancasterStemmer()
print(stemmerlanc.stem('happiness'))


# In[13]:


from nltk.stem import SnowballStemmer
SnowballStemmer.languages
spanishstemmer=SnowballStemmer('spanish')
spanishstemmer.stem('hablo')


# In[15]:


stemmer=PorterStemmer()
example="a quick brown fox jumps over a lazy dog"
example=[stemmer.stem(token) for token in example.split(" ")]
print(" ".join(example))


# In[19]:


from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("plurals"))
print(lemmatizer.lemmatize("futuristic"))
print(lemmatizer.lemmatize("better",pos='a'))


# In[20]:


import jieba
seg=jieba.cut("我很聪明",cut_all= True)
print(" ".join(seg))


# In[ ]:




