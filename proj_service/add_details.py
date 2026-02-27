import pandas as pd
import os
import django
from django.db.utils import IntegrityError

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_service.settings')
django.setup()

from orders.models import Detail
from machines.models import Machine


def load_details():
    try:
        # Чтение CSV с разделителем ';'
        df = pd.read_csv('detail.csv', sep=';', encoding='utf-8')
        print(f"Найдено {len(df)} записей для обработки")

        # Основной цикл обработки
        for index, row in df.iterrows():
            try:
                # Создаем деталь без привязки станков
                detail = Detail.objects.create(
                    number=row['number'],
                    name=row['name'],
                    material=row['material'],
                    length=row['length'],
                    width=row['width'],
                    height=row['height'],
                    prep_time=row['prep_time'],
                    piece_time=row['piece_time']
                )

                # Добавляем станки (если нужно)
                machine_name = row['machines']
                if machine_name and pd.notna(machine_name):
                    machine, created = Machine.objects.get_or_create(name=machine_name.strip())
                    detail.machines.add(machine)

                print(f"Добавлено: {row['number']} - {row['name']}")

            except IntegrityError:
                print(f"Пропущено (дубликат): {row['number']}")
            except Exception as e:
                print(f"❌ Ошибка в строке {index + 2}: {str(e)}")

    except FileNotFoundError:
        print("Файл 'detail.csv' не найден!")
    except Exception as e:
        print(f"Критическая ошибка: {str(e)}")


if __name__ == '__main__':
    load_details()
    print("Загрузка завершена")