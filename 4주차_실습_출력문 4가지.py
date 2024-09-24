이름 = input("이름을 입력하세요: ")
학번 = input("학번을 입력하세요: ")
전화번호 = input("전화번호를 입력하세요: ")

print("이름:", 이름, "학번:", 학번, "전화번호:", 전화번호)

# f문자열
print(f"이름: {이름}, 학번: {학번}, 전화번호: {전화번호}")

# % 연산자
print("이름: %s, 학번: %s, 전화번호: %s" % (이름, 학번, 전화번호))

# format() 함수
print("이름: {}, 학번: {}, 전화번호: {}".format(이름, 학번, 전화번호))
