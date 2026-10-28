# KT AIVLE School · 데이터 분석 & AI 모델링

**미니프로젝트 1차 | 2025.10.15–10.17 | 7인 팀**

공공데이터와 스마트폰 센서 데이터를 활용해 **전처리 → 특성 분석 → 모델링 → 평가**를 수행한 두 프로젝트입니다.

## 프로젝트

| 프로젝트 | 주요 내용 | 팀 성과 | 바로가기 |
| --- | --- | --- | --- |
| **01 · 미세먼지 농도 예측** | 대기·기상 데이터 결합, 시계열 특성 생성, 앙상블 모델 비교·튜닝 | Gradient Boosting **R² 0.9362** | [프로젝트 보기](projects/01-pm10-prediction/) |
| **02 · 스마트폰 행동 인식** | 561개 센서 특성 분석, 정적·동적 분기 기반 단계별 DNN | 6종 행동 분류 **정확도 96.13%** | [프로젝트 보기](projects/02-har-classification/) |

## 담당 역할 · 김건우

두 과제의 **코드 정리 및 조별 통합본 관리**를 담당했습니다. 미세먼지 과제에서는 PM10을 제외한 변수 중요도 분석을 수행하고, 시정·CO와 대기오염의 관계를 해석해 팀 발표에 공유했습니다.

각 프로젝트 페이지에서 **개인 담당 역할**과 **팀의 구현·평가 결과**를 구분해 소개합니다.

## 기술 스택

**Python · Pandas · NumPy · scikit-learn · XGBoost · TensorFlow/Keras · Matplotlib · Seaborn**

## 실행

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -r requirements-dl.txt  # HAR DNN 실행 시
jupyter lab
```

데이터 배치는 [데이터 준비 안내](docs/DATA.md)를 참고하세요. 각 프로젝트 폴더에 분석·모델링 노트북을 구성했습니다. 데이터 및 학습 모델 파일은 별도로 준비합니다.
