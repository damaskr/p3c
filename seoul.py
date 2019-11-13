import requests
from bs4 import BeautifulSoup as bs


def seoul(pagenum):

    result = [[],[],[],[],[]]
    refurl = 'http://www.sen.go.kr'
    url = 'http://www.sen.go.kr/web/services/bbs/bbsList.action?bbsBean.bbsCd=119&searchBean.searchKey=&appYn=&searchBean.searchVal=&searchBean.startDt=&startDt=&searchBean.endDt=&endDt=&ctgCd=&sex=&school=&grade=&year=&month=&schoolDiv=&establDiv=&hopearea=&searchBean.deptCd=&searchBean.currentPage='+str(pagenum)
    r = requests.get(url)
    html = r.text
    soup  = bs(html, 'html.parser')
    tr = soup.select('tbody > tr')
    for i in range(len(tr)):
        result[0].append(tr[i].select('td')[1].text.strip())
        result[1].append(tr[i].select('td')[2].text.strip())
        result[2].append(tr[i].select('td')[4].text.strip())
    href = soup.select('tbody> tr > td > a')
    for i in range(len(href)):
        result[3].append(refurl+href[i].get('href'))
    for i in range(len(result[0])):
        if "방과후" in result[2][i]:
            print(result[0][i],result[1][i], result[2][i], result[3][i])

seoul(1)
seoul(11)
seoul(21)
seoul(31)
seoul(41)
seoul(51)
