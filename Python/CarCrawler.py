mport selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from tqdm import tqdm
import pandas as pd

Python_dir = os.getcwd()
os.chdir(Python_dir[:-6])



        

class CarCrawling(self):
    def __init__(self):
        
        '''
        url = Danawa Car URL
        driver = ChromeDriver for selenium lib.
        text,col = for setting Data.
        option = ChromeDriver options.
        add_argument = Chrome window size : 1920 x 1080.
        
        '''
        
        self.url  = 'http://auto.danawa.com/auto/modelPopup.php?Type=spec&Lineup='
        self.driver = webdriver.Chrome('./driver/chromedriver', options=options) #Chromedriver는 driver Folder에 둘것.
        self.text = [[],[],[],[],[],[]]
        self.col =['차종', '전장(mm)', '전폭(㎜)', '전고(㎜)', '축거(㎜)']
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('window-size=1920,1080')
        
        #해당 URL 크롤링시 여러가지 형식으로 이루어져 있음.
        #그에따라, 가장 많이 쓰이거나, 적절한 형태의 html을 Parsing 하는것으로 하였음.
        #그것은 아래의 두가지 형식을 따라 하게되면 html을 Parsing하여, Web Crawling이 가능하게 하였음.
    
    #1번    
    def carCrawling1_set(tbody): 
        text = self.text
        rows = tbody.find_elements_by_tag_name("tr")

        len_text = len(rows[0].find_elements_by_tag_name('th'))
        t_count = [0,2,3,4,5] # 0 = 차 제원명 , 2 = 차 전장, 3 = 전폭, 4 = 전고, 5 = 축거

        for i in t_count:
            if i == 0:
                tag ='th' #차 제원은 th
            else :
                tag = 'td' #나머지는 td로 되어있음

            t = rows[i].find_elements_by_tag_name(tag)

            for text_count in range(len_text):
                if i == 2:
                    text[i].append(t[text_count+1].text)
                else:
                    text[i].append(t[text_count].text)

        text=pd.DataFrame(text).T
        text=text.drop(columns=1)
        text.columns= self.col
        return text.iloc[1:]
    
    #2번
     def carCrawling2_set(driver): 
        text = self.text
        x = 0
        t = driver.find_element_by_class_name('trim').text
        for text_count in t :
            text[x].append(text_count.text);

        for i in range(36,40):
            x += 1;        
            id = 'compareRight_'+str(i)
            t = driver.find_element_by_id(id)#36 = 전장, 37 = 전폭, 38 = 전고, 39 = 축거 
            for text_count in t :
                text[x].append(text_count.text)

        text=pd.DataFrame(text).T
        text=text.drop(columns=1)
        text.columns= self.col      
        return text
    
    #실제 Crawling 되는 Function.
    def carCrawling(self,start,end):
        
        '''
        start = URL Crawling시, 시작되는 Page
        end = URL Crawling시, 종료되는 Page
        '''
        
        
        options = self.options
        driver = self.driver
        driver.implicitly_wait(5)#as same as time.sleep()

        context = pd.DataFrame(self.col)
        context = context.T
        context.columns = self.col 

        url = self.url

        for page in tqdm(range(start,end), desc="WebPage is", mininterval=0.01):
            driver.get(url=url+str(page))
            try :
                company_name = driver.find_element_by_class_name('name').text #Company_name
                tbody = driver.find_element_by_tag_name("tbody")
            except :
                continue;

            if tbody.text != '세부모델':
                try :
                    #1번
                    text = CarCrawling.carCrawling1_set(tbody);
                    text.차종 = company_name+'::'+text.차종
                    context = pd.concat([context,text])
                except :
                    continue;
            else : 
                try :
                    #2번
                    text = CarCrawling.carCrawling2_set(driver)
                    text.차종 = company_name+'::'+text.차종
                    context = pd.concat([context,text])
                except :
                    continue;

        print('-----end------')
        print(context.head())
        
        #해당 WorkDirectory의 Data Folder에 저장.
        context.to_csv('data/Context-'+str(start)+'-'+str(end)+'.csv')
        return context
