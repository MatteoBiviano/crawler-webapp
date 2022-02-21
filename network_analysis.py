

def net_analysis(st):
	st.subheader("Upload csv for edge list")
	uploaded_file = st.file_uploader("Choose a file")
	if uploaded_file is not None:
		G = nx.read_edgelist(path, comments = "S", delimiter = ",", data=(("Count", int),))