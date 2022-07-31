import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 레시피 파일 로딩
def load_data():
    path = './data/db/recipe_final.xlsx'
    df = pd.read_excel(path)
    return df


# cosine-similarity 유사도에 가중치 계산
def scaled_score(score):
    return round(((2 * score) - (score)**2) ** 0.5 , 4) * 100


# tf-idf 함수 만들기
def tfidf_make(df):
    # 1글자 재료도 인식할 수 있도록 처리
    tfidf = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
    tfidf_matrix = tfidf.fit_transform(df['재료'])
    return tfidf_matrix


# 겹치는 재료 show
def show_ingredients(my, menu):
    tmp = []
    for m in menu:
        intersect_ingre = ','.join(list(set(my).intersection(m)))
        if len(intersect_ingre) == 0:
            tmp.append('--겹치는 재료 없음--')
        else:
            tmp.append(intersect_ingre)

    intersects = pd.Series(tmp, name='겹치는 재료')
    return intersects


# 메뉴 추천 함수
def get_recommendations(a, title, df):
    df = df.append({'이름': '메뉴', '재료': a}, ignore_index=True)
    # TF-IDF matrix 생성
    tfidf_matrix = tfidf_make(df)

    # Cosine Similarity matrix 생성
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # title과 비교할 cosine 유사도 계산
    indices = pd.Series(df.index, index=df['이름']).drop_duplicates()
    idx = indices[title]
    
    # 코사인 유사도 큰 수별로 순위 매기기
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 상위 10개 추출(자신 제외)
    top_scores = sim_scores[1:11]

    recipe_indices = [i[0] for i in top_scores]
    scores = pd.Series([scaled_score(i[1]) for i in top_scores], name='점수')

    result = df.iloc[recipe_indices].reset_index(drop=True)

    # 겹치는 재료 변환
    menu = [res.split(',') for res in result['재료']]
    my_ingredient = [i.strip() for i in a.split(',')]
    intersect_ingre = show_ingredients(my_ingredient, menu)
    result = pd.concat([result, intersect_ingre], axis=1)
    result = pd.concat([result, scores], axis=1)

    return result