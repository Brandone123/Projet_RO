def DPBUKnapsack(S,W):
    track = [[0]*(W+1) for i in range(len(S)+1)]
    keep  = [[False]*(W+1) for i in range(len(S)+1)]
    for i in range(1,len(S)+1):
        for w in range(W+1):
            if S[i-1][0]>w:
                track[i][w]=track[i-1][w]
            else:
                if S[i-1][1]+track[i-1][w-S[i-1][0]]>track[i-1][w]:
                    track[i][w] = S[i-1][1]+track[i-1][w-S[i-1][0]]
                    keep[i][w] = True
                else:
                    track[i][w]=track[i-1][w]
    w,L = W,[]
    for i in range(len(S),0,-1):
        if keep[i][w]:
            L.append(i)
            w-=S[i-1][0]                
    return track[len(S)][W],L