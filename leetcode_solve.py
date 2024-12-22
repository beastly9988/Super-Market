def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix_dict = {}
    cardinal = 0
    for i in strs : # i is word  
        cardinal += 1
        x = i[:cardinal]
        cardinal1 = 0
        for j in strs :
            cardinal1 +=1
            y = j[:cardinal1]
            if x == y :
                count += 1
            elif x!=y :
                break






longestCommonPrefix(["flower","flow","flight"])