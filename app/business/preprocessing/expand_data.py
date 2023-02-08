# -*- coding: utf-8 -*-

dx = [-1, -1, 0, 1, 1, 1, 0, -1]  # 8 directions
dy = [0, 1, 1, 1, 0, -1, -1, -1]  # 8 directions

'''
dataframe column info            
0: 격자고유번호
1: count
2: x coordinate
3: y coordinate
4: visited
5: df index
'''


def expand_data(depth, df):
    df = preprocess(df)

    queue = []
    count = 0  # depth count

    for index, value in enumerate(df):
        if not value[1] == 0:
            queue.append(value)

    while not count == depth:
        temp_queue = []
        while not len(queue) == 0:

            item = queue.pop()
            if not item[4]:  # ==  visited
                # 방문처리
                df[item[5]][4] = True  # == visited[index]

                # 8방향의 격자에 대해서 확장여부를 판단함
                for visit_target in range(0, 8):
                    # 한 방향의 공간정보(x,y)를 알아낸 뒤
                    new_y = item[3] + dy[visit_target]  # == y[index+8 directions]
                    new_x = item[2] + dx[visit_target]  # == y[index+8 directions]

                    for index, i in enumerate(df):  # 해당 공간정보를 가진 row가 전체 df 내에서 어디에 존재하는지 탐색함
                        if (i[3] == new_y) and (i[2] == new_x):
                            df[index][1] = item[1]  # 발견했을경우 시설정보를 확장시켜줌
                            temp_queue.append(df[index])  # 다음 깊이 때 탐색 시키기 위해 미리 저장해둠
                            break
        for e in temp_queue:  # 탐색을 모두 마치면 다음 깊이에서 탐색할 격자들을 준비시킴
            queue.append(e)
        count += 1

    import pandas as pd
    df_ar = pd.DataFrame(df, columns=["격자고유번호", "count"])
    return df_ar[['격자고유번호', 'count']]


def preprocess(df):
    df['격자고유번호'] = df['격자고유번호'].map(lambda x: x[-6:])
    df['x'] = df['격자고유번호'].str.slice(start=0, stop=3)
    df['y'] = df['격자고유번호'].str.slice(start=-3)
    df = df.astype({'x': 'int'})  # convert type to int
    df = df.astype({'y': 'int'})  # convert type to int

    df.insert(4, "visited", False)
    df = df.sort_values(by='count', ascending=False)  # descending order count
    df.insert(5, "index", df.index)
    return df.to_numpy()
