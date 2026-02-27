from predictor import predict_duration

# imitating django-models
class DummyDetail:
    prep_time = 12
    piece_time = 3
    length = 100.0
    width = 40.0
    height = 20.0
    material = "steel"

class DummyMachine:
    id = 1  # ID machine that was in learned model

detail = DummyDetail()
machine = DummyMachine()

predicted_time = predict_duration(detail, machine)
print(f"Предсказанное время обработки: {predicted_time} минут")