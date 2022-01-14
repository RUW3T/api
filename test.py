import requests
from rich.console import Console
from bs4 import BeautifulSoup
from pprint import pprint
import json

# w = input("what want to find >>> ")

# if len(w) == "7": 
#     print("error") 

w = input(">>> ")
r = requests.get(f'https://api.stackexchange.com/2.3/search?order=desc&sort=activity&intitle={w}&site=stackoverflow')
# response = json.loads(r.text)

# ru = int(input("Num num >> "))
res = r.json().get('items')[1] 

#[ru]#.get("title")

title = res.get('title')
link = res.get('link')

console = Console()
# console.print(res, style="yellow")
console.print(f'title = `{title}`', style="yellow")
console.print(f'link = {link}', style="green")

x = requests.get(str(link)).text
soup = BeautifulSoup(x, 'html.parser')

y = soup.select('#answers') #code find,select,select_one

z = y[0].select('code')

for code in z[0].find_all('code', attrs={'class':'hljs'}):
    cod = code.find('code')

# dat = soup.find_all("code", class_="hljs")

# TODO: Terget Cepet GOBLOK🤔🤔🤔🤔🤔🤔🤔🤔🤔
# <code>struct Pokemon: Codable, Identifiable { 
#     var id = UUID()
#     var name: String
#     var url: String

#     enum CodingKeys: String, CodingKey {
#         case name, url
#     }
# }
# </code>


# u = z[0].select('hljs')


# # questions = soup.select('.question-summary')

# # d = questions[0].select('.question-hyperlink')

# # print(d)

# buat nyari href 🤔
# for code in y.find_all('code', attrs={'class':'hljs'}):
#     # url = str(div.find('a')['href'])

#     dat = str(code.find(''))


pprint(cod)

# title = res.get('title')
# link = res.get('link')

# console = Console()
# # console.print(res, style="yellow")
# console.print(f'title = `{title}`', style="yellow")
# console.print(f'link = {link}', style="green")