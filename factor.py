# %%
nums = range(2,101)
# 0～100までの素数をリストprimeに格納
prime = []
for i in nums:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime.append(i)

# 0～100までの整数を素因数分解
for i in nums:
    print(i,end='...')
    # divを整数iに設定
    div = i
    for j in prime:
        # divが素数jで割り切れるかぎりjで割り続ける
        while div % j == 0:
            div = div//j
            print(j,end=' ')
        # divが1になったらこれ以上割れないので、分解完了
        if div == 1:
            break
    print()

# %%
