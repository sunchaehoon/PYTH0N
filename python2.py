from random import*
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50
    time = randrange(5, 51)
    if 5 <= time <= 15:     # 매칭 성공
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:   #매칭 실패한 경우
        print("[]번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))


# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):    # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):   # 출금
    if balance >= money:    # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance
def withdraw_night(balance, money):    # 저녁에 출금(+수수료)
    commission = 100    # 수수료
    return commission, balance - money - commission
  balance = 0    #잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("수수료 : {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))


# 기본값

# def profile(name, age, main_lang):
    # print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.
def profile(name, age=17, main_lang="파이썬"):
     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")
