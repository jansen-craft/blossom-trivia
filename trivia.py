import requests
category_options = ["general_knowledge","sport_and_leisure", "society_and_culture","science","music","history","geography","food_and_drink","film_and_tv","arts_and_literature"]
difficulty_options = ["easy", "medium", "hard"]
limit_max = 20

params = {
	"categories": ["General Knowledge"],
	"difficulty": difficulty_options[1],
	"limit": 1,
	"region": "US"
}

url = "https://the-trivia-api.com/api/questions?"
if len(params["categories"]) != 0:
	url += "categories=" + "{},".format(i for i in params["categories"]) + "&"
if params["difficulty"]:
	url += "difficulty={}&".format(params["difficulty"])
if params["limit"] <= 20 and params["limit"] > 0:
	url += "limit={}&".format(params["limit"])
if params["region"]:
	url += "region={}&".format(params["region"])
	
res = requests.get(url)

print("Trivia Time!")
print(res.json())

# https://the-trivia-api.com/api/questions
