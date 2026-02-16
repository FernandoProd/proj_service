import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError
import joblib
import os

#Путь к CSV-файлу
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data.csv')

#Загрузка данных
df = pd.read_csv(DATA_PATH)

#Кодировка 'material' и 'machine_id'
le_material = LabelEncoder()
df['material'] = le_material.fit_transform(df['material'])

le_machine = LabelEncoder()
df['machine_id'] = le_machine.fit_transform(df['machine_id'])

#Входные признаки (X) и целевая переменная (y)
X = df[['prep_time', 'piece_time', 'length', 'width', 'height', 'material', 'machine_id']]
y = df['actual_duration_minutes']

#Масштабирование входных данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#Разделение на train и test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=15)

#Создание модели
model = Sequential()
model.add(Dense(32, input_dim=X.shape[1], activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='linear'))  # Одна выходная переменная — время

#Компиляция и обучение
model.compile(optimizer=Adam(learning_rate=0.01), loss=MeanSquaredError(), metrics=['mae'])
model.fit(X_train, y_train, epochs=50, batch_size=8, validation_split=0.2)

#Сохранение модели и препроцессоров
model.save(os.path.join(os.path.dirname(__file__), 'duration_model.h5'))
joblib.dump(scaler, os.path.join(os.path.dirname(__file__), 'scaler.pkl'))
joblib.dump(le_material, os.path.join(os.path.dirname(__file__), 'material_encoder.pkl'))
joblib.dump(le_machine, os.path.join(os.path.dirname(__file__), 'machine_encoder.pkl'))

print("Модель успешно обучена и сохранена.")