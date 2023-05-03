#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This program collects the weblinks from the website census.gov, 
# gets rid of the duplicate weblinks, 
# and puts them in an excel file for easy viewing.


# In[ ]:


from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re


# In[ ]:


# Opens the website and creates a parse tree.
website = urllib.request.urlopen('https://www.census.gov/programs-surveys/popest.html').read()
soup = BeautifulSoup(website, "lxml")


# In[ ]:


# Creates list variables for the absolute links and relative links within the webpage.
links = list()
rel_links = list()


# In[ ]:


# Looks through and finds all of the absolute hyperlinks and adds them to the list variable.
for link in soup.findAll('a', attrs = {'href': re.compile("^http")}):
    links.append(link.get('href'))


# In[ ]:


# Looks through and finds all of the relative hyperlinks and adds them to the list variable.
for link in soup.findAll('a', attrs = {'href': re.compile("^/")}):
    rel_links.append('https://www.census.gov' + link.get('href'))


# In[ ]:


# Combines the absolute and relative links into a single list.
links += rel_links


# In[ ]:


# Changes the list into a set and back into a list to get rid of duplicate strings.
links = list(set(links))


# In[ ]:


# Puts each hyperlink on its own line. 
Linkswspace="\n".join(links)


# In[ ]:


# Creates the excel file and closes it. 
Excelfile = open('Links.csv','w')
Excelfile.write(Linkswspace)
Excelfile.close()

