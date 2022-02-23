import urllib.request as libreq
import time
import feedparser
import json
name_code = {
    "Astrophysics": "cat:astro-ph",
	"Condensed Matter": "cat:cond-mat",
	"General Relativity and Quantum Cosmology": "cat:gr-qc",
	"Mathematical Physics": "cat:math-ph",
	"Nuclear Theory":"cat:nucl-th",
	"Quantitative Biology":"cat:q-bio",
	"Quantitative Finance":"cat:q-fin", 
	"Quantum Physics": "cat:quant-ph",

}
#sortBy can be "relevance", "lastUpdatedDate", "submittedDate"

#sortOrder can be either "ascending" or "descending"


# Base api query url
base_url = 'http://export.arxiv.org/api/query?'
#cat
#all
def crawl_arxivorg(st):
    st.subheader("Data crawling - ArXiv.Org")
    with st.form(key='my_form'):
        st.markdown("Select category from list or insert an explicit one")
        category = st.selectbox('Select category', 
                    name_code.keys())

        ins_category = st.text_input('(Optional) Insert category*')

        st.markdown("*See <a href=https://arxiv.org/category_taxonomy>arxiv link</a> for complete list of category that can be use, like: math.AC, econ.EM, cs.SD", unsafe_allow_html = True)


        n_record = st.slider('Select number of records to crawl', min_value=1000, max_value=30000, step = 1000)

        sorting_method = st.selectbox('Select sorting method', ["relevance","lastUpdatedDate","submittedDate"])

        sorting_type = st.selectbox('Select how to sort', ["ascending","descending"])


        is_clicked = st.form_submit_button('Download')

        if(is_clicked):
            list_dict = []
            with st.spinner('Wait for crawling data...'):
                if len(ins_category) > 0:
                    category = "cat:"+ins_category                
                for i in range(0, n_record, 1000):
                    query = 'search_query=%s&sortBy=%s&sortOrder=%s&start=%i&max_results=%i' % (category,
                                                                    sorting_method,
                                                                    sorting_type,
                                                                    i,
                                                                    i+1000)
                    #feedparser._FeedParserMixin.namespaces['http://a9.com/-/spec/opensearch/1.1/'] = 'opensearch'
                    #feedparser._FeedParserMixin.namespaces['http://arxiv.org/schemas/atom'] = 'arxiv'
                    response = libreq.urlopen(base_url+query).read()
                    feed = feedparser.parse(response)
                    
                    for entry in feed.entries:

                        title = entry.title
                        author_string = entry.author
                        try:
                            authors =[]
                            for author in entry.authors:
                                authors.append(author.name)
                        except AttributeError:
                            pass

                        primary = entry.tags[0]['term']

                        
                        all_categories = [t['term'] for t in entry.tags]
                        categories = []
                        for category in all_categories:
                            categories.append(category)

                        dictionary = {"Scrapy_key_id": category[4:],"Title": title, "Last_Author": author_string, "Authors": authors, "Primary_Category":primary, "Categories":categories}
                        
                        list_dict.append(dictionary)
                    time.sleep(10)
                
            json_object = json.dumps(list_dict, indent = 4, ensure_ascii=False) 
            with open("data_"+ category[4:] + ".json", "w", encoding='utf-8') as outfile: 
                outfile.write(json_object)
            st.success("File Stored")
