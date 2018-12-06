#Author: lladhibhutall 
import requests

def my_function(args):

	link =  "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=O45RHWNY6BI3SSGW".format(args)
	r = requests.get(link)
	json_data = r.json()
	return str(json_data) 

