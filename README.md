# TheGraph Network Dashboard

![Overview of Allocations of Indexers on Subgraphs](https://raw.githubusercontent.com/anyblockanalytics/thegraph-curator-phase3/main/images/allocation_1.jpg)

## Overview 
This is a WIP dashboard displaying metrics and stats from TheGraph. Built with Python and Streamlit.
Using GraphQL to query the TestNet Subgraph of the Graph. It contains informations on:

* Overview of Network Stats
* Subgraphs (List of Subgraphs with Descriptions, Rewards, Signals and More)
* Curators (List of Curators, ...)
* Indexer (List of Indexer, Allocations, Indexing Rewards, Plots)


## Running the Dashboard

First it is necessary to install the required paackages, such as pandas, streamlit...

```python
pip install streamlit, pandas, plotly

```