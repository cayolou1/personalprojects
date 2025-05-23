# -*- coding: utf-8 -*-
"""Project (Cayo)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1imi3ZChIZdHph6jwtd1_YdiHwUXLYwap
"""

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime
from matplotlib import dates
import seaborn as sns
! pip install -q kaggle
from google.colab import files
files.upload()
! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json
! kaggle datasets list
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.linear_model import LinearRegression
url = "/kaggle/input/retail-analysis-with-walmart-sales-data/WALMART_SALES_DATA.csv"
movie_df = pd.read_csv(url)
movie_df.drop_duplicates(inplace=True)
mean_runtime = movie_df['Runtime'].mean()
movie_df['Runtime'] = movie_df['Runtime'].fillna(mean_runtime)
movie_df = movie_df.rename(columns = {"Runtime": "Runtime (min)"})
movie_df = movie_df.astype({"Runtime (min)": "int64"})
movie_df.head()
features = movie_df[['Released_Year', 'IMDB_Rating', 'No_of_Votes', 'Gross']]
label = movie_df['Runtime (min)']
X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=42)
LR = LinearRegression()
LR.fit(X_train, y_train)
pred = LR.predict(X_test)
plt.figure(figsize=(8, 8))
plt.scatter(y_test, pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--k', label="Correct prediction")
plt.xlabel('True Runtime (min)')
plt.ylabel('Predicted Runtime (min)')
plt.title("Real vs Predicted Runtime (min)")
plt.legend()
mean_squared_error(y_test, pred)
r2_score(y_test, pred)