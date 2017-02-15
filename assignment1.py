import requests

# r = requests.get('http://www.google.com')
#
# print(r.text)

# LAMBDA EMAIL

par = {'name': 'JB', 'lastname': 'Wood', 'email': 'wood.jdesign@gmail.com', 'message': 'Mini coding bootcamp assignemnt 1.2. Hello Lambda, This is JB.'}

r = requests.post('https://lambdaschool.com/contact-form', json=par)

print(r.status_code)
