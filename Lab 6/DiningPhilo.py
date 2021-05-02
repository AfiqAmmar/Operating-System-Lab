def add_values_in_dict(sample_dict, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

philosophers={}
jobs=5

for j in range(jobs):
    philosophers[j]=[j]

print(philosophers)

# for i in philosophers.keys():
#     RightChopstick=(i+1)%5
#     for j in philosophers.keys():
#         if RightChopstick in philosophers.get(j):
#             value=philosophers.get(j)
#             value.remove(RightChopstick)
#             philosophers[j]=value
#             print(philosophers,"1")
#             break
#     print(philosophers,"2")
#     philosophers = add_values_in_dict(philosophers, i, [RightChopstick])
#     print(philosophers,"3")
                 
    