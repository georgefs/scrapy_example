from .ithelp import IthelpSpider
from scrapy.http.request import Request
import json
import urllib
import os

file_path=os.path.abspath(__file__)
path = os.path.split(file_path)[0]
answer_path = os.path.join( path, "answer")

TMP_PATH = os.path.join(path, "tmp")

data = open(answer_path).read()
ANSWER = json.loads(data)

class JsNinjaSpider(IthelpSpider):
    name = "get_questions"

    def parse(self, response):
        print 'parse'
        resource = response.body
        data = json.loads(resource)

        tmp = open(TMP_PATH, 'a+')
        
        result = []
        result.append(data.get('quizid'))
        result.append("\t")
        result.append(resource)
        result.append('\n')
        
        tmp.write("".join(result))
        tmp.flush()
        tmp.close()

    def make_requests(self):

        url = "http://ithelp.ithome.com.tw/js-ninja/quiz2013/getquiz"
        for i in range(10000):
            yield Request(url, headers=self.headers, dont_filter=True)


class NinjaRobot(IthelpSpider):
    name = "robot"


    def make_requests(self):
        return self.get_question()

    def get_question(self, response=None):
         
        url = "http://ithelp.ithome.com.tw/js-ninja/quiz2013/getquiz"
        return Request(url, headers=self.headers, callback=self.answer_question, dont_filter=True)
        
    def answer_question(self, response):
        url = "http://ithelp.ithome.com.tw/js-ninja/quiz2013/sendans"
        data = json.loads(response.body)
        options = data.get("answer")
        quizid = data.get("quizid")
        answer = ANSWER.get(quizid)

        print 'solve {}'.format(data.get('solve'))
        tmp = dict()
        [tmp.update(opt) for opt in options]
        options = dict(zip(tmp.values(),tmp.keys()))
        optionid = options.get(answer)

        data = {  
                    "quizid": quizid,
                    "playno": data.get('playno'),
                    "roundtime": data.get('roundtime'),
                    "optionid": optionid
                }

        data = urllib.urlencode(data)
        req = Request(url, body=data, method="POST", callback=self.get_question, dont_filter=True)
        req.headers.setdefault('Content-Type', 'application/x-www-form-urlencoded')
        return req
