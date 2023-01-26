import pandas as pd



# 8방향 인접 공간들에 대한 정보
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


'''
df 컬럼 정보
0: 격자고유번호
1: count
2: x (격자고유번호를 통해 산출함)
3: y (격자고유번호를 통해 산출함)
4: visited (방문처리)
5: index (df 내 에서 몇번째 위치에 있는지)
'''

def preprocess(df):
    #csv 파일 읽은 뒤, 격자고유번호의 형태를 바탕으로 x공간정보와 y공간정보를 산출해낸다.
    df['격자고유번호']=df['격자고유번호'].map(lambda x: x[-6:])
    df['x'] = df['격자고유번호'].str.slice(start=0, stop=3)
    df['y'] = df['격자고유번호'].str.slice(start=-3)
    df = df.astype({'x': 'int'})
    df = df.astype({'y': 'int'})

    # 방문처리 인덱스를 추가한다. (이미 확장 알고리즘을 통해 적용된 구역이 다시 수정될 수 있기 때문에 해당 flag를 바탕으로 위와 같은 예외를 처리한다.)
    df.insert(4, "visited", False)

    # 낮은 시설 개수 값이 먼저 들어올 경우 높은 시설 개수 값으로 교체하지 못하기 때문에 사전에 높은 시설 개수 순으로 처리한다
    df = df.sort_values(by='count', ascending=False)

    # 인덱스 정보를 추가한다.
    df.insert(5, "index", df.index)
    return df.to_numpy()





def expand_data(depth,df):
    df = preprocess(df)

    #확장시킬 시설정보를 가지고 있는 데이터
    queue = []
    #어느정도 깊이까지 탐색할지를 저장해둔 변수
    count = 0

    #시설개수가 하나이상 있는 로우들을 저장함
    for index, value in enumerate(df):
        if not value[1] == 0:
            queue.append(value)

    # 입력으로 주어진 depth 까지 확장을 완료하였으면 멈춘다
    while not count == depth:
        temp_queue = []

        # 현재 깊이의 모든 시설 탐색이 완료될때까지 반복
        while not len(queue) == 0:
            #시설을 하나 꺼냄
            item = queue.pop()
            # 해당 아이템을 방문하지 않았다면
            if not item[4]:
                # 방문처리
                df[item[5]][4] = True

                # 8방향의 격자에 대해서 확장여부를 판단함
                for visit_target in range(0, 8):
                    # 한 방향의 공간정보(x,y)를 알아낸 뒤
                    new_y = item[3] + dy[visit_target]
                    new_x = item[2] + dx[visit_target]

                    # 해당 공간정보를 가진 row가 전체 df 내에서 어디에 존재하는지 탐색함
                    for index, i in enumerate(df):
                        if (i[3] == new_y) and (i[2] == new_x):
                            # 발견했을경우 시설정보를 확장시켜줌
                            df[index][1] = item[1]
                            # 다음 깊이 때 탐색 시키기 위해 미리 저장해둠
                            temp_queue.append(df[index])
                            break
        #탐색을 모두 마치면 다음 깊이에서 탐색할 격자들을 준비시킴
        for e in temp_queue:
            queue.append(e)
        count += 1


    df_ar = pd.DataFrame(df, columns=["격자고유번호", "count"])
    return  df_ar[['격자고유번호','count']]




