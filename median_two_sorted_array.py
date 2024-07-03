def median(nums1, nums2):
        combined = nums1 + nums2
        combined.sort()
        n = len(combined)
        print(combined)

        if n%2 == 0:
            median = combined[n//2-1]+ combined[n//2]
            median = median/2.0
        else:
            median = combined[n//2]
    
        return median


nums1=[1,2]
nums2=[3,4]
print(median(nums1, nums2))