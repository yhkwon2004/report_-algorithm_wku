nickSet = {'수선화',"코스모스",'들국화'}
userNickname = input("원하는 닉네임을 입력하세요: ")

while True:
    
    if userNickname in nickSet:
        print("이미 사용 중입니다. 다시 입력해 주세요.")
        userNickname = input("원하는 닉네임을 입력하세요: ")

    else:
        print("사용 가능합니다. 닉네임으로 등록합니다.")
        nickSet.add(userNickname)
        break

print("사용 중인 닉네임:", nickSet)
