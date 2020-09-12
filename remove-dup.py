#Remove Duplicate Names

names = ["Alex","John","Mary","Steve","John", "Steve"]

def remove_dups(list):
  new_list = []
  for item in list:
    if item not in new_list:
      new_list.append(item)

  return new_list

names = remove_dups(names)
print(names)  