def commonPrefix(strs):
    minStr=min(strs,key=len)
    l=len(minStr)
    while l>0:
        pre=minStr[:l]
        if all(pre in i[:l] for i in strs):
            print(pre)
            break
        else:
            l-=1
    print("no common prefix")

strs = ["flower","flow","flight"]
commonPrefix(strs)