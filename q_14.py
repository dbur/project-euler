largest_val=0
chains_with_len = {}
for i in range(1,1000001):
    chain_val=i
    chain_len=1
    while chain_val >1:
        if (chain_val in chains_with_len):
            chain_len+=chains_with_len[chain_val]
            break
        if chain_val%2==0:
            chain_val = chain_val/2
        else:
            chain_val = chain_val*3+1
        chain_len +=1
    chains_with_len[i] = chain_len
    print(str(i)+" "+str(chains_with_len[i]))
    if chains_with_len[i] > largest_val:
        largest_val = chains_with_len[i]
        answer = i
print(str(answer)+" "+str(chains_with_len[answer]))