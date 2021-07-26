# %%
nums = range(2,1001)
# 2～1000までの範囲にある素数をリストprimeに格納していきます。
prime = []
for i in nums:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime.append(i)     # 2～i-1までのどの数でも割り切れないとき、iは素数。

# 双子素数を画面に出力します。
for i in range(len(prime)-1):
    if prime[i] + 2 == prime[i+1]:
        print("{} {}".format(prime[i],prime[i+1]))

# %%
