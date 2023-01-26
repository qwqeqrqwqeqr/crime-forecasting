
## 스마트 치안 프로젝트

***
### 초기 환경 설정
docker run -it seoul
***
### 데이터 베이스 설정
- database 설정
  - postgresql 설치 
  - postgresql 사용자 생성 (이때, 사용자 권한은 insert,update,delete,select 모두 적용)
  - sql_script 디렉터리 내 6개 sql 파일 확인
  - app/database/config/database.ini DB 정보에 맞게 수정
***
### 필수 데이터 확인
- 지도 데이터 (./app/data/map)
  - grid_area.csv => 집계구 격자 데이터
  - grid_hangang.csv => 한강 격자 데이터
  - grid_subway.csv => 지하철 격자 데이터
  - grid_tourist.csv => 관광지 격자 데이터
  - grid.geojson => 격자 데이터
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
  - 2021년 112신고 데이터(./app/data/origin/report) **[변경예정]**
  - 2021년 데이터(./app/data/origin/life_population) **[변경예정]**
    - LOCAL_PEOPLE_202101.zip 
    - LOCAL_PEOPLE_202104.zip  
    - LOCAL_PEOPLE_202107.zip 
    - LOCAL_PEOPLE_202110.zip 
    - LOCAL_PEOPLE_202102.zip 
    - LOCAL_PEOPLE_202105.zip  
    - LOCAL_PEOPLE_202108.zip
    - LOCAL_PEOPLE_202111.zip 
    - LOCAL_PEOPLE_202103.zip 
    - LOCAL_PEOPLE_202106.zip 
    - LOCAL_PEOPLE_202109.zip  
    - LOCAL_PEOPLE_202112.zip 
***
###  생활인구 추출
- 각 디렉터리 별로 생활인구 zip 파일 압축을 해제
- ex : `unzip LOCAL_PEOPLE_202112.zip -d [path]/dec`
***


### 실행 (혼잡도,위험지수 2023-01-20 추가 예정)
- 리눅스 작업 스케쥴러 프로그램 사용 (crontab)
- `0 [시간대] * * *  [absolute_path]/tourist_app.sh`
- `0 [시간대] * * *  [absolute_path]/subway_app.sh`
- `0 [시간대] * * *  [absolute_path]/hangang_app.sh`
- `0 [시간대] * * *  [absolute_path]/report_app.sh`


***
### 테스트 (2023-01-20 추가 예정)
***