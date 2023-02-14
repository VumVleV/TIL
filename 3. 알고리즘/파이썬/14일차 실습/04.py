score_dict = {}
for i in range(5):
    score_dict[i+1] = sum(list(map(int,input().split())))
M = max(score_dict.values())
for key, value in score_dict.items():
    if value == M:
        print(f"{key} {M}")