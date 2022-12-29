import pandas as pd


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

'''
input define
colume = ['격자고유번호',count']

'''

def read_data(input_path,encoding):
    df = pd.read_csv(input_path,encoding=encoding)
    df['x'] = df['격자고유번호'].str.slice(start=2, stop=5)
    df['y'] = df['격자고유번호'].str.slice(start=-3)
    df = df.astype({'x': 'int'})
    df = df.astype({'y': 'int'})
    df.insert(4, "visited", False)

    df = df.sort_values(by='count', ascending=False)

    df.insert(5, "index", df.index)
    return df.to_numpy()


def save_data(df,output_path):
    df_ar = pd.DataFrame(df, columns=["격자고유번호", "count", "x", "y", "visited","index"])

    df_ar[['격자고유번호','count']].to_csv(output_path,index=False)


def expand_data(depth,input_path,output_path,encoding):
    df = read_data(input_path,encoding)

    queue = []
    count = 0

    for index, value in enumerate(df):
        if not value[1] == 0:
            queue.append(value)
    while not count == depth:
        temp_queue = []
        while not len(queue) == 0:
            item = queue.pop()
            if not item[4]:
                df[item[5]][4] = True
                for visit_target in range(0, 8):
                    new_y = item[3] + dy[visit_target]
                    new_x = item[2] + dx[visit_target]
                    for index, i in enumerate(df):
                        if (i[3] == new_y) and (i[2] == new_x):
                            df[index][1] = item[1]
                            temp_queue.append(df[index])
                            break
        for e in temp_queue:
            queue.append(e)
        count += 1

    save_data(df,output_path)



