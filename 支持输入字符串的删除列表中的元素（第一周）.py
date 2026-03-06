# %%
sta =list(map(str,input("请输入一组字符串（以逗号分隔）:").split(','))) 
n:int=int(input("请输入一个整数："))
from typing import Iterable,Any
class deleteElement:
 def __init__(self,iterable: Iterable[Any]):
     self.iterable = list(iterable)
 def delete(self,index_to_delete: int) -> list[Any]:
    L :int =len(self.iterable)
    for i in range(index_to_delete,L,+1):
        self.iterable[i-1]=self.iterable[i]
    self.iterable.pop()
    return self.iterable
delete_element = deleteElement(sta)
print(delete_element.delete(n))


