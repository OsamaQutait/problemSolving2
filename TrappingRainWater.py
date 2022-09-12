def trap(height):
    l, r = 0, len(height) - 1
    l_max, r_max = height[l], height[r]
    result = 0
    while r > l:
        # sheft the one that hase a smaller value
        if l_max > r_max:
            r -= 1
            r_max = max(r_max, height[r])
            result += r_max - height[r]
        else:
            l += 1
            l_max = max(l_max, height[l])
            result += l_max - height[l]
    return result

if __name__ == '__main__':
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))