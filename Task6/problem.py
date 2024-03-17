class Solution:
    def sampleStats(self, count):
        min_val, max_val, mean_val, median_val, mode_val = float("inf"), float("-inf"), 0, 0, 0 

        running_sum, total = 0, 0 

        for i in range(256):
            if count[i] > 0:
                min_val = min(min_val,i)
                max_val = max(max_val,i)
                running_sum += i*count[i]
                total += count[i]

        mean_val = running_sum/total
        mode_val = count.index(max(count))

        if total%2 == 1:
            i, val, bg = 0, total//2, 0 

            while i < 256 and bg <= val:
                bg += count[i] 
                i += 1 

            median_val = i-1
        else:
            i, val, b1 = 0, total//2-1, 0 

            while i < 256 and b1 <= val:
                b1 += count[i]
                i += 1 

            m1 = i-1

            i, val, b2 = 0, total//2, 0 

            while i < 256 and b2 <= val:
                b2 += count[i]
                i += 1 
            
            m2 = i-1

            median_val = (m1+m2)/2

        return [min_val,max_val,mean_val,median_val,mode_val]