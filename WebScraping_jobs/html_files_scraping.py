from bs4 import BeautifulSoup

with open('index.html', 'r') as website:

    content = website.read()

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # tags = soup.find_all("td")
    # print(tags)
    # for tag in tags:
    #     print(tag.text)

    elem = soup.find_all('p', class_="zero")
    for e in elem:
        name = e.text
        print(name)







