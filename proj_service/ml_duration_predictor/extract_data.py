import pandas as pd
from schedule.models import Schedule
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_service.settings')
django.setup()

def extract_data():
    data = []

    schedules = Schedule.objects.select_related('machine', 'order_detail', 'order_detail__detail')

    for s in schedules:
        if not s.actual_start_time or not s.actual_end_time:
            continue

        detail = s.order_detail.detail

        duration_minutes = (s.actual_end_time - s.actual_start_time).total_seconds() / 60

        data.append({
            'prep_time': detail.prep_time,
            'piece_time': detail.piece_time,
            'length': detail.length,
            'width': detail.width,
            'height': detail.height,
            'material': detail.material,
            'machine_id': s.machine.id,
            'actual_duration': duration_minutes,
        })

    df = pd.DataFrame(data)
    df.to_csv('duration_training_data.csv', index=False)
    print("Файл сохранён: duration_training_data.csv")

if __name__ == "__main__":
    extract_data()