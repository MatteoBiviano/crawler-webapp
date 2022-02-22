import streamlit as st
from data_crawling import *
def main():
	st.sidebar.title("Menu")
	analysis_selbox = st.sidebar.selectbox(
		'',
		["Data Crawling"], index = 0)
	if(analysis_selbox == "Data Crawling"):
		crawl_data(st)


if __name__ == '__main__':
    main()
