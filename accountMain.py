from account import *
from installAccount import *
ac = Account(1, "a")# 1번계좌 이름a 생성
ac.input(100)#100원 입금
ac.withdrow(10)#10원 출금
ac.print()#a계좌에 현 상황 출력

print()

ina = installAccount(2, 'b', '1/1')# 2번계좌 이름b 일자 1/1 생성
ina.input(10000)#10000원 입금, installaccount는 account의 subclass이므로 account의 메소드 사용가능
ina.print()#현 상황 출력

print()

ina.close()#적금 해지

