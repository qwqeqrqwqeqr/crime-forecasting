
## Crime Forecasting
- 범죄 예측 지도 프로젝트입니다.

### 서버 가상환경 연결 
1. preferences -> project -> Python Interpreter -> add Interpreter - ssh 
2. set ssh config
   1. **existing**
   2. **Host** 121.131.185.164
   3. **Port** 10022
   4. **UserName** ncyc-admin
   5. **Location** /home/ncyc-admin/anaconda3/envs/crime-forecasting/bin/python3.9
   6. **Sync-folders**  Project root -> /home/ncyc-admin/crime-forecasting

### conda 기반 필수 패키지 설치

`conda install --file packagelist.txt`