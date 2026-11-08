total_seconds=int(input("Seconds: "))
while True:
    print("How do you want to print the duration?\n1. _ h _ min _ s\n2. __:__:__")
    value=int(input("Choose 1 or 2: "))
    match value:
        case 1|2:
            result=value
            break
        case _:
            print("Invalid number")

def h_min_sec(seconds):
    total_minutes=seconds//60
    total_hours=total_minutes//60
    total_seconds_left=total_seconds%60
    total_minutes_left=total_minutes%60
    if result==1:
        print(f"{total_hours} h {total_minutes_left} min {total_seconds_left} s")
    else:
        print(f"{total_hours:02d}:{total_minutes_left:02d}:{total_seconds_left:02d}")
h_min_sec(total_seconds)