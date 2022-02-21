import streamlit as st
from data_crawling import *
from network_analysis import *
def main():
	st.sidebar.title("Menu")
	analysis_selbox = st.sidebar.selectbox(
		'',
		["Home", "Data Crawling", "Network Analysis"], index = 0)
	if(analysis_selbox == "Data Crawling"):
		crawl_data(st)
	if(analysis_selbox == "Network Analysis"):
		net_analysis(st)



if __name__ == '__main__':
    main()