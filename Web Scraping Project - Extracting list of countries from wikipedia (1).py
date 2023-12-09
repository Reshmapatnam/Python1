#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Web Crawling:The process of collecting the hyperlinks from the websites,URL’s & locating information on world wide web repeatedly & build a list,indexing them and store in a database.Inshort it’s a job of search ingines for information from group of websites
##Web Scrapping:Process of requesting web document & automatically collecting the information from them.Specifically targeted at specific data like stock market data,Business leads information.They obet robot.txt.submits forms,executing java script,transforming data into required form & format,saving the data into the database.


# In[4]:


https://www.amazon.com/robots.txt
#Public content
#Terms of use
#Authentication based websites
#Crawl delay-eg:HIQ Vs. LinkedIn
#Python Libraries required for web scrapping:
1.Requests-Used for fetching URL's---?htps://
2.Beautiful Soup-Used for pulling out information from websites
3.HTML Syntax-<a href='www.intellipaat.com'> Visit to learn more


# In[ ]:


###Web Scrapping Project Using Python###


# In[12]:


#import the library to query a website
import requests
#Specify the URL
wiki_link="https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
link=requests.get(wiki_link).text


# In[14]:


print(link)


# In[13]:


print(link)


# In[17]:


from bs4 import BeautifulSoup
Soup=BeautifulSoup(link,'lxml')
print(Soup)


# In[18]:


print(Soup.prettify())


# In[19]:


Soup.title


# In[20]:


Soup.title.string


# In[21]:


Soup.a


# In[22]:


Soup.find_all("a")


# In[23]:


all_link=Soup.find_all("a")
for link in all_link:
    print(link.get("href"))


# In[24]:


all_tables=Soup.find_all('table')
print(all_tables)


# In[27]:


right_table=Soup.find('table',class_='wikitable sortable')
right_table


# In[29]:


table_links=right_table.findAll('a')
table_links


# In[30]:


country=[]
for links in table_links:
    country.append(links.get('title'))
    print(country)


# In[32]:


import pandas as pd
df=pd.DataFrame()
df['country']=country
df


# In[ ]:





# In[ ]:




