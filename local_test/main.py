# -*- coding: utf-8 -*-
import json
import math

from ncpApiCall import NcpApiCall

ncpApiCall = NcpApiCall()

def distance(vector1: list, vector2: list) -> float:
    sum_of_squares = sum((v2 - v1) ** 2 for v1, v2 in zip(vector1, vector2))
    return math.sqrt(sum_of_squares)

def main() -> None:

    title = ""

    request_data = json.loads(f'{{"text": "{title}"}}', strict=False)
    # call api, res : list
    response_data = ncpApiCall.execute(request_data)

    with open("../asset/emoji_vector.json") as file:
        candidate_data = json.load(file)

    dist_list = []
    for row in candidate_data:

        dist_data = {"hexcode": row['hexcode'], "distance": distance(row['vector'], response_data)}
        dist_list.append(dist_data)

    min_distance_row = min(dist_list, key=lambda x: float(x["distance"]))
    min_hexcode = min_distance_row['hexcode']

    print(min_hexcode)

if __name__ == '__main__':
    main()
