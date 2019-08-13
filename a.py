import requests

response = requests.get('http://artii.herokuapp.com/make?text=eunbi&font=acrobatic')
print(response.text)