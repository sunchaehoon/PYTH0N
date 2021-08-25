# 지역변수
# 전역변수
gun = 10

def checkpoint(soldiers):    # 경계근무
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))    # 여기까지 함수

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2)   # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))


def std_weight(height, gender):
    if gender == "남자":
        return heightheight22
    else:
        return heightheight21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)    # round = 소수 자릿수 설정
print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(height, gender, weight))
