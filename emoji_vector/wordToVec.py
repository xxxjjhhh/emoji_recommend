# -*- coding: utf-8 -*-
import json

from ncpApiCall import NcpApiCall
from jsonExecutor import JonsExecutor

# class init
ncpApiCall = NcpApiCall()
jsonExecutor = JonsExecutor()


def call_api() -> list:

    vector_list = []

    raw_data = jsonExecutor.read_file()
    for num, row in enumerate(raw_data):
        print(num)
        request_data = json.loads('{"text": "' + row["description"] + '"}', strict=False)
        # call api, res : list
        response_data = ncpApiCall.execute(request_data)

        vector_data = {"hexcode" : row['hexcode'], "vector" : response_data}
        vector_list.append(vector_data)

    return vector_list

def save_result(vector_list: list) -> None:
    
    jsonExecutor.write_file(vector_list)


if __name__ == '__main__':
    vector_list = call_api()
    save_result(vector_list)
