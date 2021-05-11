import unittest
from model.Items.UseItem import UseItem
from model.Items.DefenseItem import DefenseItem
from model.Items.AttackItem import AttackItem
#TODO add more tests.

class ItemTest(unittest.TestCase):
    def test_emptyUseItem(self):
        testItem = UseItem()
        self.assertEqual(testItem.getQuality(), 0)

    def test_basicDefenseItem(self):
        testItem = DefenseItem(defense=10)
        self.assertEqual(testItem.getDefense(), 10)

    def test_basicAttackItem(self):
        testItem = AttackItem()
        self.assertEqual(testItem.getDamage(), 0)

    def test_useOfUseItem(self):
        testItem = UseItem(use=lambda y:  y+ " used")
        self.assertEqual(testItem.use("Item"), "Item used")

if __name__ == '__main__':
    unittest.main()