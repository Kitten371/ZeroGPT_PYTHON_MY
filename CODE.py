import sys
import time
import random
from colorama import Fore, Style, init

init()

def typing_effect(text, speed=0.05):
    for char2 in text:
        sys.stdout.write(char2)
        sys.stdout.flush()
        time.sleep(speed)  # Здесь скорость должна быть float-значением
    print()


def blink_text(text, count=3, interval=0.32):
    for _ in range(count):
        sys.stdout.write("\r" + text)  # Показываем текст
        sys.stdout.flush()
        time.sleep(interval)

        sys.stdout.write("\r" + " " * len(text))  # Скрываем текст
        sys.stdout.flush()
        time.sleep(interval)

    sys.stdout.write("\r" + text)  # Оставляем финальный текст видим
    sys.stdout.flush()



time_wait = 0.64
chat = 1
# -----------------------------------------------------------------------------------------------------------------------------------------------------
punctuation = [
    '.', ',',
    '!', '?',
    ':', ';',
    '-', '_',
    '(', ')',
    '[', ']',
    '{', '}',
    '<', '>',
    '+', '=',
    '|',
    '@', '#',
    '$', '%',
    '^', '&',
    '*', '~',
    '`', "'",
    '"',
]
# ------------------------------------------------------------------------------------------------------------------------------------------------
hello = ["Что у тебя сегодня на уме?","В чем сегодня твой фокус?", "Есть идеи над которыми хочешь поработать?","Начнем с чего-нибудь простого или сложного?","Давай обсудим твои сегодняшнии цели." , "Чем займемся сегодня?" , "Какой вопрос беспокоит тебя сейчас?", "Время делиться мыслями и идеями!" , "О чем поговорим сегодня первым делом?" , "Какой вопрос давно ждёт своего решения?" , "О чём сегодня поговорить интереснее всего?" , "Есть идея, которой хочется поделиться прямо сейчас?" ,"Какие мысли занимают тебя сейчас?"]
# --------------------------------
plox = [
    "запрещено",
]
# ------------------------------------------------------------------------
voproc = [
    'привет',
    "как дела",
    "нормально",
    "как тебя зовут"
]
# ----------------------------
plox = [
    "запрещено",
]
# ------------------------------
otvet = [
    'Приветик, как дела?',
    "У меня все отлично! Спасибо,за вопрос.",
    "Хорошо, что это так!",
    "Меня зовут ZeroGPT, а вас?"
]
# ------------------------------
pamat = []
# -----------------------------
smile = ["^^ |" , ":) |" , ":0 |" , "(◕‿◕) |", "✯ |"]

# --------------------------------
print(Style.BRIGHT + Fore.BLACK + random.choice(smile) , random.choice(hello))
print(Style.NORMAL +f"|------------------Чат {chat}-----------------------|" )
# ----------------------------

while True:
   user = input()
   user = user.lower()
   for char in punctuation:
       user = user.replace(char, " ")
   if user in voproc:
       index_otveta = voproc.index(user)
       blink_text(" ✦Generative...✦ ")
       print()
       time.sleep(time_wait)
       otvetAI = otvet[index_otveta]
       typing_effect(">>>>> " + otvet[index_otveta])
       pamat.append(user)
       pamat.append(otvetAI)
   elif user not in voproc and user not in plox and user != '/вывод' and user != "/новый чат":
        blink_text(" ✦Generative...✦ ")
        print()
        time.sleep(time_wait)
        user_vopros = user
        typing_effect(f">>>>> Я еще этого не знаю.Но вы можете обучить меня! Я помню контекст: {user_vopros} .Остается написать ответ!")
        user_otvet = input()
        print(" ✎︎ [ZeroGPT хочет обновить базу данных.Являются ли ваши данные обучения -- не нарушающими нашу политику?] (да или нет)")
        user_podtv = input()
        user_podtv = user_podtv.lower()
        for char in punctuation:
              user_podtv = user_podtv.replace(char, "")
        if "да" in user_podtv :
              blink_text(" Updating servers... ")
              print()
              time.sleep(1.10)
              otvet.append(user_otvet)
              voproc.append(user_vopros)
              blink_text(" ✦Generative...✦ ")
              print()
              time.sleep(time_wait)
              typing_effect(">>>>>" "Я смог обновить сервера,теперь я стал еще чуть-чуть лучше!")
              print(Fore.GREEN + " →✔ [ZeroGPT обновил базу данных,спасибо что улучшаете наш сервис!]" + Style.RESET_ALL)
        else:
              blink_text(" Updating servers... ")
              print()
              time.sleep(1.10)
              print( Fore.RED + "[Updating servers... -- был отклонен.]" + Style.RESET_ALL)
              blink_text(" ✦Generative...✦ ")
              print()
              time.sleep(0.10)
              typing_effect(">>>>>" "Я не смог обновить сервера,мне отключили доступ к ним.")
              print(Fore.RED +" →Х [Попытка ZeroGPT обновить базу данных была отклонена.Так как подтверждение не было распознано.]"+ Style.RESET_ALL )
              break
   elif user in plox:
        blink_text(" ✦Generative...✦ ")
        print()
        print(Fore.RED + " →Х [Иногда ZeroGPT может сгенерировать не подходящий для всех контент.Попробуйте еще раз...]" + Style.RESET_ALL)
        break
   elif user == '/вывод':
       blink_text(" ✦Generative...✦ ")
       print()
       print(Fore.YELLOW + f"! [ Вопрос(-ы): " + Fore.BLACK + f"{', '.join(map(str, voproc))}" + Fore.YELLOW + f", и ответ(-ы): " + Fore.BLACK + f"{', '.join(map(str, otvet))}" + Fore.YELLOW + " ] !")
   elif user == '/новый чат':
        chat += 1
        print()
        print(Style.BRIGHT + Fore.BLACK + random.choice(smile), random.choice(hello))
        print(Style.NORMAL + f"|------------------Чат {chat}-----------------------|")
# юзер = вопрос (от юзера)
# ответАИ = ответИИ
# работа ответов и вопросов:
#
# если есть юзер в вопросах:
# то: определить индекс вопроса
# индекс вопроса = 1
# значит и ответ под индексом 1
# принт ответ[индекс вопроса]

# юзер Привет
# бот Приветик как дела?


