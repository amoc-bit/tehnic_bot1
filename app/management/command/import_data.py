import requests
from django.core.management.base import BaseCommand
from django.core.files.temp import NamedTemporaryFile
from .models import All_tecnic
import pandas as pd

class Command(BaseCommand):
    help = 'Import data from XLSX file'

    def handle(self, *args, **options):
        url = 'https://www.ileasing.ru/scripts/generate_xlsx_list.php'
        
        # Загрузка файла
        response = requests.get(url)
        if response.status_code != 200:
            self.stderr.write(f'Error downloading file: HTTP {response.status_code}')
            return

        # Сохраняем во временный файл
        with NamedTemporaryFile(suffix='.xlsx') as tmp:
            tmp.write(response.content)
            tmp.flush()

            # Чтение XLSX файла
            try:
                df = pd.read_excel(tmp.name)
            except Exception as e:
                self.stderr.write(f'Error reading XLSX file: {str(e)}')
                return

            # Преобразование данных и сохранение в БД
            counter = 0
            for index, row in df.iterrows():
                try:
                    All_tecnic.update_or_create(
                        contract_number=row['Номер договора'],
                        defaults={
                            'client_name': row['Имя клиента'],
                            'amount': row['Сумма'],
                            'start_date': row['Дата начала'],
                            'end_date': row['Дата окончания'],
                        }
                    )
                    counter += 1
                except Exception as e:
                    self.stderr.write(f'Error processing row {index}: {str(e)}')

            self.stdout.write(self.style.SUCCESS(f'Successfully imported/updated {counter} contracts'))
