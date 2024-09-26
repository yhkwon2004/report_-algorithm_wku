def print_n_times(n,*valueS):
    #n번반복하기
    for i in range(n):
        #valueS는 리스트처럼 사용

        for value in valueS:
            print(value)

        #줄바꿈용도
        print()
#함수호츨
print_n_times(3,"안녕하세요","즐거운","파이썬? 프로? 그래?밍?")