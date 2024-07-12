reslen = 0
res = ''
s = 'babada'
for i in range(len(s)):
    l,r = i,i

    while l>=0 and r<reslen and s[l] == s[r]:
        if (r-l+1)>reslen:
            reslen = r-l+1
            res = s[l:r+1]
        l-=1
        r+=1
    
for i in range(len(s)):
    l,r = i, i+1
    while l>0 and r<reslen and s[l] == s[r]:
        if (r-l+1)>reslen:
            reslen = r-l+1
            res = s[l:r+1]
        l-=1
        r+=1
