from typing import List

class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        pass

    def ins(self, name: str, row: List[str]) -> bool:
        pass

    def rmv(self, name: str, rowId: int) -> None:
        pass

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        pass
    
    def exp(self, name: str) -> List[str]:
        pass
