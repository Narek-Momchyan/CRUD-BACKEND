import json
import os
import django

# 1. Կարգավորում ենք Django-ի միջավայրը (Environment)
# Այստեղ 'base.settings'-ը քո հիմնական կարգավորումների ֆայլն է
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')

# Սա ակտիվացնում է Django-ն, որպեսզի կարողանանք օգտագործել մեր մոդելները
django.setup()

# 2. Ներմուծում ենք մեր Ստեղծած մոդելը (App-ի անունը polls է)
from polls.models import Student

def run():
    # 3. Բացում ենք db.json ֆայլը՝ որպես կարդալու ենթակա ֆայլ ('r')
    with open('db.json', 'r', encoding='utf-8') as file:
        # JSON-ը դարձնում ենք Python-ի բառարան (Dictionary)
        data = json.load(file)
        
        # Վերցնում ենք միայն 'students' զանգվածը
        students_list = data.get('students', [])

        # 4. Ցիկլով (loop) պտտվում ենք յուրաքանչյուր ուսանողի վրայով
        for item in students_list:
            
            # Ստեղծում ենք նոր գրառում բազայում
            # Եթե email-ով արդեն կա, որ error չտա, օգտագործում ենք get_or_create
            student, created = Student.objects.get_or_create(
                email=item['email'], # Ստուգում ենք email-ով
                defaults={
                    'fullName': item['fullName'],
                    'facultet': item['facultet'],
                    'age': int(item['age']), # տարիքը դարձնում ենք թիվ
                    'phone': item['phone'],
                    'about': item['about']
                }
            )
            
            if created:
                print(f"✅ Ավելացվեց նոր ուսանող: {item['fullName']}")
            else:
                print(f"⚠️ Այս ուսանողն արդեն կա բազայում: {item['fullName']}")

    print("🎉 Տվյալների բեռնումն ավարտվեց։")


if __name__ == '__main__':
    run()