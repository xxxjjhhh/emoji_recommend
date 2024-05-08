import json
import math

from ncpApiCall import NcpApiCall

ncpApiCall = NcpApiCall()

def distance(vector1: list, vector2: list) -> float:
    
    sum_of_squares = sum((v2 - v1) ** 2 for v1, v2 in zip(vector1, vector2))
    
    return math.sqrt(sum_of_squares)

def call_api(title: str) -> list:
    
    request_data = json.loads(f'{{"text": "{title}"}}', strict=False)
    # call api, res : list
    return ncpApiCall.execute(request_data)
    

def lambda_handler(event, context):
    
    request_body = json.loads(event['body'])
    title = request_body.get('title', None)
    
    response_data = call_api(title)
    
    with open("./emoji_vector.json") as file:
        candidate_data = json.load(file)

    dist_list = []
    for row in candidate_data:

        dist_data = {"hexcode": row['hexcode'], "distance": distance(row['vector'], response_data)}
        dist_list.append(dist_data)

    min_distance_row = min(dist_list, key=lambda x: float(x["distance"]))
    min_hexcode = min_distance_row['hexcode']
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(min_hexcode)
    }
