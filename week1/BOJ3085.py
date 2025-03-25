import sys
input = sys.stdin.readline

n = int(input())
candy = [list(input().strip()) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = 0

def count(x, y):
    retX = 1
    retY = 1
    sumX = 0
    sumY = 0
    for i in range(n-1):
        if candy[x][i] == candy[x][i+1]:
            retX += 1
            sumX = max(sumX, retX)
        else:
            retX = 1
        if candy[i][y] == candy[i+1][y]:
            retY += 1
            sumY = max(sumY, retY)
        else:
            retY = 1
    return max(sumX, sumY)

for x in range(n):
    for y in range(n):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            candy[nx][ny], candy[x][y] = candy[x][y], candy[nx][ny]
            ans = max(ans, count(x, y))
            candy[nx][ny], candy[x][y] = candy[x][y], candy[nx][ny]

print(ans)


# n의 범위가 50이기 때문에 2중 for문으로 상하좌우 다 돌아도 ok
# 문제를 잘봅시다...
# 처음엔 한 줄에 같은 사탕 개수를 구하는건줄 알았음;;
# 그다음엔 한 줄이 아니라 상하좌우로 연결된 사탕 개수를 구하는건줄
# dx, dy 배열을 사용하여 상하좌우와 값 변경
# count 함수로 바꾼 위치의 행, 열에서 연속된 문자열의 개수를 구한다.