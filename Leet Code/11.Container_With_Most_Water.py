
def maxArea(height):
    
    l =0
    r = len(height)-1
    area =0
    while (l<r):
        h = min(height[l],height[r])
        w = r-l
        area = max(area,h*w)
        if (height[l]<height[r]):
            l+=1
        else:
            r -=1
    return area
    

data =[1,8,6,2,5,4,8,3,7]
c = maxArea(data)
print(c)
        
        
