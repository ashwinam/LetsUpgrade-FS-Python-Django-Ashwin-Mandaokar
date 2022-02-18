# XPATH (xml path language) x_path is a query language for selecting nodes from an xml documents.
 # _nodes in xml
'''
 				-----html-----
 				|			  |
 		    ----a---- 	  ----p----
 		    |		|	  |		   |
 		    **		**	  **       **
'''
# Lets Begin the project
from lxml import html
import requests

url = "https://en.wikipedia.org/wiki/Outline_of_the_Marvel_Cinematic_Universe"

resp = requests.get(url)
tree = html.fromstring(resp.content)
elements = tree.xpath('//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[*]/th/i/a')

base_url = "https://en.wikipedia.org"
dict_of_names_with_links = {}
for element in range(len(elements)):
	title = elements[element].attrib['title']
	links = base_url + elements[element].attrib['href']
	dict_of_names_with_links[title] = links

tab = '\t'
print()
print(f"MOVIES {tab * 5} |{tab * 3}LINKS")
designing = ("_")
print(designing * 110)
# movies_name = []
for movies,link in dict_of_names_with_links.items():
	# movies_name.append(movies)
	print(movies.ljust(36), "\t |", link) # for clear print i used ljust it create a space 
	# print('_'* 110)

print(designing * 110)

# max_len=len(max(movies_name,key=len))+1 # for calculating the max length for clear printing purpose
# print(max_len)