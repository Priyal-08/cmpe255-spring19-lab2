def mean_num_friends(x):
    return sum(x)/len(x)

def median_num_friends(x):
    x = sorted(x)
    length = len(x)
    if(length%2==0):
        return (x[(int)(length/2) - 1] + x[(int)(length/2)])/2
    else:
        return x[(int)(length/2)]

num_friends = [100, 49, 41, 40, 25, 10, 5, 4, 7, 20,60]
print("mean={}".format(mean_num_friends(num_friends)))
print("median={}".format(median_num_friends(num_friends)))
