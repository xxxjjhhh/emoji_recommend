# emoji_recommend

사용자로 부터 한글 문장을 입력 받아 생성된 임베딩 벡터로 유클리드 거리 기반 이모지 추천 시스템.

한국어 설명을 가진 이모지는 npm 리포지토리의 emoji_korean을 사용했고 임베딩 모델은 네이버 클라우드 플랫폼의 클로바 스튜디오 임베딩 API를 활용했다.

## 이모지 데이터

한국어 설명 기반 이모지는 npm 리포지토리의 emoji_korean을 사용한다.

https://www.npmjs.com/package/emoji_korean

<pre><code>
npm i emoji_korean
</code></pre>

## 카테고리

<pre><code>

- asset
  - emoji_korean.json : 한국어 설명을 가진 이모지 json 파일
  - emoji_vector.json : 한국어 설명에 대한 1024차원 임베딩 벡터를 가진 이모지 hexcode json 파일
- emoji_vector
  - jsonExecutor.py : asset 경로에 존재하는 json 파일 읽기, 쓰기 파일
  - ncpApiCall.py : NCP 클로바 스튜디오 임베딩 API 호출 파일
  - wordToVec.py : emoji_korean.json 파일을 불러와 각각의 이모지 설명에 대한 NCP 클로바 스튜디오 1024차원 임베딩 벡터를 획득하고 emoji_vector.json으로 만드는 파일
- local_test
  
</code></pre>

---
