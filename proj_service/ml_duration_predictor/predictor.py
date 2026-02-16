import numpy as np
import joblib
from tensorflow.keras.models import load_model
import tensorflow.keras.losses as losses
import os



# Пути к сохранённым файлам
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, 'duration_model.h5')
SCALER_PATH = os.path.join(BASE_DIR, 'scaler.pkl')
MATERIAL_ENCODER_PATH = os.path.join(BASE_DIR, 'material_encoder.pkl')
MACHINE_ENCODER_PATH = os.path.join(BASE_DIR, 'machine_encoder.pkl')

# Загрузка модели и препроцессоров
model = load_model(MODEL_PATH, custom_objects={'mse': 'mean_squared_error'})
scaler = joblib.load(SCALER_PATH)
le_material = joblib.load(MATERIAL_ENCODER_PATH)
le_machine = joblib.load(MACHINE_ENCODER_PATH)

def predict_duration(detail, machine):
    """
    Предсказать длительность обработки детали на конкретном станке.

    Аргументы:
    - detail: объект Detail (или OrderDetail.detail)
    - machine: объект Machine

    Возвращает:
    - float — предсказанное время в минутах
    """

    try:
        material_encoded = le_material.transform([detail.material])[0]
        machine_encoded = le_machine.transform([machine.id])[0]
    except Exception as e:
        print(f"Ошибка кодирования: {e}")
        return None

    # Формируем вектор признаков
    features = np.array([[
        detail.prep_time,
        detail.piece_time,
        detail.length,
        detail.width,
        detail.height,
        material_encoded,
        machine_encoded,
    ]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled, verbose=0)[0][0]

    return round(prediction, 2)