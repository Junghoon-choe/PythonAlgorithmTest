# [문제 설명]
# [나의 풀이]
# [다른 방식]
# [Best]
# [1]
# [2]

# ========================= [LV_3] =========================

# TODO : [문제] - 모의고사 (종합)

# TODO : [문제] - 소수찾기 (수학)

# TODO : [문제] - 체육복 (for, if)


# ========================= [LV_2] =========================

# TODO : [문제] - 비밀지도(진법)

# TODO : [문제] - 시저암호 (for, if)

# TODO : [문제] - 예산 (for)

# TODO : [문제] - 2016년 (if)

# TODO : [문제] - 완주하지 못한 선수 (for, if)

# TODO : [문제] - 나누어 떨어지는 숫자 배열 (array)

# TODO : [문제] - 하샤드 수 (형변환)

# TODO : [문제] - K 번째 수 (method)

# TODO : [문제] - 핸드폰 번호 가리기 (string, 한줄로 풀어보기)

# TODO : [문제] - 자연수 뒤집어 배열로 만들기 (형변환, 숫자)

# TODO : [문제] - 정수 내림차순으로 배치하기 (형변환, 한줄로 풀어보기)

# TODO : [문제] - 문자열 다루기 기본 (지수표기법)
# [문제 설명]
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# 예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

# [나의 풀이]

# def solution(s):
#     if len(s) == 4 or len(s) == 6:
#         for i in range(len(s)):
#             if not s[i].isdigit():
#                 return False
#         return True
#     else:
#         return False
# solution("1234")

# [다른 방식]
# [Best]
# def alpha_string46(s):
#     return s.isdigit() and len(s) in (4, 6)
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print( alpha_string46("a234") )
# print( alpha_string46("1234") )
# [1]
# def alpha_string46(s):
#     import re
#     return bool(re.match("^(\d{4}|\d{6})$", s))
#
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print( alpha_string46("a234") )
# print( alpha_string46("1234") )
# [2]
# def alpha_string46(s):
#     try:
#         int(s)
#     except:
#         return False
#     return len(s) == 4 or len(s) == 6
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print( alpha_string46("a234") )
# print( alpha_string46("1234") )
# TODO : [문제] - 정수 제곱근 판별 (math, 한줄로 풀어보기)

# TODO : [문제] - 최대공약수와 최소공배수 (변수, 수학)

# TODO : [문제] - 자릿수 더하기 (형변환, 재귀)

# TODO : [문제] - 평균 구하기 (for, method, 한줄로 풀어보기)
'''
# [문제 설명]
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# [나의 풀이]
# def solution(arr):
#
#     return sum(arr)/len(arr)
# arr = [1,2,3,4]
# [다른 방식]
# [Best]
# def solution(arr):
#
#     return sum(arr)/len(arr)
# arr = [1,2,3,4]
# [1]
# from functools import reduce
# def average(list):
#     # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
#     return reduce(lambda x, y : x + y, list) / len(list)
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# list = [5,3,4]
# print("평균값 : {}".format(average(list)))
# [2]
# def average(array):
#     return sum(array)/len(array) if array else 0
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# list = [5,3,4]
# print("평균값 : {}".format(average(list)))
'''
# TODO : [문제] - 직사각형 별 찍기 (for)

# TODO : [문제] - 같은 숫자는 싫어 (for, if)

# TODO : [문제] - 문자열 내 p와 y의 개수 (method, 한줄로 풀어보기)

# TODO : [문제] - 약수의 합 (for, if)

# ========================= [LV_1] =========================

# TODO : [문제] - 짝수와 홀수 (연산자, 한줄로 풀어보기)
'''
# [문제 설명]
# 정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.
# [나의 풀이]
# def solution(num):
#     answer = ''
#     if num % 2 == 1:
#         answer = 'Odd'
#     else:
#         answer = 'Even'
#     return answer
#
# solution(4)

# [다른 방식]
# [Best]

# def evenOrOdd(num):
#     return "Even" if num%2 == 0 else "Odd"
#
# #아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : " + evenOrOdd(3))
# print("결과 : " + evenOrOdd(2))

# [1]
# def evenOrOdd(num):
#     if (num%2):
#         return "Odd"
#     else:
#         return "Even"
#
# #아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : " + evenOrOdd(3))
# print("결과 : " + evenOrOdd(2))

# [2]
# def evenOrOdd(num):
#     return ["Even", "Odd"][num & 1]
#
# #아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : " + evenOrOdd(3))
# print("결과 : " + evenOrOdd(2))
'''
# TODO : [문제] - 평균 구하기 (for, method, 한줄로 풀어보기)
'''
# [문제 설명]
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# [나의 풀이]
# def solution(arr):
#     answer = 0
#
#     for i in range(len(arr)):
#         answer += arr[i]
#
#     return answer/len(arr)

# [다른 방식]
# [Best]

# def average(list):
#     return (sum(list) / len(list))
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# list = [5,3,4]
# print("평균값 : {}".format(average(list)))

# [1]
# def average(list):
#     # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
#     if len(list) == 0:
#         return 0
#
#     return sum(list) / len(list)
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# list = [5,3,4]
# print("평균값 : {}".format(average(list)))
# [2]

# from functools import reduce
# def average(list):
#     # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
#     return reduce(lambda x, y : x + y, list) / len(list)
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# list = [5,3,4]
# print("평균값 : {}".format(average(list)))
'''
# TODO : [문제] - x만큼 간격이 있는 n개의 숫자 만들기 (for)
"""
# [문제 설명]
# 함수 solution은 정수 x와 자연수 n을 입력 받아,
# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
# [나의 풀이]
'''
def solution(x, n):
    answer = []
    for i in range(n):
        a = x * i + x
        answer.append(a)
    print(answer)
    return answer


solution(-4, 2)
'''
# [다른 방식]
# [Best]
'''
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))
'''
# [1]
'''
def number_generator(x, n):
    # 함수를 완성하세요
    return [i for i in range(x, x*n+1, x)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(2,5))
'''
# [2]

'''def number_generator(x, n):

    t = list(range(x, n*x+1, x))
    return t

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(3,5))'''
"""
# TODO : [문제] - 가운데 글자 가져오기 (math)
'''
# [문제 설명]
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# [나의 풀이]
# def solution(s):
#     if len(s) % 2 == 1:
#         a = len(s) // 2
#         b = len(s) // 2 + 1
#     else:
#         a = len(s) // 2 - 1
#         b = len(s) // 2 + 1
#     return s[a:b]

# [다른 방식]
# [Best]
# def string_middle(str):
#
#     return str[(len(str)-1)//2:len(str)//2+1]  #
#
# print(string_middle("power"))
# [1]
# def string_middle(str):
#     a = len(str)
#     if a % 2 == 0 :
#         a = (a-2) / 2
#     else :
#         a = (a-1) / 2
#     return str[int(a) : -int(a)]
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(string_middle("power"))
# [2]
# def string_middle(str):
#     leng = len(str)
#     if leng%2==0:
#         return str[leng//2-1:leng//2+1]
#     else:
#         return str[leng//2]
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(string_middle("powerr"))
'''
# TODO : [문제] - 서울에서 김서방 찾기 (method)
'''
# [문제 설명]
# String 형 배열 seoul 의 element 중 Kim 의 위치 x를 찾아, 김서방은 x에 있다는 String 을 반환하는 함수,
# solution 을 완성하세요. seoul 에 Kim 은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# [나의 풀이]
# def solution(seoul):
#     answer = ''
#     print('김서방은 %d에 있다' % seoul.index('Kim'))
#     return ('김서방은 %d에 있다' %seoul.index('Kim'))
# solution("Kim")

# [다른 방식]
# [Best]
# def findKim(seoul):
# return "김서방은 {}에 있다".format(seoul.index('Kim'))

# [1]
# def solution(seoul):
#     answer = ''
#     print('김서방은 %d에 있다' % seoul.index('Kim'))
#     return ('김서방은 %d에 있다' %seoul.index('Kim'))
# solution("Kim")

# [2]
# def findKim(seoul):
#     kimIdx = 0
#     # 함수를 완성하세요
#     for i in range(len(seoul)):
#         if seoul[i]=="Kim":
#             return "김서방은 {}에 있다".format(i)
#
# # 실행을 위한 테스트코드입니다.
# print(findKim(["Queen", "Tod", "Kim"]))
'''
# TODO : [문제] - 수박수박수박수박수? (string)
'''
# [문제 설명]
# 길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수,
# solution을 완성하세요.
# 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

# [나의 풀이]
# [1]
# def solution(n):
#     answer = ''
#     for i in range(n):
#         if i%2 == 0:
#             answer += '수'
#         else:
#             answer += '박'
#
#     return answer
#
# solution(3)

# [2]
# list = []
#
#
# def solution(n):
#     for i in range(n):
#         if i % 2 == 0:  # n을 2로 나눈 나머지 값이 1이면
#             list.append('수')  # 수를 리스트에 넣는다.
#         else:  # 그렇지 않을 경우
#             list.append('박')  # 박을 리스트에 넣는다.
#
#
# solution(10)  # 함수를 불러와서 파리메터값으로 10을 넣어준다.
#
# for i in range(len(list)):  # 반복문으로 리스트의 길이만큼 i번 반복하게 만들고,
#     print(list[i], end="")  # 리스트를 참조해 리스트의 i번째 값을 차례대로 가져올 수 있도록 한다.

# [다른 방식]
# [Best]
# def water_melon(n):
#     s = "수박" * n  # s변수에 수박을 저장한다. *n 만큼. s = '수박수박수박'
#     return s[:n]  # 반환값으로 s에 있는 문자열로 3까지만 출력한다. s[:3] '수박수'
# s[n:] = 끝에서 부터 앞으로 n번째 자리까지 출력한다.
# s[:n] = 앞에서 부터 뒤로 n번째 자리까지 출력한다.
# s[:] = 처음부터 끝까지 뽑아낸다.
# s[19:-7] = 19번쨰 자리부터 -8번쨰 자리 까지 말한다. -7은 포함하지 않는다.
# https://wikidocs.net/13 << 참고할 것.
#
#
# # 테스트 코드.
# print(water_melon(3))

# [1]
# def solution(n):
#     return ('수박'*n)[:n]
# solution(4)
#
# [2]
# def solution(n):
#     answer = ''
#
#     for i in range(n):
#         if i & 2 == 0:
#             answer += '수'
#         else:
#             answer += '박'
#     return answer
#
#
# number = int(input("숫자입력 :"))
#solution(number)
'''
# TODO : [문제] - 두 정수 사이의 합 (for)
'''
# [문제 설명]
# 두 정수 a,b가 주어졌을때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solutiondmf
# 완성하세요. 예를 들어, a = 3, b = 5인 경우, 3+4+5=12 이므로 12를 리턴합니다.


# [나의 풀이]

# list = []
#
#
# def solution(a, b):  # a와 b를 파라미터값으로 받고,
#     if a == b:
#         c = -a
#     else:
#         x = b + a
#         c = x // 2
#
#     answer = a + b + c
#     print(answer)
#     return answer
#
#
# a = int(input("a 값:"))
# b = int(input("b 값:"))
# solution(a, b)


# [다른 방식]
# [Best]
# def adder(a, b):
#     # 함수를 완성하세요
#     if a > b: 
#         a, b = b, a
# 
#     return sum(range(a, b + 1))  # sum 함수를 사용해서 3~5까지 더해준다.
# 
# 
# print(adder(3, 5))

# [1]
# def solution(a, b):
#     answer = 0
#     if a > b:  # 만일 a가 b보다 큰경우,
#         a, b = b, a  # 서로 자리를 바꿔 a를 낮은수로 만들어 줍니다.
#     for i in range(a, b + 1):  # 그 후에 a번 부터 b+1번까지 정수 i로 반복해줍니다.
#         answer += i  # answer로 반복된 i를 차례대로 넣어 더해줍니다. 3 4 5
#     print(answer)  # 해당 답을 프린트해보고,
#     return answer  # 해당 값을 return 합니다.
#
#
#
# solution(3, 5)

# [2]
# def solution(a, b):
#     print((abs(a - b) + 1) * (a + b) // 2)
#     return (abs(a - b) + 1) * (a + b) // 2
#
#
# solution(3, 5)
'''
