#!/usr/bin/env python
#
# https://docs.github.com/en/rest/reference/users#followers
#
import os
import sys
import random
import requests
themes = ["default", "default_repocard", "dark", "radical", "merko", "gruvbox", "gruvbox_light", "tokyonight", "onedark", "cobalt", "synthwave", "highcontrast", "dracula", "prussian", "monokai", "vue", "vue-dark", "shades-of-purple", "nightowl", "buefy", "blue-green", "algolia", "great-gatsby", "darcula", "bear", "solarized-dark", "solarized-light", "chartreuse-dark", "nord", "gotham", "material-palenight", "graywhite", "vision-friendly-dark", "ayu-mirage", "midnight-purple", "calm", "flag-india", "omni", "react", "jolly", "maroongold", "yeblu", "blueberry", "slateorange", "kacho_ga", "outrun", "ocean_dark", "city_lights", "github_dark", "discord_old_blurple", "aura_dark", "panda", "noctis_minimus", "cobalt2", "swift", "aura", "apprentice", "moltack"]

def github_stats(name, width):
	include_all_commits = 'false'
	hide_rank = 'false'
	theme = random.choice(themes)
	stats = '<a href="https://github.com/' + name + '">' + \
		'<img src="https://github-readme-stats.vercel.app/api?username=' + name + \
		'&count_private=true&show_icons=true' + \
		'&include_all_commits=' + include_all_commits + \
		'&hide_rank=' + hide_rank + \
		'&theme=' + theme +'"  width=' + str(width) + '% /></a>'
	print(stats)

def github_users(user, isIdol, api_token = None):
	page = 1
	username_list = []
	while True:
		if isIdol:
			url = 'https://api.github.com/users/' + user +'/followers?page=' + str(page)
		else:
			url = 'https://api.github.com/users/' + user +'/following?page=' + str(page)
		if api_token == None:
			headers = {"Accept": "application/vnd.github.v3+json"}
		else:
			headers = {"Authorization": "token " + api_token, "Accept": "application/vnd.github.v3+json"}
		page += 1
		response = requests.get(url, headers=headers)
		idols = response.json()
		#print(idols)
		if type(idols) != list:
		# Prevent exception
		# {'message': "API rate limit exceeded for xx.xx.xx.xx
			print()
			print(page-1)
			break
		for idol in idols:
			username_list.append(idol['login'])
		print(page-1, username_list[-30:])
		if len(idols) < 30 or len(username_list) >= 300:
			break

	username_list = sorted(username_list)
	print(username_list)
	original_stdout = sys.stdout
	with open('README.md', 'w') as f:
		sys.stdout = f
		print('<div align="center">')
		github_stats(user, 60)
		print('</div>')

		print("It isn't 10,000 hours that creates outliers, it's 10,000 iterations.")
		print('<p align="right">― Naval</p>')
		if isIdol:
			print('<h3>I am followed by:</h3>')
		else:
			print('<h3>I am following:</h3>')
		print('<div align="center">')
		for name in username_list:
			github_stats(name, 46)
		print('</div>')
		sys.stdout = original_stdout

def main():
	user = 'evmn'
	isIdol= False
	api_token = None
	github_users(user, isIdol, api_token)
if __name__ == "__main__":
	main()
