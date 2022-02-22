from stackapi import StackAPI
from datetime import datetime
import calendar
import json
import os

name_code = {
	"Anime & Manga": "anime",
	"Arqade": "gaming",
	"Ask Different": "apple",
	"Ask Ubuntu": "askubuntu",
	"Bicycles": "bicycles",
	"Biology": "biology",  
	"Blender": "blender",
	"English Language": "english",
	"Home Improvement":"diy",
	"Latex": "tex",
	"Mathematics": "math",
	"Movies & TV":"movies",
	"Music: Practice & Theory":"music", 
	"Seasoned Advice":"cooking",
	"Server Fault":"serverfault",
	"SharePoint": "sharepoint",
	"StackOverflow": "stackoverflow",
	"Super User": "superuser",
	"Travel":"travel",
	"WorldBuilding":"worldbuilding"
}




def crawl_data(st):
	st.subheader("Data crawling")
	with st.form(key='my_form'):
		api_key = st.text_input('Insert stackexchange API key*')
		
		st.markdown("*To obtain an api key you have to register an app on <a href=https://stackapps.com/apps/oauth/register>registration link</a>", unsafe_allow_html = True)

		forum = st.selectbox('Select forum', 
									name_code.keys())
		n_record = st.slider('Select number of records to crawl', min_value=1000, max_value=50000, step = 1000)
		st.subheader("Select date range")
		date_start = st.date_input('Start date')
		date_end = st.date_input('End date')

		type_data = st.selectbox('Select what type of data', ["answers", "badges", "collectives", "comments", "posts", "questions", "tags"])

		is_sorted = st.radio("Which type of sorting?", ["votes", "activity", "added"])
		
		filters = st.text_input("(Optional) Insert filter for data you want to crawl*")
		
		st.markdown("*Create filter searching data type on <a href=https://api.stackexchange.com/docs/>api link</a> then edit the filter field", unsafe_allow_html = True)

		is_clicked = st.form_submit_button('Download')

		if(is_clicked):
			if len(api_key) == 0:
				st.error("Insert an api key")
				is_clicked = False
			else:
				with st.spinner('Wait for crawling data...'):
					SITE = StackAPI(name_code[forum],   key = api_key , impose_throttling = True)
					SITE.page_size = 100
					SITE.max_pages = n_record/100
					if len(filters)>0:
						data = SITE.fetch(type_data, filter = filters, fromdate =  calendar.timegm(date_start.timetuple()), todate = calendar.timegm(date_end.timetuple()), sort = is_sorted)			
					else:
						data = SITE.fetch(type_data, fromdate =  calendar.timegm(date_start.timetuple()), todate = calendar.timegm(date_end.timetuple()), sort = is_sorted)
				with open(f"data_{name_code[forum]}_{type_data}.json", "w") as jsonF:
					json.dump(data, jsonF)
					st.success("File Stored")
