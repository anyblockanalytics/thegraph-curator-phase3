import requests
import os
import json
import pandas as pd
#from gql import gql, Client
#from gql.transport.aiohttp import AIOHTTPTransport

def getGraphQuery(subgraph_url, query, variables=None):

    # use requests to get query results from POST Request and dump it into dat
    """
    :param subgraph_url: 'https://api.thegraph.com/subgraphs/name/ppunky/hegic-v888'
    :param query: '{options(where: {status:"ACTIVE"}) {id symbol}}'
    :param variables:
    :return:
    """
    request_json = {'query': query}
    if variables:
        request_json['variables'] = variables
    resp = requests.post(subgraph_url, json=request_json)
    data = json.loads(resp.text)
    data = data['data']
    
    return data

"""
def getGraphQuery_gql(subgraph_url,query,variables=None):
    transport = AIOHTTPTransport(url=subgraph_url)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    query = gql(query)
    result = client.execute(query)
    return result 
"""