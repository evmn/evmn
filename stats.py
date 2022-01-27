#!/usr/bin/env python
import os
import sys
import random
import requests
name = "evmn"
url = 'https://api.github.com/users/' + name +'/following'
header = {"Accept": "application/vnd.github.v3+json"}
themes = ["default", "default_repocard", "dark", "radical", "merko", "gruvbox", "gruvbox_light", "tokyonight", "onedark", "cobalt", "synthwave", "highcontrast", "dracula", "prussian", "monokai", "vue", "vue-dark", "shades-of-purple", "nightowl", "buefy", "blue-green", "algolia", "great-gatsby", "darcula", "bear", "solarized-dark", "solarized-light", "chartreuse-dark", "nord", "gotham", "material-palenight", "graywhite", "vision-friendly-dark", "ayu-mirage", "midnight-purple", "calm", "flag-india", "omni", "react", "jolly", "maroongold", "yeblu", "blueberry", "slateorange", "kacho_ga", "outrun", "ocean_dark", "city_lights", "github_dark", "discord_old_blurple", "aura_dark", "panda", "noctis_minimus", "cobalt2", "swift", "aura", "apprentice", "moltack"]
resp = requests.get(url, header)
following = resp.json()
original_stdout = sys.stdout

with open('README.md', 'w') as f:
	sys.stdout = f
	theme = random.choice(themes)
	print('<div align="center">')
	stats = '<img src="https://github-readme-stats.vercel.app/api?username=' + name + \
		'&count_private=true&show_icons=true&include_all_commits=true&theme=' + theme +'" width=50% />'
	print(stats)
	print('</div>')

	print("It isn't 10,000 hours that creates outliers, it's 10,000 iterations.")
	print('<p align="right">― Naval</p>')
	print('<h1>I am following:</h1>')
	print('<div align="center">')
	for mentor in following:
		name = mentor['login']
		theme = random.choice(themes)
		stats = '<img src="https://github-readme-stats.vercel.app/api?username=' + name + \
			'&count_private=true&show_icons=true&include_all_commits=true&theme=' + theme +'"  width=32% />'
		print(stats)
	print('</div>')
	sys.stdout = original_stdout
