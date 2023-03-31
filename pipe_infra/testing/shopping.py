from typing import List, Dict, Tuple, Optional, Union, Any
from dataclasses import dataclass

class ShoppingCart:
    def __init__(self, name: str, max_size: int) -> None:
        self.name = name
        self.max_size=max_size
        self.items: Dict[str, int] = {}

    def add(self, item: str, quantity: int,items: Dict[str,str]=None) -> None:
        if item in self.items:
            self.items[item]+=quantity
        elif len(self.items)<self.max_size:
                self.items[item]=quantity
        else:
            raise ValueError("Cart is full")

    def get_items(self) -> List[str]:
        return list(self.items.keys())

    def get_quantity(self, item: str) -> int:
        return self.items[item]

