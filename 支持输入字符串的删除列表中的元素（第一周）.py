# %%
sta =list(map(str,input("请输入一组字符串（以逗号分隔）:").split(','))) 
n:int=int(input("请输入一个整数："))
"""
获取需要删除元素的字符串列表和需要删除的元素的位置
:param sta: 需要删除元素的字符串列表
:param n: 需要删除的元素的位置
"""
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
    for i in range(index_to_delete,L,+1):
        self.iterable[i-1]=self.iterable[i]
    self.iterable.pop()
    return self.iterable
delete_element = deleteElement(sta)
print(delete_element.delete(n))
# 打印删除后的列表

