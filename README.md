# 테이블 데이터 수정 예제

Streamlit을 사용한 CSV 테이블 데이터 수정 예제 애플리케이션입니다.

## 데모
실제 동작하는 예제는 다음 링크에서 확인할 수 있습니다:
https://esoyeon-streamlit-table-edit-app-ogsp13.streamlit.app/

## 파일 구조
- `app.py`: Streamlit 메인 애플리케이션
- `generate_data.py`: 샘플 데이터 생성 스크립트
- `research_projects.csv`: 테이블 데이터 파일

## 실행 방법

1. 가상환경 생성 및 활성화
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. 필요한 패키지 설치
```
pip install streamlit pandas
```

3. 샘플 데이터 생성 (선택사항)
```
python generate_data.py
```

4. Streamlit 애플리케이션 실행
```
streamlit run app.py
```

## 주요 기능
- CSV 파일의 테이블 데이터 조회
- 데이터 수정 및 실시간 업데이트
- 수정된 데이터 CSV 파일 저장
