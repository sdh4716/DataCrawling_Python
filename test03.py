#p124
nums=[1,1,1,2,2,3,2,3,2,3,3,3,1]

def max_count(nums):
    counts ={}
    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = i # 1:3 2:1
    return counts

counts = max_count(nums)
first = []
max_num = max(counts.values())
for name, count in counts.items():
    print(name,":",count,"번")
    if count == max_num :
        first.append(name)
print("1등 :", first)

#####
def sum(n):
    hap = 0
    for i in range(1,n+1):
        hap += i
    return hap

print(sum(10))
