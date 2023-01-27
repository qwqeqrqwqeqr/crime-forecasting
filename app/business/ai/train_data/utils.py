# -*- coding: utf-8 -*-

from functools import reduce
import pandas as pd



# 격자별로 데이터를 하나로 통합한다
def concat_grid_data(dfs,map_key):
    return reduce(lambda left, right: pd.merge(left, right, on=map_key), dfs)


# 시설정보 df들을 리스트 묶음으로 변환함
def grid_df_to_list(df_list):
    dfs = []
    for i in range(0, len(GRID_NAME_LIST)):
        df = df_list[i]
        df = df.rename(columns={'count': GRID_NAME_LIST[i]})
        dfs.append(df)
    return dfs


GRID_NAME_LIST = [
    '112신고데이터', '생활인구', 'CCTV', '보안등', '편의점', '여성안심지킴이집', '여성안심택배함', '아동안전지킴이시설물', '인터넷컴퓨터게임시설', '노래연습장', '단란주점',
    '유흥주점', '목욕장업', '숙박업', '지구대/파출소', '치안센터', '접수경찰서']