def problem2_8(mylis):
    tot = 0
    for i in mylis:
        tot = tot + i
    ave = tot/len(mylis)
    max_t = max(mylis)
    min_t = min(mylis)
    print("Average:", ave)
    print("High:", max_t)
    print("Low:", min_t)
