
## 초기 환경 설정 및 확인 사항

***
### 데이터 베이스 설정 및 확인
- database 설정
  - postgresql 설치 
  - postgresql 사용자 생성 (이때, 사용자 권한은 insert,update,delete,select 모두 적용)
  - sql_script 디렉터리 내 6개 sql 파일 확인
  - **DB table 스키마 위치 이름 확인** 
    - 스키마 이름 변경할 경우 (public -> digitalif)  /app/database/query/constants.py내 쿼리문 또한 변경해줘야함.  
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
- 특정 폴더에 일마다 누적
- 형식
  - 단일 파일 `LOCAL_PEOPLE_yyyyMMdd.csv`
***
###  신고 데이터 
- 특정 폴더에 일마다 누적
- 형식 
  - 단일 파일 `POL_01_YYYYMMDD_M.csv `
***
### 그외 확인 사항
- cron 실행 여부 확인
  - `crontab -l`
  - 설정 오류날 경우 ./build/utils/cron.sh 파일을 crontab에 직접 주입
- data directory 확인 
  - /data/population
  - /data/safety
  - *데이터 폴더 경로 수정할 시, "./build/utils/movefile.sh" 파일 내부 설정 경로도 같이 수정할 것

## 실행 방식
- docker file 내부에서 DB ENV 정보에 맞게 수정
- docker build
  - `sudo docker build -t [image-name]  ./`
- docker run (생활인구 신고데이터폴더를 컨테이너에서 접근할 수 있도록 연결)
  - `docker run -it -d -v /data:/data [image]`
- 내부 shell 접속
  - `sudo docker attach [container_id]`

***
## AI
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
  - 최종적으로 N+1월에 대한 예측 데이터가 만들어짐
  - 위험 지수는 N+1월에 대한 예측을 하기 위해 N-1월의 생활인구와 작년 112신고 건수를 사용함
  - 예시
    - 2023년도 3월 예측을 진행할 경우, 요구 데이터는 다음과 같음
      - 훈련: 2022년도 12월 생활인구, 시설데이터, 2022년도 112 신고 건수 데이터
      - 테스트: 2023년도 1월 생활인구, 시설데이터, 2022년도 112 신고 건수 데이터

***
## 프로그램 별 요구 데이터 정리
  - **관광지 경찰대** ->일일 112 신고 건수, 관광지 격자 맵 데이터(기보유), 서울시 격자 맵(기보유)
  - **한강 경찰대** ->일일 112 신고 건수, 한강 격자 맵 데이터(기보유), 서울시 격자 맵(기보유)
  - **지하철 경찰대** ->일일 112 신고 건수, 지하철 격자 맵 데이터(기보유), 서울시 격자 맵(기보유)
  - **혼잡도** -> 한달 112 신고 건수, 한달 생활인구, 혼잡 지역 격자 맵 데이터(기보유),서울시 집계구 맵(기보유),서울시 격자 맵(기보유)
  - **위험지수(산출용)** -> 1년 112 신고 건수, 한달 생활인구(N-1), 시설 데이터
  - **공간회귀 위험지수** -> 1년 112 신고 건수, 한달 생활인구(N-1), 시설 데이터
  - **범죄 모델 훈련** -> 1년 112 신고 건수, 한달 생활인구(N-2), 시설 데이터
  - **범죄 예측** -> 1년 112 신고 건수, 한달 생활인구(N-1), 시설 데이터, 모델