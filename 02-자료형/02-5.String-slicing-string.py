# 슬라이싱으로 문자열 나누기
a = "20220127Snow"
date = a[:8]
weather = a[8:]
print(date) # 20220127
print(weather) # Snow

# 두 부분으로 나누기
a = "20230127Snow"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year + " " + day + " " + weather)
