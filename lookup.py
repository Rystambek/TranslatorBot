import requests
from pprint import pprint

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"


headers = {
	"X-RapidAPI-Key": "8ffab1e567msh9d3c11650e43ad1p122ee2jsn0db792092f5f",
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
}

def query(work):
	querystring = {"term":work}
	response = requests.request("GET", url, headers=headers, params=querystring)
	res = response.json()

	if len(res['list']) == 0:
		return False
	
	output = {}
	lists = res['list']
	definition = []
	for list in lists:
		definition.append(f"{list['definition']}")
	output['definitions'] = '\n➡️'.join(definition)

	return output
if __name__ == '__main__':
	print(query('Uzbekistan'))