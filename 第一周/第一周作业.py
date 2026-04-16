fruits: list[str]=["apple0","apple1","apple2","apple3","apple4"]
from typing import Iterable,Any
class deleteElement:
 def __init__(self,iterable: Iterable[Any]):
     self.iterable = list(iterable)
 def delete(self,index_to_delete: int) -> list[Any]:
    """
    从列表中删除元素
    
    :param index_to_delete: 需要删除的元素的位置
    """
    L :int =len(self.iterable)
    """
    从后往前替换元素，并将最后一位空置
    """
    for i in range(index_to_delete,L-1,+1):
        self.iterable[i]=self.iterable[i + 1]
    self.iterable.pop()
    return self.iterable
delete_element = deleteElement(fruits)
print(delete_element.delete(2))
# 打印删除后的列表