# -*- coding: utf-8 -*-
import json
import http.client

class NcpApiCall():
    def __init__(self) -> None:
        self.__host = 'clovastudio.apigw.ntruss.com'
        self.__path = '/testapp/v1/api-tools/embedding/clir-emb-dolphin/a94490cc05eb4467859045836eb77d04'
        self.__api_key = 'NTA0MjU2MWZlZTcxNDJiY1hwQAv1f9N2hXCKeNLejej4xsafLclhA+rTcTphvp8q'
        self.__api_key_primary_val = 'k5TdtxTKiZi4O7gi6uidLBXnqzU4eG0vmBfF9Ys0'
        self.__request_id = 'f0fda080-70d1-4d3d-8edd-b6f9fd0cb1e0'

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
