import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'longitude':122, 'latitude':37.7, 'housing_median_age':50 , 'total_rooms':200 , 'total_bedrooms':400 , 'population':500 , 'households':600 , 'median_income':10  })

print(r.json())
