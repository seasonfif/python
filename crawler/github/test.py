import bs4
import json

def parse_repo_name(tag):
	repo_name = {}
	repo_name["href"] = tag.find("a")["href"]
	return repo_name

def parse_repo_description(tag):
	repo_des = {}
	repo_des["des"] = tag.text.strip()
	return repo_des

html="""
<ol class="repo-list">
	<li class="col-12 d-block width-full py-4 border-bottom" id="pa-abapGit">
		<div class="d-inline-block col-9 mb-1">
			<h3>
				<a href="/larshp/abapGit">
					<span class="text-normal">larshp / </span>abapGit </a>
			</h3>
		</div>

		<div class="py-1">
			<p class="col-9 d-inline-block text-gray m-0 pr-4">
				Git client for ABAP
			</p>
		</div>

		<div class="f6 text-gray mt-2">
			<span class="d-inline-block mr-3">
				<span class="repo-language-color ml-0" style="background-color:#E8274B;"></span>
				<span itemprop="programmingLanguage">
					ABAP
				</span>
			</span>

			<a class="muted-link d-inline-block mr-3" href="/larshp/abapGit/stargazers">
				<svg aria-label="star" class="octicon octicon-star" height="16" role="img" version="1.1" viewBox="0 0 14 16" width="14">
					<path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"></path>
				</svg>
				292
			</a>

			<a class="muted-link d-inline-block mr-3" href="/larshp/abapGit/network">
				<svg aria-label="fork" class="octicon octicon-repo-forked" height="16" role="img" version="1.1" viewBox="0 0 10 16" width="10">
					<path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path>
				</svg>
				102
			</a>

		</div>
	</li>

	<li class="col-12 d-block width-full py-4 border-bottom" id="pa-Tennis-Refactoring-Kata">
		<div class="d-inline-block col-9 mb-1">
			<h3>
				<a href="/emilybache/Tennis-Refactoring-Kata">
					<span class="text-normal">emilybache / </span>Tennis-Refactoring-Kata
				</a>
			</h3>
		</div>

		<div class="py-1">
			<p class="col-9 d-inline-block text-gray m-0 pr-4">
				Starting code for a Refactoring Code Kata on the Tennis rules
			</p>
		</div>

		<div class="f6 text-gray mt-2">
			<span class="d-inline-block mr-3">
				<span class="repo-language-color ml-0" style="background-color:#E8274B;"></span>
				<span itemprop="programmingLanguage">
					ABAP
				</span>
			</span>

			<a class="muted-link d-inline-block mr-3" href="/emilybache/Tennis-Refactoring-Kata/stargazers">
				<svg aria-label="star" class="octicon octicon-star" height="16" role="img" version="1.1" viewBox="0 0 14 16" width="14">
					<path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"></path>
				</svg>
				163
			</a>

			<a class="muted-link d-inline-block mr-3" href="/emilybache/Tennis-Refactoring-Kata/network">
				<svg aria-label="fork" class="octicon octicon-repo-forked" height="16" role="img" version="1.1" viewBox="0 0 10 16" width="10">
					<path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path>
				</svg>
				306
			</a>

		</div>
	</li>

</ol>
"""

soup = bs4.BeautifulSoup(html,'html.parser')
#repo_list = soup.find('ol',{"class":"repo-list"})
repo_items = soup.findAll('li',{"class":"col-12 d-block width-full py-4 border-bottom"})
#print repo_items

parsed_items = []

for repo_item in repo_items:
	parsed_item = {}
	for tag in repo_item:
		# print type(tag)
		if type(tag) is bs4.element.Tag and "class" in tag.attrs:
			# print tag["class"][0]
			if tag["class"][0] == "d-inline-block":
				# print parse_repo_name(tag)
				parsed_repo_name = parse_repo_name(tag)
				parsed_item.update(parsed_repo_name)
			if tag["class"][0] == "py-1":
				# print parse_repo_description(tag)
				parsed_repo_des = parse_repo_description(tag)
				parsed_item.update(parsed_repo_des)
	print parsed_item
	parsed_items.append(parsed_item)