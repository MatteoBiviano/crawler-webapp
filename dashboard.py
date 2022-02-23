import streamlit as st
from PIL import Image
from crawling_stackexchange import *
from crawling_arxivorg import *
from crawling_github import *


# Set background
def set_background(is_set, text = None):
	if is_set:
		if text:
			header_html = f"""
				<div style="background-color:#145796;padding:10px;border-radius:10px">
				<h1 style="color:white;text-align:center;">{text}</h1>
				</div>
			"""
			st.components.v1.html(header_html)

		image = Image.open('images/background.png')
		st.image(image)


def main():
    st.sidebar.title("Menu")
    crawled_method = st.sidebar.selectbox(
        '',
        ["Home", "StackExchange", "ArXiv.Org", "Github"], index = 0)
    if(crawled_method == "StackExchange"):
        crawl_stackexchange(st)
    elif(crawled_method == "ArXiv.Org"):
        crawl_arxivorg(st)
    elif(crawled_method == "Github"):
        crawl_github(st)
    else:
        set_background(True, "Welcome to Data Crawler")

if __name__ == '__main__':
    main()