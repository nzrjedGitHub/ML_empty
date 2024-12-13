import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Крок 1. Завантаження та очищення даних
df = pd.read_csv('titanic.csv')

print(df.head())