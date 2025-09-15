import requests
"""
from pydoc import importfile
module = importfile('..\\config.py')
from config import RAPID_API_KEY
"""
# Defining constants
API_HOST = "flixster.p.rapidapi.com"
POPULAR_MOVIES_URL = "https://flixster.p.rapidapi.com/movies/get-popularity"
MOVIE_DETAIL_URL = "https://flixster.p.rapidapi.com/movies/detail"


querystring = {"zipCode":"90002","radius":"50"}
querystring = {"emsVersionId":"0e2459f2-51d8-30f3-9114-4b0e7d3946dc"}

headers = {
	"x-rapidapi-key": "2b2e34e86amsh082488a7dfd21eap11a229jsn4ca63b8b9825",
	"x-rapidapi-host": "flixster.p.rapidapi.com"
}

response_popular = requests.get(POPULAR_MOVIES_URL, headers=headers, params=querystring)
querystring = {"emsVersionId":"0b990002-9ffe-3706-919e-da57869defc0"}
response_details = requests.get(MOVIE_DETAIL_URL, headers=headers, params=querystring)
#print(response_popular.json())
data_popular = response_popular.json()
data_popular['data']['popularity']
for movie in data_popular['data']['popularity']:
    movie_id = movie['emsId']
    movie_ver_id = movie['emsVersionId']
    movie_title = movie['name']
    try:
        movie_rating = movie['userRating']['dtlLikedScore']
    except:
        movie_rating='None'
    print(movie_id)
    print(movie_ver_id)
    print(movie_title)
    print(movie_rating)
    print("\n")
data_details =response_details.json()
print(data_details['data']['movie']['name'])
print(data_details['data']['movie']['durationMinutes'])
print(data_details['data']['movie']['releaseDate'])
print(data_details['data']['movie']['totalGross'])
print(data_details['data']['movie']['directedBy'])
print(data_details['data']['movie']['synopsis'])
print(data_details['data']['movie']['genres'][0]['name'])

