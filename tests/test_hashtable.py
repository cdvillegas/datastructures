import unittest
from datastructures.hashtable import HashTable

class TestHashTable(unittest.TestCase):

    def test_put_and_get(self):
        ht = HashTable(10)
        ht.put('a', 1)
        self.assertEqual(ht.get('a'), 1)

        ht.put('b', 2)
        self.assertEqual(ht.get('b'), 2)

    def test_collision_handling(self):
        ht = HashTable(1)
        ht.put('a', 1)
        ht.put('b', 2)

        self.assertEqual(ht.get('a'), 1)
        self.assertEqual(ht.get('b'), 2)

    def test_update_existing_key(self):
        ht = HashTable(10)
        ht.put('a', 1)
        self.assertEqual(ht.get('a'), 1)

        ht.put('a', 3)
        self.assertEqual(ht.get('a'), 3)

    def test_key_not_found(self):
        ht = HashTable(10)
        with self.assertRaises(KeyError):
            ht.get('nonexistent_key')

    def test_large_dataset(self):
        ht = HashTable(1000)
        for i in range(1000):
            ht.put(str(i), i)

        for i in range(1000):
            self.assertEqual(ht.get(str(i)), i)

if __name__ == '__main__':
    unittest.main()
