ReadMe
====================
玉山銀行的匯率資料scrapy

這個範例用scrapy 的FormRequest 去掃玉山銀行的幣值匯率0.0
超好用XD
FormRequest 基本上就是幫你把data 包給request 再發.. 這沒什麼ˇˇ

不過有做一個功能0..0
FormRequest.from_response
顧名思義就是用本來的response 的資料帶入來做request~

但是.. scrapy 的cookie  header 本來就在 downloadermiddleware 裡面做merge了阿~
那這個功能事做啥鬼的XD

其實就是幫你去分析response body裡面的form的資料, 再組合你想修改的資料來做回傳的~ 超方便@@"  晚點我也來改urllib2, 這功能好棒XD

from_response(cls, response, formname=None, formnumber=0, formdata=None, clickdata=None, dont_click=False, **kwargs)

恩 doc 裡面的
cls 這用classmetho 裝飾, 所以不解釋...
response 就是你想submit form 的頁面的response
formname 這就是你想要submit 的 form 在response 裡面的name
formnumber 恩ˇˇ 如果有同樣的formname 你要送哪個0..0
clickdata & dont_click 我沒用到XD 不過應該是click 的選取設定ˇˇ

Run-service
====================
scrapy crawl esunbank
