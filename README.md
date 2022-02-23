# Dashboard - Data crawling from stackexchange forum
### Getting Started

### Install Julia packages
```
add CSV
add DataFrames
add JSON
```
### Install Python packages
```
pip install Julia
```

### Run from python
```
python test_call.py
```
or include this in your code
```
from julia import Main
Main.include("polytree_events.jl")

Main.event_analysis("nodes.csv", "edges.csv")
```

### Clone the repo
Get a copy of this repo using git clone
```
git clone https://github.com/MatteoBiviano/stackexchange-crawler-webapp.git
```


