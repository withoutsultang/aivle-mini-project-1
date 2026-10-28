# 데이터 배치

원본 데이터는 Git에 포함하지 않습니다. 교육 과정에서 적법하게 확보한 파일을 아래에 두세요. 강의 파일의 이용·배포 범위는 별도로 확인해야 합니다.

## HAR: data/har/

- data01_train.csv: 5,881행 × 563열
- data01_test.csv: 1,471행 × 563열
- features.csv: 561행 × 4열

학습·테스트에는 561특성 + subject + Activity가 있습니다. 확보한 두 파일의 결측은 0이며 subject 각21명이 모두 겹칩니다. 데이터 분할 근거와 원래 공개 HAR 자료의 분할을 동일하다고 가정하지 마세요. 기본 노트북의 과거 출력638/798건은 이 파일과 다릅니다.

## 미세먼지: data/dust/

- air_2024.csv / air_2025.csv
- weather_2024.csv / weather_2025.csv

현재 이 네 파일은 미확보입니다. 교안상 에어코리아 서울 종로구 관측2024년 전체 학습/2025년1~4월 테스트, 기상청 서울 날씨2024년 전체 학습/2025년1~5월 테스트입니다. 원본은 cp949로 읽는 코드입니다. 각 CSV의 열 이름과 시간 표현이 팀 노트북과 맞아야 하며, 최신 사이트에서 새로 받은 데이터로 과거 성능이 재현된다고 보장하지 않습니다.

[에어코리아](https://www.airkorea.or.kr/web/pastSearch?pMENU_NO=123) / [기상청 ASOS](https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36)

노트북은 실행 도중 data 폴더 아래 파생 CSV·pkl·모델 파일을 만들 수 있습니다. .gitignore에서 이를 제외합니다.
