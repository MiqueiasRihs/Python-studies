import unittest

from first_project import avg

class EasyTestCase(unittest.TestCase):

    def test_easy_input(self):
        self.assertEqual(avg(1, 2, 3), 2)
    
    def test_easy_input_two(self):
        self.assertEqual(avg(10, 10, 10, 10, 10), 10)


class MediumTestCase(unittest.TestCase):

    def test_medium_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, "Miquéias"), 2)

    def test_medium_input_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, "10"), 2)


class HardTestCase(unittest.TestCase):

    def test_hard_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, None), 2)

    def test_hard_input_two(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, float), 10)

    def test_hard_input_three(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, frozenset), 10)

    def test_hard_input_four(self):
        with self.assertRaises(TypeError):
            self.assertEqual(avg(1, 2, 3, set), 2)


if __name__ == '__main__':
    unittest.main()