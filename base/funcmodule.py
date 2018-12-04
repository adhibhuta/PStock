#Author: lladhibhutall 


def my_function(args):
	symbol = args.symbol
	link =  "https://www.alphavantage.co/query?function=GLOBAL_QUOTES&symbol={}&apikey=demo".format(symbol)
	return link 

