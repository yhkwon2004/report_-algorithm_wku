student = []

# 학생 정보 입력 받기
for i in range(3):
    name = input(f"{i+1}번 학생의 이름: ")
    stu_num = input(f"{i+1}번 학생의 학번: ")
    phone = input(f"{i+1}번 학생의 전화번호: ")
    
    student.append({"이름": name, "학번": stu_num, "전화번호": phone})

for i in range(3):
    print(f"{i+1}번 학생 정보: {student[i]}")
