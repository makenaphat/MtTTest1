import random

secret_number = random.randint(1, 10)
attempts = 0

print("=== เกมทายตัวเลข (1-10) ===")

while True:
    guess = int(input("ทายตัวเลข: "))
    attempts += 1

    if guess < secret_number:
        print("น้อยเกินไป! ลองใหม่นะ")
    elif guess > secret_number:
        print("มากเกินไป! ลองใหม่นะ")
    else:
        print(f"ถูกต้อง! คุณทายถูกใน {attempts} ครั้ง")
        break
        