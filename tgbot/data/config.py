# - *- coding: utf- 8 - *-
import configparser

# Токен бота
BOT_TOKEN = configparser.ConfigParser()
BOT_TOKEN.read("settings.ini")
BOT_TOKEN = BOT_TOKEN['settings']['token'].strip().replace(' ', '')
BOT_TIMEZONE = "Europe/Moscow"  # Временная зона бота


PATH_DATABASE = "tgbot/data/database.db"  # Путь к БД
PATH_LOGS = "tgbot/data/logs.log"  # Путь к Логам
BOT_VERSION = "3.4"  # Версия бота


# Получение администраторов бота
def get_admins() -> list[int]:
    read_admins = configparser.ConfigParser()
    read_admins.read("settings.ini")

    admins = read_admins['settings']['admin_id'].strip().replace(" ", "")

    if "," in admins:
        admins = admins.split(",")
    else:
        if len(admins) >= 1:
            admins = [admins]
        else:
            admins = []

    while "" in admins: admins.remove("")
    while " " in admins: admins.remove(" ")
    while "\r" in admins: admins.remove("\r")
    while "\n" in admins: admins.remove("\n")

    admins = list(map(int, admins))

    return admins





WHY_WE = f"""
<b>ПОЧЕМУ МЫ?</b>  

Мы — команда профессиональных нотариусов с многолетним опытом работы. Гарантируем юридическую чистоту и оперативное выполнение всех услуг.  

— Работаем с физическими и юридическими лицами  
— Предоставляем полный спектр нотариальных услуг  
— Конфиденциальность и надежность гарантированы  
— Индивидуальный подход к каждому клиенту  
— Оформляем документы в кратчайшие сроки  
— Помогаем разобраться со сложными юридическими вопросами  

Мы всегда рады помочь вам в решении любых нотариальных задач! Свяжитесь с нами, и мы найдем оптимальное решение для вас.  
""".strip()

ABOUT_FIRMS = """
<b>НАШИ НОТАРИАЛЬНЫЕ УСЛУГИ</b>

✅ Заверение копий документов  
✅ Доверенности (генеральные, разовые, на представительство)  
✅ Оформление брачных договоров и соглашений  
✅ Заверение переводов документов  
✅ Оформление завещаний и наследственных договоров  
✅ Подтверждение сделок и контрактов  
✅ Регистрация юридических лиц и оформление учредительных документов  
✅ Ведение нотариального делопроизводства  

📌 **Стоимость услуг уточняйте у наших специалистов.**  
"""
