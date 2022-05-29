import requests
from bs4 import BeautifulSoup as BS
import codecs
import lxml.html as LH

def prepare_data_for_searching(textAterRecognized):
    url = "https://mediametrics.ru/search/week.html#ru:tm:"
    textAterRecognized = textAterRecognized.replace(' ', '%20')
    url = (url + textAterRecognized)[:-3]
    #html_request(url)
    



def  html_request(url):
    #take the source
    html_taken = requests.get(url)
    print(html_taken.text)
    '''
    parse = open("sample.html","w")
    parse.write(html_taken.text)
    parse.close()


    #parse in file
    #parse = BS(html_taken.text, "source.html")
    for el in parse.select('#news > .rsearch > .rs-link'):
        #text = el.select("a") 
        href_tag = el.find(href = True) 
        print() 
        print(href_tag['href'])'''

    root = LH.fromstring(html_taken.text)
    for el in root.iter('rslink'):
        id=el.get('a')
        print('Ele class : ' + str(id))
        outString = outString + el.text + "|"+fileName+"|"+id+"\n"
    return 0

url = "https://mediametrics.ru/search/week.html#ru:tm:Страны%20ес%20уступают%20российским%20требованиям%20об%20оплате%20за%20газ%20в%20рублях.%20Если%20за%20венгрией%20уступает%20требованиям%20президента%20россии%20владимира%20путина%20то%20по%20пати%20газа%20в%20рублях%20пишут%20бунберг%20в%20статье%20до%20журнала.%20Обозреватели%20джон%20фолей%20и%20альберта%20нордели%20странно%20члены%20ес%20все%20больше%20и%20больше%20разделяются%20в%20вопросах%20касающихся%20украины%20в%20том%20числе%20ведения%20санкций%20против%20россии.%20Основное%20внимание%20было%20уделено%20отказу%20венгрии%20поддержать%20санкции%20однако%20другие%20страны%20уступают%20требованиям%20путина%20о%20платежах%20за%20газ%20в%20рублях%20отметили%20авторы."
html_request(url)