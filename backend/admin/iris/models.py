from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from admin.common.models import ValueObject
from admin.tensor.models import Perceptron


class Iris(object):
    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/iris/data/'

    def base(self):
        np.random.seed(0)
        iris = load_iris()
        iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
        # print(f'아이리스 데이터 구조: {iris_df.head(2)} \n {iris_df.columns}')
        '''
        ['sepal length (cm)', 꽃받침
        'sepal width (cm)', 꽃받침
        'petal length (cm)', 꽃잎
        'petal width (cm)', 꽃잎
        ]
        '''
        iris_df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        # print(f'품종 추가된 아이리스 데이커 구조: {iris_df.head(2)}\n {iris_df.columns}')
        ''' 'sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)' '''
        iris_df['is_train'] = np.random.uniform(0, 1, len(iris_df)) <= 0.75  # train set 75%
        train, test = iris_df[iris_df['is_train'] == True],\
                      iris_df[iris_df['is_train'] == False]
        features = iris_df.columns[:4]  # 0 ~ 3까지 feature 추출
        # print(f'아이리스 features 값: {features} \n')
        '''
        아이리스 features 값: Index(['sepal length (cm)', 'sepal width (cm)', 
                                    'petal length (cm)', 'petal width (cm)'], dtype='object')
        '''
        y = pd.factorize(train['species'])[0]
        # print(f'아이리스 y 값: {y}')  # 총 3종류의 품종이 있다
        '''
        아이리스 y 값: [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
                     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
                     1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                     2 2 2 2 2 2 2]
        '''
        # Learning
        clf = RandomForestClassifier(n_jobs=2, random_state=0)   # n_jobs = epoch
        clf.fit(train[features], y)
        # print(clf.predict_proba(test[features])[0:10])
        '''
        # 0    1    2번
        [[1.   0.   0.  ]
         [1.   0.   0.  ]
         [1.   0.   0.  ]
         [1.   0.   0.  ]
         [1.   0.   0.  ]
         [0.95 0.05 0.  ]  # 애매하긴 한데 맞춤
         [1.   0.   0.  ]
         [0.99 0.01 0.  ]
         [1.   0.   0.  ]
         [1.   0.   0.  ]]
        '''
        # accuracy
        preds = iris.target_names[clf.predict(test[features])]
        print(f'아이리스 crosstab 결과: {preds[0:5]} \n')
        '''
        아이리스 crosstab 결과: ['setosa' 'setosa' 'setosa' 'setosa' 'setosa']
        '''
        # crosstab
        temp = pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Prediced Species'])
        print(f'아이리스 crosstab 결과: {temp} \n')
        '''
        # 0:setosa  1:versicolor  2:virginica
        아이리스 crosstab 결과: Prediced Species  setosa  versicolor  virginica
                              Actual Species
                              setosa                13           0          0
                              versicolor             0           5          2
                              virginica              0           0         12
        '''
        # feature 별 중요도
        print(list(zip(train[features], clf.feature_importances_)))
        ''' # 상관관계
        [('sepal length (cm)', 0.08474010289429795), -- 꽃받침
         ('sepal width (cm)', 0.022461263894393204), 
         ('petal length (cm)', 0.4464851467243143),  -- 꽃잎
         ('petal width (cm)', 0.4463134864869946)]
        '''

    def advanced(self):
        iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                           header=None)
        # 0:setosa  1:versicolor
        iris_mini = iris.iloc[0:100, 4].values
        y = np.where(iris_mini == 'Iris-setosa', -1, 1)  # 2진 분류는 -1과 1
        X = iris.iloc[0:100, [0,2]].values               # X값 : 확률변수로 사용?
        clf = Perceptron(eta = 0.1, n_iter=10)
        # self.draw_scatter(X)
        # self.draw_decision_regions(X, y, classifier=clf,  resolution=0.02)

    def draw_scatter(self, X):
        plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
        plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
        plt.xlabel('sepal length[cm]')
        plt.ylabel('petal length[cm]')
        plt.legend(loc='upper left')
        plt.savefig(f'{self.vo.context}iris_scatter.png')

''' # 시도했지만 실패 ㅜ
    def draw_decision_regions(self, X, y,classifier, resolution=0.02):    # 경계선(오류값들을 보여줌) / 값이 오는 파라미터는 맨 마지막으로
        # 마커와 컬러맵을 설정합니다
        markers = ('s', 'x', 'o', '^', 'v')
        colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(y))])

        # 결정 경계를 그립니다
        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        """
        numpy 모듈의 arrange 함수는 반열린구간 [start, stop) 에서
        step 의 크기만큼 일정하게 떨어져 있는 숫자들을
        array 형태로 반환하는 함수
        meshgrid 함수는 사각형 영역을 구성하는
        가로축의 점들과 세로축의 점을
        나타내는 두 벡터를 인수로 받아서
        이 사각형 영역을 이루는 조합을 출력한다.
        결과는 그리드 포인트의 x 값만을 표시하는 행렬과
        y 값만을 표시하는 행렬 두 개로 분리하여 출력한다
        """
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                               np.arange(x2_min, x2_max, resolution))
        Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
        Z = Z.reshape(xx1.shape)
        plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())

        # 샘플의 산점도를 그립니다
        for idx, cl in enumerate(np.unique(y)):
            plt.scatter(x=X[y == cl, 0],
                        y=X[y == cl, 1],
                        alpha=0.8,
                        c=colors[idx],
                        marker=markers[idx],
                        label=cl,
                        edgecolor='black')
        plt.xlabel('sepal length [cm]')
        plt.ylabel('petal length [cm]')
        plt.legend(loc='upper left')
        plt.savefig(f'{self.vo.context}iris_decision_regions.png')
'''

