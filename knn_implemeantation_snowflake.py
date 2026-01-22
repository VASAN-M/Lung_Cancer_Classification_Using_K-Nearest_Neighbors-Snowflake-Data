from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import snowflake.connector
conn=snowflake.connector.connect(
    user='<Username>',
    password='<Password>',
    account='<Account_ID>',
    database='<Database_Name>',
    schema='<Scheme_Name>',
    warehouse='<Warehouse_Name>'
)
query='SELECT*FROM "CANCER" LIMIT 5'
df=pd.read_sql(query,conn)
conn.close
print(df.head())

for col in df.columns:
  print(df[col].name,df[col].unique())

le=LabelEncoder()
for col in df.columns:
  if df[col].name=='AGE':
    continue
  df[col]=le.fit_transform(df[col])
for col in df.columns:
  print(df[col].name,df[col].unique())


X = df.drop('LUNG_CANCER', axis=1)
y = df['LUNG_CANCER']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

knn_model = KNeighborsClassifier(n_neighbors=3)

knn_model.fit(X_train, y_train)

y_pred = knn_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"K-Nearest Neighbors Classifier Accuracy: {accuracy:.2f}")