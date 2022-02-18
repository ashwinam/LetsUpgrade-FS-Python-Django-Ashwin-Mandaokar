import requests
from bs4 import BeautifulSoup
import pprint

# BeatifulSoup is allows us to use Html & grab different data from html
# requests module is a module that helps to grab that html

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.a)  # it gives first a tag

# BeautifulSoup slector
# print(soup.select('#score_30335314'))  # it is takes css selector

links = soup.select('.titlelink')
links2 = soup2.select('.titlelink')
# votes = soup.select('.score')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
# print(links[0].get('href'))
mega_links = links + links2
mega_subtext = subtext + subtext2
'''
Why we are going for subtext Because every score has subtext , But every Subtext has no score. if the latest news come & if there is no Score then it gives us a error List index out of error.
'''


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'links': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
