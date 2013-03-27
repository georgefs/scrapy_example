# -*- coding: utf-8 -*-
#!/usr/bin/env python

from scrapy.spider import BaseSpider
from datetime import date, timedelta
from scrapy.http.request.form import FormRequest
import lxml
import os

file_path=os.path.abspath(__file__)
path = os.path.split(file_path)[0]
RESULT_PATH = os.path.join( path, "result")
"""
玉山銀行匯率spider
"""
class EsunbankSpider(BaseSpider):

    name = "esunbank"
    allowed_domains = ["esunbank.com.tw"]
    start_urls = (
            'http://www.esunbank.com.tw/info/rate_spot_exchange_history.aspx',
            )
    start_date = date(2008,4,1)
    
    def __init__(self):
        pass

    def parse(self, response):
        
        one_day_time = timedelta(days=1)    
        start_date = self.start_date
        today = date.today()
        body=lxml.html.fromstring(response.body)

        process_date = start_date    
        view_state = body.cssselect('input[name=__VIEWSTATE]')[0].value
        event_target = "cal_Date"
        
        data = {}

        while True:
            data.update({ "cal_Date" : process_date.strftime('%Y-%m-%d') })
            #scrapy 提供的好用功能!! 可以先幫你parse response 的目標form, 擷取資料後再修改自己的資料再送出就好XD
            yield FormRequest.from_response( 
                                             response = response,
                                             formdata = data,
                                             formname = "frmInfo",
                                             callback = self.parse_item
                                             )   
            #日期遞增
            process_date += one_day_time
            if process_date > today:
                break



    def parse_item(self, response):
        print 'parse_item'
        self.tmp = open(RESULT_PATH, "a+")
        body = lxml.html.fromstring(response.body.decode('utf-8'))
        f = self.tmp        
        datas = body.cssselect('.tableContent-light td')
        time = body.cssselect('input[name=cal_Date]')[0].value
        

        #簡單的組csv..
        result = [time]
        for data in datas:
            value = data.text
            try:
                result.append(value.encode('utf-8'))
            except Exception:
                result.append('')

        result.append('\n')

        f.write("\t".join(result))
        f.flush()
        f.close()



