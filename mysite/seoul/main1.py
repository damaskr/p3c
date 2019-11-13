import requests
from bs4 import BeautifulSoup as bs


def afterschool(pagenum):

    result = [[],[],[],[]] #Database matrix for Print
    val = [[],[],[],[]]
    refurl = 'http://www.sen.go.kr'
    url = 'http://www.sen.go.kr/web/services/bbs/bbsList.action?bbsBean.bbsCd=119&searchBean.searchKey=&appYn=&searchBean.searchVal=&searchBean.startDt=&startDt=&searchBean.endDt=&endDt=&ctgCd=&sex=&school=&grade=&year=&month=&schoolDiv=&establDiv=&hopearea=&searchBean.deptCd=&searchBean.currentPage='+str(pagenum)
    r = requests.get(url)
    html = r.text
    soup  = bs(html, 'html.parser')
    tr = soup.select('tbody > tr') #<-Tag body
    for i in range(len(tr)): #This code takes School name, Province, Type of employ
        result[0].append(tr[i].select('td')[1].text.strip())
        result[1].append(tr[i].select('td')[2].text.strip())
        result[2].append(tr[i].select('td')[4].text.strip())
    href = soup.select('tbody> tr > td > a') #<-Address Tag
    for i in range(len(href)):  #This code takes address from a href tag
        result[3].append(refurl+href[i].get('href'))

    for i in range(len(result[0])):
        if "방과후" in result[2][i]: #Only print Afterschool
            val[0].append(result[0][i])
            val[1].append(result[1][i])
            val[2].append(result[2][i])
            val[3].append(result[3][i])
    return val

def output():
    string = ''
    for i in range(1,5):
        out = afterschool(10*i+1)
        for j in range(len(out[0])):
            string += '\n' +  str(out[0][j]) + '    ' + str(out[1][j]) + '  ' +str(out[2][j]) + '   '  + str(out[3][j]) + '\n'
    return string

#each pagenum in seoul function will be changed


