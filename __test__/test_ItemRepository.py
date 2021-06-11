from model.Items.ItemRepository import ItemRepository
import unittest

class ItemRepositoryTest(unittest.TestCase):
    def test_ItemRepositoryCreation(self):
        testRepo = ItemRepository(pathItem="./assets/items.json", pathAttackItem="./assets/AttackItems.json")
        self.assertEqual(len(testRepo.getItemList()), 3)

if __name__ == '__main__':
    unittest.main()
