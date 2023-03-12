# sort ascending & descending a dictionary by value


# import lib
import operator

# create dictionary

dict1 = {1:2, 3:4, 4:3, 2:1, 0:0}

print("dictionary is:", dict1)

# sort dictionary
sorted_dict1 = sorted(dict1.items(), key=operator.itemgetter(1))
print("Ascending order is: ", sorted_dict1)

desc_sorted_dict1 = dict(sorted(dict1.items(), key=operator.itemgetter(1), reverse=True))
print("Descending order is: ", desc_sorted_dict1)

# Thanks for Watching
