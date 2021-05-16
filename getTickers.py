import urllib.request, json
from jinja2 import Environment, FileSystemLoader

tickers = ''

# Fetch all the tickers from CoinGecko and append to add to tickers string
for i in range(1, 11):
	api = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page={i}&sparkline=false"

	with urllib.request.urlopen(api) as url:
		data = json.loads(url.read().decode())
		for crypto in data:
			tickers += "'" + crypto['symbol'].upper() + "'" + ','

# Get the data template from "data.jinja2" and render the tickers on there 
file_loader = FileSystemLoader("./")
env = Environment(loader=file_loader)
template = env.get_template("data.jinja2")
output = template.render(tickers=tickers)

# Dump the jinja template to "data.py"
with open("data.py", "w") as fh:
	fh.write(output)