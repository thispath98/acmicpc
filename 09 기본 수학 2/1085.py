x, y, w, h = map(int, input().split())
# 문제는 맞췄지만 https://hwiyong.tistory.com/222 에서
# 변수 리스트를 만들지 않고 푸는 방법을 참고하였습니다.
print(min([x, w - x, y, h - y]))