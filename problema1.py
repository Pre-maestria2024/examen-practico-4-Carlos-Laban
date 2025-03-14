def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
   
    m, n = map(int, data[:2])
    H = list(map(int, data[2:2+m]))           # h_i
    D = list(map(int, data[2+m:2+2*m]))       # d_i
   
    total_d = sum(D)
   

    if n == 0:
        print(total_d)
        return
   
    INF = 10**15
    dp = [INF] * (n+1)
    dp[0] = 0
   
    for i in range(m):
        hi, di = H[i], D[i]
       
        new_dp = dp[:]
       
        for k in range(n+1):
            if dp[k] == INF:
                continue  # no se puede alcanzar esta salud, omitir
           
            nk = min(n, k + hi)   # nueva salud
            cost = dp[k] + di    # costo acumulado al comer este alimento
            if cost < new_dp[nk]:
                new_dp[nk] = cost
       
        dp = new_dp
   

    if dp[n] == INF or dp[n] > total_d:
        answer = 0
    else:
        answer = total_d - dp[n]
   
    print(answer)


if __name__ == '__main__':
    main()
