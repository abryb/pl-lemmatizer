## Server
### running with docker
```shell script
docker run -it -p 5000:5000 abryb/pl-lemmatizer
```

## Client
#### curl
```shell script
curl --request POST \
  --url http://localhost:5000/lemmatize \
  --header 'content-type: application/json' \
  --data '{
	"texts": [
		"Żółtą piłką bramkę strzelił."
	]
}'
```

#### python
```python
import requests
import json

res = requests.post(
    'http://localhost:5000/lemmatize',
     data=json.dumps({'texts': ['Żółtą piłką bramkę strzelił.']})
)
print(res.json())
```