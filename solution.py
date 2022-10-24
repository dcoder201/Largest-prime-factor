#User function Template for python3

class Solution:
    def largestPrimeFactor (self, N):
        # code here
        res=[]
        for i in range(2,N+1):
            if(N%i==0):
                value=0
                for j in range(2,i):
                    if(i%j==0):
                        value=1
                        break
                if value==0:
                    res.append(i)
        return(max(res))
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends
