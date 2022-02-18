# issues:
# 1)it takes times to get the data so thats need to use multithreading.

from lxml import html
import requests

url = "https://www.imdb.com/name/nm0000375/?ref_=nv_sr_1?ref_=nv_sr_1"

resp = requests.get(url).text
tree = html.fromstring(resp)

titles = tree.xpath('//*[@class="filmo-row even"]//b//text()')


dict_of_movie_names_and_links = {}

base_url = "https://www.imdb.com/"
for title in titles:
	movie_url = tree.xpath(f'//a[text()="{title}"]/@href')
	movie_url = list(set(movie_url))
	link = base_url + movie_url[0]
	dict_of_movie_names_and_links[title] = link

# print(dict_of_movie_names_and_links)

def get_rating(t1):
	name, url = t1
	data = requests.get(url).text
	tree = html.fromstring(data)
	rating = tree.xpath("//span[@class='AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV']//text()")
	return (name,url,rating) 

new_dict_of_all_information = {}
for each in dict_of_movie_names_and_links.items():
	title,movieUrl,ratings=get_rating(each)
	new_dict_of_all_information[title] = [movieUrl,ratings]

print(new_dict_of_all_information)

# for name,url,rating in new_dict_of_all_information.items():
# 	print(name,url,rating)