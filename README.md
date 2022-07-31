# 리사야 냉장고를 부탁해



## 개요 ##
- 냉장고의 남은 식재료 기반으로 완성도 높은 요리를 추천해주는 웹서비스
- 홈페이지에 영수증 사진을 등록하면 식재료의 유통기한을 알려주는 모델도 구현
- 광주형 인공지능 아이디어 공모전 수상작(우수상)

## 환경
- python version == 3.8
- requirements.txt 참조

## konlpy 모델관련
- 식재료명 분석에 사용된 konlpy 모델은 Java 기반이기 때문에 그냥 pip install konlpy로 설치할 수 없습니다.

- 아래 주소는 konlpy 설치 절차 설명글
(https://velog.io/@soo-im/konlpy-%EC%84%A4%EC%B9%98-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0%EC%B1%85-%EC%95%84%EB%82%98%EC%BD%98%EB%8B%A4-JPYPE)

- 실행이 안된다면 pip install tweepy==3.10.0 를 통해 tweepy 버전을 다시 설정해보세요.

## google-vision 관련
- google-cloud-vision을 이용하기 위해선 gcp-key 등록을 통해 개인 고유 key를 확보해야 합니다.
show_expiration.py 파일에 자신의 gcp-key 경로를 첨부하세요.
- 아래 주소는 gcp-key 등록 절차 설명글
https://naramp4.github.io/python/ocr/#%ED%8F%B4%EB%8D%94-%EA%B5%AC%EC%A1%B0

## 실행 예시
- 콤마(",")를 기준으로 냉장고의 남은 재료를 입력하면, 입력 재료에 기반하여 크롤링한 데이터(10,000여개)를 토대로 추천
- ![image](https://user-images.githubusercontent.com/62554639/137439590-4fbddbd8-a084-4074-9a24-541c6d67db6e.png)

- 크롤링 데이터는 만개의 레시피에서 크롤링함
- main.py를 실행하면 됩니다

