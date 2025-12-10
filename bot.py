import time
import random
import ctypes
import keyboard

MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

def click():
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

print("БОТ ДЛЯ РЫБАЛКИ В TERRARIA")
print("=" * 40)
print("F1 - старт/стоп")
print("F2 - выход")

input("Подготовься в Terraria, потом Enter...")

работает = False
циклы = 0
рыба = 0

def переключить():
    global работает
    работает = not работает
    if работает:
        print("\nБОТ ЗАПУЩЕН")
    else:
        print("\nБОТ ОСТАНОВЛЕН")

def выйти():
    print(f"Итог: {циклы} циклов, {рыба} рыбы")
    keyboard.unhook_all()
    exit(0)

keyboard.add_hotkey('f1', переключить)
keyboard.add_hotkey('f2', выйти)

print("Нажми F1 в Terraria чтобы начать")

try:
    while True:
        if работает:
            циклы += 1
            
            print(f"\nЦикл {циклы}")
            
            print("Заброс...")
            click()
            time.sleep(1.5)
            
            время_ожидания = random.randint(3, 6)
            print(f"Жду {время_ожидания} сек")
            
            for сек in range(время_ожидания):
                if not работает:
                    break
                time.sleep(1)
            
            if работает:
                print("Подсечка...")
                click()
                time.sleep(1)
                
                рыба += 1
                print(f"Рыбы: {рыба}")
                
                time.sleep(random.uniform(1.0, 2.0))
        else:
            time.sleep(0.1)
            
except KeyboardInterrupt:
    print("Аварийная остановка")

keyboard.unhook_all()
print(f"\nЦиклов: {циклы}")
print(f"Рыбы: {рыба}")
input("Нажми Enter...")