import tkinter as tk #Импортируем бибилиотеку для GUI
from datetime import datetime, timedelta #Для работы с датами и временем
from dateutil import relativedelta #удобный подсчёт разницы дат

#Константа - дата и время выхода фильма Интерстеллар
INTERSTELLAR_DATE = datetime(2014, 11, 5, 0, 0, 0,)
#Множитель времени планеты Миллер (1 час = 7 земных лет)
#Переведём 7 земных лет в часы: 7 лет * 365.25 дней/год *24 часа = ~61332 ч
#Значит 1 час Миллер соответствует 61332 земным часам
MILLER_TIME_MULTIPLIER = 1 / 61332

#Функция обновления времени в окне
def update_time():
    now = datetime.now() #Получаем текущее земеное время
    earth_time_str=now.strftime("%H:%M:%S") #Форматируем земное время в строку в формате часы,минуты,секунды
    
    #Вычисляем точное прошедшее время с момента выхода фильма в годах,месяцах,днях с момощью библиотеки релативидельта
    diff = relativedelta.relativedelta(now, INTERSTELLAR_DATE)
    #Формируем строку, которая будет показывать, сколько точно прошло времени
    elapsed_str = (f'На земле прошло {diff.years} лет, {diff.months} месяцев, '
                   f'{diff.days} дней, {now.hour} часов')
    
    #Считаем сколько прошло времени с выхода фильма
    delta_earth = now - INTERSTELLAR_DATE
    #Переводим разницу времени в количество часов
    delta_earth_hours=delta_earth.total_seconds() / 3600 #секунд в часе
    #Рассчитываем время планеты Миллер
    delta_miller_hours=delta_earth_hours * MILLER_TIME_MULTIPLIER
    #Конвертируем часы Милллера обратно в часы:минуты:секунды
    miller_hours = int(delta_miller_hours)%24
    miller_minutes = int((delta_miller_hours * 60))%60
    miller_seconds=int((delta_miller_hours * 3600))%60
    
    miller_time_str=f'{miller_hours:02}:{miller_minutes:02}:{miller_seconds:02}'
    
    #Обновляем текст меток в интерфейсе
    elapsed_label.config(text=elapsed_str) #сообщение о прошедшем времени с даты выхода фильма
    earth_label.config(text=f'Earth time: {earth_time_str}')
    miller_label.config(text=f'Miller time: {miller_time_str}')
    
    #Показываем эквивалент 1 минуты Миллера в земных днях и месяцах
    minute_in_days=42.6
    minute_in_months=1.4
    minute_text=f'1 minute ={minute_in_days} earth days or {minute_in_months} earth months'
    minute_equiv_label.config(text=minute_text)

    #Миллеровская секунда - это ожин земной час умноженный на миллер_тайм_мультиплеер
    #Обратное время секунда Миллера в земных секундах
    seconds_per_miller_sec=3600*(1/MILLER_TIME_MULTIPLIER)
    #Вычисляем сколько осталось земных секунд до следующей смены секунды Миллера 
    passed_miller_seconds=(delta_miller_hours*3600)%1
    remaining_miller_seconds = 1 - passed_miller_seconds
    remaining_earth_seconds = remaining_miller_seconds * seconds_per_miller_sec
    remaining_earth_hours = remaining_earth_seconds / 3600
    
    warning_text=f'Next Miller second change in approx {remaining_earth_hours:.2f} Earth hours'
    warning_label.config(text=warning_text)
    
    #Запускаем эту функцию снова через 1000 мс (1 секунда)
    root.after(1000, update_time)

#Создаем главное окно приложения
root = tk.Tk()
root.title('Часы Земли и планеты Миллер')
root.geometry('450x350') #устанавливаем фиксированнй размер окна для удобства позиционирования

#Метки для отображения времени Земли и планеты Миллер
earth_label=tk.Label(root, font=('Arial', 24))
earth_label.pack(pady=10)

miller_label=tk.Label(root, font=('Arial', 24))
miller_label.pack()

#Создаём метку для фразы с прошедшим временем (наш основной текст)  
elapsed_label=tk.Label(root, font=('Arial', 14), anchor='w', justify='left')
elapsed_label.place(x=10, y=280)
# Новая метка под elapsed_label с информацией о соотношении минут
minute_equiv_label = tk.Label(root, font=('Arial', 12), fg='gray', anchor='w', justify='left')
minute_equiv_label.place(x=10, y=310)
# Ещё одна метка с предупреждением на английском
warning_label = tk.Label(root, font=('Arial', 12), fg='red', anchor='w', justify='left')
warning_label.place(x=10, y=335)


#Запускаем обновление времени
update_time()

#Запускаем главный цикл окна
root.mainloop()

    
    
    
    
    