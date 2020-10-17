import bs4
import requests
import clearbit
clearbit.key = 'sk_da14e16c2943eee59eddf40a42983144'

info_data={'name':'ayo', 'email':'hjpohncapper@live.com'}

# GET https://person.clearbit.com/v2/people/find?email=:email
res = requests.get('https://person.clearbit.com/v2/combined/find?email=:' + info_data['email'])
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')



# print(soup.text.strip())
