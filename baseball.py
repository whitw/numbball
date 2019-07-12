import random


def seperate(check: int):
    # 1234 -> [1, 2, 3, 4]
    return [check // 1000, check % 1000 // 100, check % 100 // 10, check % 10]
  
def compare(check, to) -> (int, int):
    # strike, ball 계산
    if not validate(check) or not validate(to):
        raise Exception('invalid data' + str(check) + str(to))
    sepC = seperate(check)
    sepT = seperate(to)

    strike = 0
    ball = 0
    for a, b in zip(sepC, sepT):
        if a == b:
            strike += 1
    for a in set(sepC):
        if a in set(sepT):
            ball += 1
    ball -= strike

    return strike, ball

def validatelist(num):
    #유효한 값들만 뽑아서 리스트로 만든다
    return [i for i in num if validatenum(i)]

def validatenum(num):
    #값이 유효한지 확인한다
    if not (0 <= num <= 9999):
        return False
    if len(set(seperate(num))) < 4:
        return False
    return True

def validate(num):
    #validatelist + validatenum: 자료 형태에 따라 결정
    try:
        iter(num)
    except Exception:
        return validatenum(num)
    else:
        return validatelist(num)

def getSet(check: int, strike: int, ball: int):
    #check와 비교해 s,b가 나오는 숫자들의 set 생성
    if not validate(check):
        return set()
    result = set()
    positional = seperate(check)
    for i in range(0, 10000):
        if(validate(i)):
            if (compare(check, i) == (strike, ball)):
                result.add(i)
    return result


def solve_game():
    answer = 1234
    while(True):
        temp = random.randint(0, 9876)
        if(validate(temp) is True):
            answer = temp
            break
    del(temp)
    data = {i for i in range(0, 10000)}
    validate(data)

    # 답을 임의의 값으로 맞추고 싶으면
    # 아랫 줄의 #표시를 떼고 값을 입력할 것
    #answer = 5372
    while(True):
        # 실제 게임
        try:
            testnum = int(input('야구, 시도해볼 숫자'))
        except ValueError:
            print('다른 값을 시도하세요.')
            continue
        if not validate(testnum):
            print('다른 값을 시도하세요.')
            continue # 이상한 값을 넣었으면 다시
        data = data & getSet(testnum, *compare(testnum, answer)) #답안 줄이기
        s,b = compare(testnum, answer) #s,b계산
        print(str(s) + 's' + str(b) + 'b')
        if(len(data) <= 1):
            try:
                testnum = int(input('답은?'))
                if(answer == testnum):
                    print('정답!')
                    return #정답이면 게임 종료
                else:
                    print('아닌데요... 다시 해보세요.')
            except ValueError:
                print('정수값을 입력하세요.')
        else: #값이 많으면 한번 더 시도
            pass
            # print(data)
            # print(str(len(data)) + '개 경우의 수가 남았습니다!')

if(__name__ == '__main__'):
    while(True):
        solve_game()
