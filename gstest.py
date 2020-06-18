def getSubTotals(target,numListList,sofar,use_exclude,exclude):
    if numListList == []: 
        if target==0:
            sofar.append(exclude)
        
    else:
        for y in numListList[0]:
            if not (use_exclude and y in exclude):
                getSubTotals(target -y,numListList[1:],sofar,use_exclude,exclude + [y])
    return sofar


x=getSubTotals(5,[{1}, [4]],[],True,[])
x=getSubTotals(5,[{1, 2, 4}, [1, 2, 4]],[],True,[])
print(x)

i=1


