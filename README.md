
### 초기 환경 설정

***
### 데이터 베이스 설정
- database 설정
  - postgresql 설치 
  - postgresql 사용자 생성 (이때, 사용자 권한은 insert,update,delete,select 모두 적용)
  - sql_script 디렉터리 내 6개 sql 파일 확인
  - app/database/config/database.ini DB 정보에 맞게 수정 (수정 예정)
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
###  생활인구 
- 특정 폴더에 ~~일마다~~ 누적
- 형식
  - 단일 파일 `LOCAL_PEOPLE_yyyyMMdd.csv`
  - 월별 파일 `LOCAL_PEOPLE_yyyyMM.zip`
***
###  신고 데이터 
- 특정 폴더에 일마다 누적
- 형식 
  - 단일 파일 `POL_01_YYYYMMDD_M.csv `
***
### 실행 방식