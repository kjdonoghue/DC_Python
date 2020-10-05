#Duplicate the Array

list_num = [1,2,3,4,5]

def duplicate_list(list):
  i=0
  list_length = len(list)
  while i < list_length:
      list.append(list[i])
      i += 1
  return list

print(duplicate_list(list_num))
