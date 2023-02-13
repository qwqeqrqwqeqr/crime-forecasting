
## 초기 환경 설정 및 확인 사항

***
### 데이터 베이스 설정 및 확인
- database 설정
  - postgresql 설치 
  - postgresql 사용자 생성 (이때, 사용자 권한은 insert,update,delete,select 모두 적용)
  - sql_script 디렉터리 내 6개 sql 파일 확인
  - **DB table 스키마 위치 이름 확인** 
    - 스키마 이름 변경할 경우 (public -> digitalif)  /app/database/query/query.py내 쿼리문 또한 변경해줘야함.  
***
### 필수 데이터 확인
- 지도 데이터 (./app/data/map)
  - grid_area.csv => 집계구 격자 데이터
  - grid_hangang.csv => 한강 격자 데이터
  - grid_subway.csv => 지하철 격자 데이터
  - grid_tourist.csv => 관광지 격자 데이터
  - grid_congestion.csv => 혼잡 지역 (실시간 도시) 격자 데이터
  - large_map => 자치구 격자 데이터
  - middle_map => 행정동 격자 데이터
  - small_map => 집계구 격자 데이터
  - grid.geojson => 격자 데이터
  - congestion_map.geojson => 혼잡지역 집계구 지리 데이터
  - large_map(dbf,prj,shp,shx) => 자치구 지리 데이터
  - middle_map(dbf,prj,shp,shx) => 행정동 지리 데이터
  - small_map(dbf,prj,shp,shx) => 집계구 지리 데이터 

- 원본 데이터 (./app/data/origin)
  - 위험시설 데이터
    - 서울시노래연습장업인허가정보.csv  
    - 서울시목욕장업인허가정보.csv  
    - 서울시유흥주점영업인허가정보.csv 
    - 서울시단란주점영업인허가정보.csv
    - 서울시숙박업인허가정보.csv   
    - 서울시인터넷컴퓨터게임시설제공업인허가정보.csv
  - 치안시설 데이터(./app/data/origin/police_facility)
    - 경찰서.csv 
    - 치안센터.
    - 파출소지구대.csv
  - 안전시설 데이터(./app/data/origin/safety_facility)
    - 서울시_CCTV_설치현황.csv 
    - 스마트보안등.csv  
    - 아동안전지킴이시설물.csv  
    - 여성안심지킴이집.csv 
    - 여성안심택배함.csv
    - 편의점.csv
***
###  생활인구 폴더 확인
- 특정 폴더에 일마다 누적 (/population)
- 형식
  - 단일 파일 `LOCAL_PEOPLE_yyyyMMdd.csv`
***
###  신고 데이터 
- 특정 폴더에 일마다 누적 (/safty)
- 형식 
  - 단일 파일 `POL_01_YYYYMMDD.csv`
***
### 그외 확인 사항
- cron 실행 여부 확인
  - `crontab -l`
  - 설정 오류날 경우 cron.sh 파일을 crontab에 직접 주입
  - crontab 점검 후 에도 cron 실행이 안된다면, docker container가 데몬으로 띄어져있는지 확인할 것
- data directory 확인 
  - /data/population
  - /data/safety
  - *데이터 폴더 경로 수정할 시, 하단 파일들의 내부 설정 접근 경로도 같이 수정할 것*
    - move_file_by_month.sh
    - move_file_by_year.sh
    - hangang.sh
    - report.sh
    - subway.sh
    - tourist.sh
    - congestion.sh
    - danger_index.sh 
- docker file 내부에서 DB ENV 정보에 맞게 수정



***
## AI
***
### 요약
- 현재 AI모델은 GWR,LR,LGBM 3가지를 사용하고 있음
  - GWR
    - 공간회귀를 통한 위험지수를 산출할 때 사용
    - 해당 방식은 학습에 긴시간(약 1일)이 소요 되기 떄문에 분석 용도로 사용
  - LR
    - logistic regression 방식으로 산출 데이터 뽑기위해 사용
    - 7개의 사건 종별 코드에 따라 산출하기 때문에 7번의 학습을 진행함
    - 공간회귀 방식을 통해 산출 데이터를 구할경우 약 7일이 소요되기 때문에 현재 LR을 채택함
  - LGBM 
    - 현재 월의 범죄 예측을 하기 위해 사용됨
    - 모델의 성능 지표와 같은 리포트를 추출하기 위해 사용
- 학습 데이터 구성 방식
  - 훈련
    - 시설 데이터
    - 생활인구 프로그램 가동 기준 N-2월 데이터
    - 112 신고 건수 작년 데이터
  - 테스트(예측)
    - 시설 데이터
    - 생활인구 프로그램 가동 기준 N-1월 데이터
    - 112 신고 건수 작년 데이터
  - 최종적으로 N월에 대한 예측 데이터가 만들어짐
  - 위험 지수는 N+1월에 대한 예측을 하기 위해 N-1월의 생활인구와 작년 112신고 건수를 사용함
  - 예시
    - 2023년도 2월 예측을 진행할 경우, 요구 데이터는 다음과 같음
      - 훈련: 2022년도 12월 생활인구, 시설 데이터, 2022년도 112 신고 건수 데이터
      - 테스트: 2023년도 1월 생활인구, 시설 데이터, 2022년도 112 신고 건수 데이터
***
### 산출 데이터 경로
- 모든 데이터는 ./app/data/ai/ 에 저장됨
- 저장되는 데이터
  - danger index
    - 모델, 전처리 학습 데이터 (총 7종) **(위험지수 결과 7종은 DB에 저장됨)**
  - spatial regression
    - 모델, 전처리 학습 데이터, 결과 데이터(위험지수)
  - predict
    - 모델, 스케일러, 테스트용 전처리 데이터, 학습용 전처리 데이터, 최종 예측 데이터

***
## 프로그램 별 요구 데이터 정리
  - **관광지 경찰대(tourist_app)** ->일일 112 신고 건수, 관광지 격자 맵 데이터(기보유), 서울시 격자 맵(기보유)
  - **한강 경찰대(hangang_app)** ->일일 112 신고 건수, 한강 격자 맵 데이터(기보유), 서울시 격자 맵(기보유)
  - **지하철 경찰대(subway_app)** ->일일 112 신고 건수, 지하철 격자 맵 데이터(기보유), 서울시 격자 맵(기보유)
  - **혼잡도(congestion_app)** -> 한달 112 신고 건수, 한달 생활인구, 혼잡 지역 격자 맵 데이터(기보유),서울시 집계구 맵(기보유),서울시 격자 맵(기보유)
  - **위험지수(산출용)(danger_index_app)** -> 1년 112 신고 건수, 한달 생활인구, 시설 데이터(기보유)
  - **공간회귀 위험지수(spatial_regression_danger_index_app)** -> 1년 112 신고 건수, 한달 생활인구, 시설 데이터(기보유)
  - **범죄 모델 훈련(predict_train_app)** -> 1년 112 신고 건수, 한달 생활인구, 시설 데이터(기보유)
  - **범죄 모델 예측(predict_test_app)** -> 1년 112 신고 건수, 한달 생활인구, 시설 데이터(기보유), 모델, 스케일러
***


## 실행
***
### 도커 실행
- docker build (반드시 외부에서 빌드해서 이미지 만들 것)
  - `sudo docker build -t [image-name]  ./`
- docker run (생활인구 신고데이터폴더를 컨테이너에서 접근할 수 있도록 연결)
  - `docker run -it -d -v /data:/data [image]`
- 내부 shell 접속
  - `sudo docker attach [container_id]`
***
### 수동 실행 (경찰대 3종 유형별 신고건수)
- `python3 (파일이름)_app.py "112신고경로 파일"`
- 요구되는 파라미터는  (파일이름)_app.py 파일을 열어보면 상단 주석에 기재 되어있음
- 반드시 파라미터 경로 확인 후 실행할 것
- 예시 (2023년 1월 관광지 경찰대를 수동 추출 하고 싶을 경우)
  - seoul 디렉터리로 이동
  - `python3 tourist_app.py "/data/safty/POL_01_20230101.csv"`
- (추가) 경찰대 csv 파일에 header가 빠져서 전송 되는 이슈가 있음 헤더를 추가하기 위해선 다음과 같이 작업함 **(자동 실행의 경우 header 자동 추가 코드가 붙혀져 있으니, 고려하지 않아도 됨)**
  1. 해당 파일이 있는 디렉터리로 이동
  2. 다음 명령어를 실행
  3. perl -p -i -e '$.==1 and print "RECV_NO,DAY,TIME,EVT_CL_CD,RECV_EMG_CD,RPTER_SEX,TRC_TYPE,HPPN_Y_SW,HPPN_X_SW,HPPN_Y_NE,HPPN_X_NE,HPPN_Y_NW,HPPN_X_NW,HPPN_Y_SE,HPPN_X_SE,END_CD\n"' [파일이름]
***
### 수동 실행 (혼잡도)
- `python3 (파일이름)_app.py "112신고건수 디렉터리", "생활인구 디렉터리"`
- 요구되는 파라미터는  (파일이름)_app.py 파일을 열어보면 상단 주석에 기재 되어있음
- 반드시 파라미터 경로 확인 후 실행할 것 (디렉터리의 경우 마지막은 /로 끝나야 함)
- 각 년월별 디렉터리들은 move_file.sh가 만들어냄
- 예시 (2023년 1월 혼잡도를 수동 추출 하고 싶을 경우)
  - seoul 디렉터리로 이동
  - `python3 congestion_app.py "/data/safty/202301/" "/data/population/202301/"`
***
### 수동 실행 (위험지수)
- `python3 (파일이름)_app.py "112신고건수 디렉터리", "생활인구 디렉터리"`
- 요구되는 파라미터는  (파일이름)_app.py 파일을 열어보면 상단 주석에 기재 되어있음
- 반드시 파라미터 경로 확인 후 실행할 것 (디렉터리의 경우 마지막은 /로 끝나야 함)
- 위험지수의 경우 지난달의 생활인구와 지난년도의 신고건수를 사용하여 산출
- 각 년월별 디렉터리들은 move_file.sh가 만들어냄
- 예시 (2023년 1월 위험지수를 수동 추출 하고 싶을 경우)
  - seoul 디렉터리로 이동
  - `python3 danger_index_app.py "/data/safty/2022/" "/data/population/202212/"`

***
### 수동 실행 (훈련 및 예측)
**훈련**
- `python3 (파일이름)_app.py "112신고건수 디렉터리", "생활인구 디렉터리"`
- 요구되는 파라미터는  (파일이름)_app.py 파일을 열어보면 상단 주석에 기재 되어있음
- 반드시 파라미터 경로 확인 후 실행할 것 (디렉터리의 경우 마지막은 /로 끝나야 함)
- 훈련의 경우 지지난달의 생활인구와 지난년도의 신고건수를 사용하여 산출
- 각 년월별 디렉터리들은 move_file.sh가 만들어냄
- 훈련을 진행할 경우 /seoul/app/data/ai/predict/ 디렉터리 내에 model 및 scaler가 만들어짐
- 예시 (2023년 1월에 대해 훈련을 하고 싶은 경우)
  - seoul 디렉터리로 이동
  - `python3 predict_train_app.py "/data/safty/2022/" "/data/population/202211/"`

**예측**
- `python3 (파일이름)_app.py "112신고건수 디렉터리", "생활인구 디렉터리" "모델 파일" "스케일러 파일"`
- 요구되는 파라미터는  (파일이름)_app.py 파일을 열어보면 상단 주석에 기재 되어있음
- 반드시 파라미터 경로 확인 후 실행할 것 (디렉터리의 경우 마지막은 /로 끝나야 함)
- 예측의 경우 지난달의 생활인구와 지난년도의 신고건수를 사용하여 산출
- 각 년월별 디렉터리들은 move_file.sh가 만들어냄
- 훈련을 통해 만들어진 모델과 스케일러를 지정하여 예측을 진행함
- 예시 (2023년 1월 8일에 훈련을 진행했다고 가정하에 2023년 1월에 대해 훈련을 하고 싶은 경우)
  - seoul 디렉터리로 이동
  - `python3 predict_test_app.py "/data/safty/2022/" "/data/population/202212/" "/seoul/app/data/ai/predict/model/2023-01-08.pkl" "/seoul/app/data/ai/predict/scaler/2023-01-08.pkl"`