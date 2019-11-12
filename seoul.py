import requests
from bs4 import BeautifulSoup as bs


def fuck(pagenum):

    result = [[],[],[],[]]

    url = 'http://www.sen.go.kr/web/services/bbs/bbsList.action?bbsBean.bbsCd=119&searchBean.searchKey=&appYn=&searchBean.searchVal=&searchBean.startDt=&startDt=&searchBean.endDt=&endDt=&ctgCd=&sex=&school=&grade=&year=&month=&schoolDiv=&establDiv=&hopearea=&searchBean.deptCd=&searchBean.currentPage=1'+str(pagenum)
    r = requests.get(url)
    html = r.text
    soup  = bs(html, 'html.parser')
    tr = soup.select('tbody > tr')
    for i in range(len(tr)):
        if tr[i].select('td')[4].text.strip():
            result[0].append(tr[i].select('td')[1].text.strip())
            result[1].append(tr[i].select('td')[2].text.strip())
            result[2].append(tr[i].select('td')[4].text.strip())

    for i in range(len(result[0])):
        if "ddd" in result[2][i]
            print(result[0][i], result[1][i], result[2][i]))


fuck(1)
fuck(2)
fuck(3)
