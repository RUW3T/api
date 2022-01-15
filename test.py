import requests
from rich.console import Console
from bs4 import BeautifulSoup
from pprint import pprint
import json


try: 
    w = input(">>> ")
    r = requests.get(f'https://api.stackexchange.com/2.3/search?order=desc&sort=activity&intitle={w}&site=stackoverflow')
    # response = json.loads(r.text)

    ru = int(input("Num num >> "))
    res = r.json().get('items')[ru]#.get("title")

    title = res.get('title')
    link = res.get('link')

    console = Console()
    # console.print(res, style="yellow")
    console.print(f'title = `{title}`', style="yellow")
    console.print(f'link = {link}', style="green")

    x = requests.get(str(link)).text #semisal revisi dari sini🤔🤔
    soup = BeautifulSoup(x, 'html.parser')

    y = soup.select('#answers') #jawaban hungkul🤔

    z = y[0].select('pre')

    # cod = z[0].select('.s-code-block') How to fetch created and updated status of JIRA ticket with Python API
    # How to fetch data from google book api using python 🤔🤔🤔🤔

    # with open('json_data.json', 'w') as outfile:
    #     outfile.write(json_string)

    pprint(z)

    # with open('data.html', 'w') as result:
    #     result.write(z)

except:
    print("\n>> Not Found🤔🤔🤔🤔 <<")

    # except error:
    #     print("Not Found")



# for code in z[0].find_all('pre', attrs={'class':'s-code-block'}):
#     cod = code.find('hljs')


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




# title = res.get('title')
# link = res.get('link')

# console = Console()
# # console.print(res, style="yellow")
# console.print(f'title = `{title}`', style="yellow")
# console.print(f'link = {link}', style="green")