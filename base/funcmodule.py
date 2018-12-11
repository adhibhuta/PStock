#Author: lladhibhutall 
import requests
import json
import pprint

def my_function(args):

	link =  "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&outputsize=full&apikey=O45RHWNY6BI3SSGW".format(args)
	r = requests.get(link)
	json_data = r.json()
	return (convert_json_to_dict(json_data))
	#return isinstance(json_data,dict) 

def convert_json_to_dict(_json):
	stock_data = _json['Time Series (5min)']
	#s_data = {}
	list_of_dict_data = []
	for key,value in stock_data.items():	
		s_data = {}
		s_data['Timestamp'] = key 
		s_data['Position'] = value['1. open']
		list_of_dict_data.append(s_data)	
	return list_of_dict_data
