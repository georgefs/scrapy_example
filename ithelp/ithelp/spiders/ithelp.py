from scrapy.http.request.form import FormRequest
from scrapy.spider import BaseSpider
from scrapy.http.request import Request
import json, urllib
from lxml import html
from getpass import getpass


class IthelpSpider(BaseSpider):
    

    login_page = "http://ithelp.ithome.com.tw/"

    headers = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Charset':'Big5,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
            'Connection':'keep-alive',
            'Host':'ithelp.ithome.com.tw',
            'Referer':'http://ithelp.ithome.com.tw/js-ninja/quiz2013',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22',
            }



    def parse(self, response):
        pass


    def start_requests(self):
        print 'start request'
        return [self.login()]


    def login(self, response=None):
        print 'login'
        url = self.login_page
        if(response == None):
            return Request(url, method="POST", dont_filter=True, callback=self.login)
            
        
        name = html.fromstring(response.body).cssselect('#ithelpProfile h3')

        if(name):
            return self.make_requests()

        else:
            user = raw_input("enter username: ")
            password = getpass("enter password: ")

            data = {"username":user, "password":password}
            return FormRequest.from_response(response, formname="login", formdata=data, callback=self.login, dont_filter=True)


    def make_requests(self):
        print 'make_requests'
        raise Exception, 'not in use'
        pass
    
