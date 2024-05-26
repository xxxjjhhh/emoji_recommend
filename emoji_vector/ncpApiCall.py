# -*- coding: utf-8 -*-
import json
import http.client

class NcpApiCall():
    def __init__(self) -> None:
        self.__host = 'clovastudio.apigw.ntruss.com'
        self.__path = '/testapp/v1/api-tools/embedding/clir-emb-dolphin/a94490cc05eb4467859045836eb77d04'
        self.__api_key = 'NTA0MjU2MWZlZTcxNDJiY8PymlAy1/NbUwjSOdrpZy9Lld76ceoqaWOH9Xn5zDKt'
        self.__api_key_primary_val = 'Oo5ZzbtiCS46dZfye2dV4uizSx95pUJaNSzm45wd'
        self.__request_id = 'a54ad6aa-805c-41ff-8357-217a24bb5ab2'

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
