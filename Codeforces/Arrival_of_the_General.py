military = int(input())
heights = list(map(int,input().split()[:military]))


# maxx = max(heights)
# minn = min(heights)
# for i in range(military):
#     if heights[i] > maxx:
#         maxx = heights[i]
#         index_max = i
#     if heights[i] <= minn:
#         minn = heights[i]
        # index_min = i

maxx = 0
minn = 101

for i in range(military):
    if heights[i] > maxx:
        maxx = heights[i]
        index_max = i
    if heights[i] <= minn:
        minn = heights[i]
        index_min = i
if index_max>index_min:
    index_min = index_min+1
print(index_max+(military-1)-index_min)