import json
from github import Github
import time
import pandas as pd
name_code = {
	"C": "c",
	"C#": "c#",
	"F#": "f#",
	"Java": "java",
	"Javascript": "javascript",
	"PHP": "php",  
	"Python": "python"
}


def crawl_github(st):
	st.subheader("Data crawling - Github")
	with st.form(key='my_form'):
		api_key = st.text_input('Insert Github Access token*')
		
		st.markdown("*To obtain an access token see this <a href=https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>documentation</a>", unsafe_allow_html = True)
        
		st.markdown("Select language from list or insert an explicit one")
		language = st.selectbox('Select language', 
                    name_code.keys())

		ins_language = st.text_input('(Optional) Insert language*')

		st.markdown("*See <a href=https://github.com/collections/programming-languages>link</a> for a list of programming languages that are actively developed on GitHub", unsafe_allow_html = True)

		is_clicked = st.form_submit_button('Download')

		if(is_clicked):
			repo_name = []
			repo_owner = []
			repo_language = []
			repo_stargazers_count = []
			repo_forks = []
			if len(api_key) == 0:
				st.error("Insert an access token")
				is_clicked = False
			else:
				g = Github(api_key)
				with st.spinner('Wait for crawling data...'):
					if len(ins_language) > 0:
						language = ins_language                
					repositories = g.search_repositories(query='language:'+str(language))
					it = 0
					for repo in repositories:
						print(f"Iteration: {it}")
						repo_name.append(repo.full_name)
						repo_owner.append(repo.owner.login)
						repo_stargazers_count.append(repo.stargazers_count)
						repo_language.append(repo.language)
						repo_forks.append(repo.forks_count)
						it = it + 1
						if it == 2000: #Max 3k repo for user
							break
						if it%50 == 0: #Max 200 it every 10 secs
							time.sleep(10)

				df = pd.DataFrame({'Name': repo_name, 'Owner': repo_owner, 'Language': repo_language, 'Stars': repo_stargazers_count, 'Forks': repo_forks})
				df.to_csv(f"repositories_{language}.csv", index=False)

				st.success("File Stored")
