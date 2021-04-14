import re

import requests as req
class GoogleReq():
    def __init__(self):
        self.apikey="AIzaSyAxG6wmKjvs6ni4WEcXIG18cw4DLquuAKI"

    def get_direct_info(self,paramOri,paramDes):
        temp_url="https://maps.googleapis.com/maps/api/directions/json?origin="+paramOri+"&destination="+paramDes+"&key="+self.apikey
        ret_dic=req.post(temp_url).json()
        htmlre=re.compile('>(.*?)<')
        temp_steps=ret_dic["routes"][0]["legs"][0]["steps"]
        retstr=""
        for tem in temp_steps:
            retstr=retstr+">>>"+''.join(htmlre.findall(tem["html_instructions"]))
        return retstr
    def do_translate(self,paramContent):
        language_type = ""
        url = "https://translation.googleapis.com/language/translate/v2"
        data = {
            'key': self.apikey,
            'source': language_type,
            'target': 'zh-cn',
            'q': paramContent,
            'format': "text"
        }
        res = req.post(url, data).json()
        print(res)
        result = res["data"]["translations"][0]["translatedText"]
        return result



# mapReq=GoogleReq()
# print(mapReq.get_direct_info("Washington","Chicago"))
