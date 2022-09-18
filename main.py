from bs4 import BeautifulSoup
#opening local files
with open('index.html','r') as react_tuts:
    content = react_tuts.read()
    #lxml is a parser
    soup = BeautifulSoup(content,'lxml')
    # find by tags but only gives only first matching tag in case of find
    tag = soup.find('h1')
    # use find all to get all mathing tags and gives a list of tags
    tags = soup.find_all('h1')
    for t in tags:
        print(t.text)
    # get specific div tag with specific class name
    # use class_ to define class as 'class' is a reserved keyword in python
    cards = soup.find_all('div',class_="card")
    # get specific tags inside cards
    for aTag in cards:
        price = aTag.a.text 
        priceVal = price.split()[-1] # splitting the string to get price value
        print(priceVal)
