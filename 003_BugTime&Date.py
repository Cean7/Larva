import datetime

print("Bug Clock")
print("Press Enter to check the time. To quit, type 'q'. \n")

while True:
    user = input(">")
    if user.lower() == 'q':
        print("Goodbye, sleepy bug!")
        break
    now = datetime.datetime.now()
    print(f"{now.strftime('%A, %B %d, %Y')}")
    print(f"{now.strftime('%I:%M:%S %p')}\n")