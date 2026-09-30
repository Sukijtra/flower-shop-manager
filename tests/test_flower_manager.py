import sys
import os
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from flower_manager import FlowerManager
from flower import Flower, FreshFlower

def test_add_and_search_flower():
    manager = FlowerManager()
    initial_count = len(manager.flowers)
    
    flower = Flower(0, "Test Rose", 150.0, 10, ["test"])
    added = manager.add_flower(flower)
    
    assert len(manager.flowers) == initial_count + 1
    assert added.id > 0
    
    # ทดสอบการค้นหา
    results = manager.search_flowers("Test Rose")
    assert len(results) >= 1
    
    # ลบข้อมูลทดสอบออก
    manager.delete_flower(added.id)