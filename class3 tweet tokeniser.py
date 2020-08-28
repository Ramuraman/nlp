#!/usr/bin/env python
# coding: utf-8

# In[3]:


import nltk
text1='''A paragraph is a series of related sentences developing a central idea, called the topic. Try to think about paragraphs in terms of thematic unity: a paragraph is a sentence or a group of sentences that supports one central, unified idea. Paragraphs add one idea at a time to your broader argument.'''
for text in text1:
    sentences=nltk.sent_tokenize(text1)
    for word in sentences:
        nltk.word_tokenize(sentences)
        tagged=nltk.pos_tag(words)
        print(tagged)


# In[5]:


from nltk.tokenize import TweetTokenizer
text='My Administration has been focused on finding treatments for Coronavirus. If you’ve recovered from Coronavirus, donate your plasma today to help SAVE LIVES! Together, we will beat the Virus!'
twtkn=TweetTokenizer()
twtkn.tokenize(text)


# In[6]:


from urllib import request
url="http://www.guttenburg.org/filess/2554/2554-0.txt"
response=request.urlopen(url)
raw=response.read().decode('utf-8')
print(type(raw))
print(len(raw))
raw[:75]
from nltk.tokenize import word_tokenize
tokens=word_tokenize(raw)
type(tokens)


# In[ ]:




