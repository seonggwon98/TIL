import random

print("3번 이기시면 최종승리하는 가위바위보 게임입니다.")
user_count = 0
com_count = 0
while user_count or com_count < 4:
    user = int(input("가위 = 1 바위 = 2 보 = 3 중 입력해 주세요: ")) # 입력 받기
    if user == 1:
        print("가위")
    elif user == 2:
        print("바위")
    elif user == 3:
        print("보")
    else:
        print("정해진 값을 입력해주세요.")
    
# 컴퓨터가 낼 가위(1) 바위(2) 보(3) 정해주기
# 가위1 바위2 바위2 보3 가위1 보3

    com_=[1,2,3]
    computer = random.choice(com_) # 컴퓨터의 가위, 바위 ,보 값 정해주기

    if user == computer:
        print("비겼습니다\n비긴 경우 카운트 되지 않습니다.")
    elif user == 1 and computer == 2:
        print("내가 가위를 내고 컴퓨터가 바위를 내서 패배하였습니다.")
        com_count += 1
        print(f"유저 {user_count} : 컴 {com_count}")
    elif user == 1 and computer == 3:
        print("내가 가위를 내고 컴퓨터가 보를 내서 승리하였습니다.")
        user_count += 1
        print(f"유저 {user_count} : 컴 {com_count}")
    elif user == 2 and computer == 1:
        print("내가 바위를 내고 컴퓨터가 가위를 내서 승리하였습니다.")
        user_count += 1
        print(f"유저 {user_count} : 컴 {com_count}")
    elif user == 2 and computer == 3:
        print("내가 바위를 내고 컴퓨터가 보를 내서 패배하였습니다.")
        com_count += 1
        print(f"유저 {user_count} : 컴 {com_count}")
    elif user == 3 and computer == 1:
        print("내가 보를 내고 컴퓨터가 가위를 내서 패배하였습니다.")
        com_count += 1
        print(f"유저 {user_count} : 컴 {com_count}")
    elif user == 3 and computer == 2:
        print("내가 보를 내고 컴퓨터가 바위를 내서 승리하였습니다.")
        user_count += 1
        print(f"유저 {user_count} : 컴 {com_count}")

    if user_count == 3:
        print("===유저가 최종 승리하였습니다===")

    if com_count == 3:
        print("===컴퓨터가 최종 승리하였습니다.===")

                