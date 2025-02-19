# emoji_recommend

사용자로 부터 한글 문장을 입력 받아 생성된 임베딩 벡터로 유클리드 거리 기반 이모지 추천 시스템.

한국어 설명을 가진 이모지는 npm 리포지토리의 emoji_korean을 사용했고 임베딩 모델은 네이버 클라우드 플랫폼의 클로바 스튜디오 임베딩 API를 활용했다.

## 카테고리

<pre><code>

- asset
  - emoji_korean.json : 한국어 설명을 가진 이모지 json 파일
  - emoji_vector.json : 한국어 설명에 대한 1024차원 임베딩 벡터를 가진 이모지 hexcode json 파일
- aws_lambda
  - emoji_vector.json : 한국어 설명에 대한 1024차원 임베딩 벡터를 가진 이모지 hexcode json 파일
  - lambda_function.py : AWS Lambda 기반으로 동작하는 추천 시스템
  - ncpApiCall.py : NCP 클로바 스튜디오 임베딩 API 호출 파일
- emoji_vector
  - jsonExecutor.py : asset 경로에 존재하는 json 파일 읽기, 쓰기 파일
  - ncpApiCall.py : NCP 클로바 스튜디오 임베딩 API 호출 파일
  - wordToVec.py : emoji_korean.json 파일을 불러와 각각의 이모지 설명에 대한 NCP 클로바 스튜디오 1024차원 임베딩 벡터를 획득하고 emoji_vector.json으로 만드는 파일
- fastapi
  - main.py : fastapi 서버 프레임워크 기반으로 동작하는 추천 시스템
- local_test
  
</code></pre>

## 이모지 데이터

한국어 설명 기반 이모지는 npm 리포지토리의 emoji_korean을 사용한다.

https://www.npmjs.com/package/emoji_korean

<pre><code>
npm i emoji_korean
</code></pre>

## NCP 클로바 스튜디오 임베딩 API

NCP 콘솔 > CLOVA Studio > 임베딩

https://console.ncloud.com/clova-studio/product

- API 호출 파이썬 SDK
<pre><code>

  # -*- coding: utf-8 -*-

import base64
import json
import http.client


class CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def _send_request(self, completion_request):
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id
        }

        conn = http.client.HTTPSConnection(self._host)
        conn.request('POST', '/testapp/v1/api-tools/embedding/clir-emb-dolphin/a9생략', json.dumps(completion_request), headers)
        response = conn.getresponse()
        result = json.loads(response.read().decode(encoding='utf-8'))
        conn.close()
        return result

    def execute(self, completion_request):
        res = self._send_request(completion_request)
        if res['status']['code'] == '20000':
            return res['result']['embedding']
        else:
            return 'Error'


if __name__ == '__main__':
    completion_executor = CompletionExecutor(
        host='clovastudio.apigw.ntruss.com',
        api_key='',
        api_key_primary_val = '',
        request_id=''
    )

    request_data = json.loads("""{
  "text" : "웃는 얼굴"
}""", strict=False)

    response_text = completion_executor.execute(request_data)
    print(request_data)
    print(response_text)

  
</code></pre>

## NCP 클로바 스튜디오 임베딩 API 제공 모델

- clir-emb-dolphin : 도메인과 무관한 범용성
- clir-sts-dolphin : 작은 범위에서 세부적으로 유사도 체크


## Lambda 테스트

## AWS Lambda 업로딩 10MB 제한 문제

AWS S3를 활용하면 좋으나 Lambda에 직접 올려도 사용은 가능

## Lambda Timeout 문제

Lambda 메모리 용량을 늘리면 무방, emoji를 벡터화 시킨 emoji_vector.json 파일 자체를 파이썬 변수로 올려서 구동 시키는게 훨씬 빠르게 로딩됨

약 1300개의 이모지 hexcode에 대한 벡터 데이터를 가지는 코드는 메모리 용량 1300MB ~ 1500MB가 필요 (Python3.12)

---
