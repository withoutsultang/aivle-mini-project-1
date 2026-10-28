# 데이터 준비 및 실행

저장소 루트에서 의존성을 설치한 뒤 Jupyter로 각 프로젝트의 노트북을 실행합니다. 로컬 실행용 노트북은 저장소 루트의 `requirements.txt`를 기준으로 데이터 경로를 찾습니다.

## 과제1 · 미세먼지

다음 파일을 `data/dust/`에 배치합니다.

- `air_2024.csv`, `air_2025.csv`
- `weather_2024.csv`, `weather_2025.csv`

팀 코드의 파일 인코딩은 `cp949`입니다. [미세먼지 노트북](../projects/01-pm10-prediction/notebooks/01_pm10_prediction.ipynb)은 전처리 후 생성한 CSV를 모델링 단계에서 읽습니다.

데이터 출처: [에어코리아](https://www.airkorea.or.kr/web/pastSearch?pMENU_NO=123), [기상청 ASOS](https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36)

## 과제2 · HAR

다음 파일을 `data/har/`에 배치합니다.

- `data01_train.csv` — 5,881행 × 563열
- `data01_test.csv` — 1,471행 × 563열
- `features.csv` — 특성 설명

563열은 센서 특성561개와 `subject`, `Activity`로 구성됩니다. [EDA·모델링 노트북](../projects/02-har-classification/notebooks/)에서 각 단계를 실행합니다.

## 추가 실행 도구

```bash
python scripts/verify_har_eda.py --data-dir data/har --output results/har_eda_current.json
```

저장소 정리 시 추가한 Random Forest 기준 모델 실행 도구입니다. 2026-10-28 검증 데이터1,177건에서 정확도97.96%를 기록했습니다. 팀의 단계별 DNN 테스트와는 별도의 실험입니다.

데이터·모델 파일은 Git 추적에서 제외합니다. `requirements.txt`와 `requirements-dl.txt`는 실행용 의존성 목록입니다. 원본 교육 환경의 버전을 고정한 파일은 아닙니다.
