from selenium import webdriver
from time import sleep
class Parser:

    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1280, 1024)
        self.driver.get('http://www.yellowpages.ca/search/si/1/Used+Car+Dealers/canada')

    def scroll_down(self):
        last_height = self.driver.execute_script('return document.body.scrollHeight')
        for x in range(1):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(30)
            newheight = self.driver.execute_script("return document.body.scrollHeight")
            print newheight
            print last_height
            if newheight == last_height:
                break
            last_height = newheight
    def analizator(self):
        self.linkuri = self.driver.find_elements_by_xpath('//h3[@class="listing__name jsMapBubbleName"]/a')
        try:
            for element in self.linkuri:
                print element.get_attribute('href')
                with open('rezultat.txt', 'a') as f:
                    f.write(element.get_attribute('href') +'\n')
                    f.close()
        except Exception, e:
            print e


    def feedBack(self):
        self.driver.quit()


if __name__ == '__main__':
    a = Parser()
    a.scroll_down()
    a.analizator()
    a.feedBack()
