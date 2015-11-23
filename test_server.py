import requests as rq

input = '{"teamID": "1234-BCda-CDF-1", "playerID":"1234aBA", "time": "2015-5-1T12:15:06Z", "message": "what are you"}'

res=rq.post('http://127.0.0.1:5000/',data=input)
