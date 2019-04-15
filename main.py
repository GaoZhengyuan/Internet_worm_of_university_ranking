import requests
from bs4 import BeautifulSoup

allUniv = []

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        elif ltd[2].string !='河南':
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)

def printUniverlist(num , save):
    if save:
        target = open("./ranking_for_Henan.csv", "w")
        target.write("排名,学校名称,省市,总分,新生高考成绩得分\n")
    print("{1:^2}{2:{0}^10}{3:{0}^5}{4:{0}^7}{5:{0}^8}".
          format(chr(12288),"排名","学校名称","省市","总分","新生高考成绩得分"))
    for i in range(num):
        u = allUniv[i]
        if save:
            target.write("%d,%s,%s,%s,%s\n"%(i+1,u[1],u[2],eval(u[3]),u[4]))
        print("{1:^4}{2:{0}^10}{3:{0}^5}{4:{0}^8.1f}{5:{0}^10}".
              format(chr(12288),i+1,u[1],u[2],eval(u[3]),u[4]))
def main(num,save=False):
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    printUniverlist(num, save)


main(12,save=True)


