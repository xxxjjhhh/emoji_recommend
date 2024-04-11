# -*- coding: utf-8 -*-
import json
import http.client

class NcpApiCall():
    def __init__(self) -> None:
        self.__host = 'clovastudio.apigw.ntruss.com'
        self.__path = ''
        self.__api_key = ''
        self.__api_key_primary_val = ''
        self.__request_id = ''

    def __send_request(self, completion_request) -> any:
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-NCP-CLOVASTUDIO-API-KEY': self.__api_key,
            'X-NCP-APIGW-API-KEY': self.__api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self.__request_id
        }

        conn = http.client.HTTPSConnection(self.__host)
        conn.request('POST', self.__path, json.dumps(completion_request), headers)
        response = conn.getresponse()
        result = json.loads(response.read().decode(encoding='utf-8'))
        conn.close()
        
        return result
    
    def execute(self, completion_request) -> any:
        res = self.__send_request(completion_request)
        if res['status']['code'] == '20000':
            return res['result']['embedding']
        else:
            return 'Error'
