height = [1,1]

max_area = 0
l = 0
r = len(height)-1

while l<r:
    min_value = min(height[l],height[r])
    dis = r-l
    area = min_value*dis
    max_area = max(area, max_area)
    if (height[l]<height[r]):
        l=l+1
    else:
        r=r-1


print(max_area)