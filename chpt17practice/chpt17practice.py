# Chapter 17 practice
# Linhe Sun
# 17: 50 Aug 24 2019 Beijing

# practice 17-1
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call, and store the response.
url = 'https://api.github.com/search/repositories?q=language:R&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.force_uri_protocol = 'http'
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred R Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('R_repos.svg')

# practice 17-2
import requests
import json
from operator import itemgetter

# Make an API call, and store the response.
# actually, in China this website is blocked. 
# YOU NEED A VPN TO RUN THE SCRIPTS BELOW!
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
# write the data down, then i dont need to connect to VPN everytime.
with open('hacker_news_ids.json', 'w') as f_obj:
    json.dump(submission_ids, f_obj)
submission_dicts = []
for submission_id in submission_ids:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
        }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)
# write the data down, then i dont need to connect to VPN everytime.
with open('hacker_news_infos.json', 'w') as f_obj:
    json.dump(submission_dicts, f_obj)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])

plot_dicts = []
for submission_dict in submission_dicts[:50]:
    plot_dict = {
        'value': submission_dict['comments'],
        'label': submission_dict['title'],
        'xlink': submission_dict['link'],
        }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.force_uri_protocol = 'http'
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Comments Articals on Hacker News'
chart.x_labels = submission_ids[:50]

chart.add('', plot_dicts)
chart.render_to_file('articals_hacker_news.svg')

# practice 17-3
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

import unittest

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()
# print("Total repositories:", response_dict['total_count']) 4143054

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
    
    
class TestPythonRepos(unittest.TestCase):
    def test_status_code(self):
        self.assertEqual(r.status_code, 200)
        
    def test_total_count(self):
        # the total_count must be greater than the one in the book
        self.assertGreaterEqual(response_dict['total_count'], 713062)
        
    def test_items_count(self):
        self.assertEqual(len(repo_dicts), 30)
        self.assertEqual(len(names), 30)
        self.assertEqual(len(plot_dicts), 30)
        
unittest.main()
