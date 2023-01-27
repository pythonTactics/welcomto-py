## 기본 사용예
# a = "Life is too short, You need Python"
# b = a[8] + a[9] + a[10] + " " + a[12] + a[13] + a[14] + a[15] + a[16]
# print(b)

## 슬라이싱 사용예
# # 0 <= a < 3
# a = "Life is too short, You need Python"
# # print(a[0:4])
# print(a[0:5])

## 슬라이싱 시 항상 시작 번호가 0일 필요는 없다.
a = "Life is too short, You need Python"

print(a[0:2]) ## 'Li'
print(a[5:7]) ## 'is'
print(a[12:17]) ## 'short
print(a[19:34]) ## You need Python

# a[시작 번호:끝 번호]에서 끝번호 생략 시 시작 번호부터 그 문자열의 끝까지 뽑아냄
print(a[19:]) ## You need Python
# a[시작 번호:끝 번호]에서 시작 번호 생략 시 문자열의 처음부터 끝 번호까지 뽑아냄
print(a[:17]) ## Life is too short

# a[시작번호: 끝번호]에서 시작 번호와 끝 번호를 생략 시 문자열의 처음 부터 끝까지 뽑아냄
print(a[:])

# 슬라이싱에서도 인덱싱과 마찬가지로 마이너스(-) 기호 사용 가능
print(a[19: -7]) ## You need