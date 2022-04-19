"""
Write function which deletes defined element from list.
Restriction: Use .pop method of list to remove item.
Examples:
    >>> delete_from_list([1, 2, 3, 4, 3], 3)
    [1, 2, 4]
    >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
    ['a', 'c', 'd']
    >>> delete_from_list([1, 2, 3], 'b')
    [1, 2, 3]
    >>> delete_from_list([], 'b')
    []
"""
from typing import List, Any

def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
    print("lista wejściowa: ", list_to_clean)
    print("element do usunięcia: ",item_to_delete)
    #musimy sprawdzic czy element znajduje sie w liscie 
    #by zadzialala funkcja pop potrzebujemy indeks elementu
    
    if item_to_delete in list_to_clean:
      while item_to_delete in list_to_clean:
          #print(list_to_clean)
          wystapienia = list_to_clean.count(item_to_delete)
          #print("element nalezy do listy")
          pozycja = list_to_clean.index(item_to_delete)
          #print("element do usuniecia pojawil sie w liscie wejsciowej ",wystapienia," razy")
          #print("Pierwszy na pozycji ",pozycja)
          list_to_clean.pop(pozycja)
      print("lista wyjściowa :")
      print(list_to_clean)

   
      
    else:
        print("Element do usunięcia nie znajdował się na liście")
        print(list_to_clean)
  
    

        
