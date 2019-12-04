import account
class installAccount(account.Account):#account를 수퍼클래스로 갖는 클래스 installAccount 생성, 날짜를 추가적인 요소로 갖는다.
    def __init__(self, num, name, date):
        super().__init__(num, name)
        self.date = date
        self.charge = 0
    def close(self):#적금을 해지하는 메쏘드, 반환값은 charge에 이자율2%를 곱한 값으로 한다.
        self.charge = 1.02 * self.charge
        print("적금 해약금:", self.charge)
        return self.charge
