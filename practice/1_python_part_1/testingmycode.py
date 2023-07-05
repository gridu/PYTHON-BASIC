def delete_from_list(list_to_clean, item_to_delete):

    print (list_to_clean)
    print (list_to_clean.remove(3))
    return list_to_clean.remove(item_to_delete)

#delete_from_list([1, 2, 3, 4, 3], 3)

list_to_clean = [1, 2, 3, 4, 3]
list_to_clean = [i for i in list_to_clean if i!=3]

print (list_to_clean)

