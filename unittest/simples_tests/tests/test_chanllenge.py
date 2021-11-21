import unittest
from challenge import Car


class EasyTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_easy_input(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.assertEqual(self.car._speed, 20)

    def test_easy_input_two(self):
        self.car.add_speed()
        self.car.add_speed()

        self.car.stop()
        self.assertEqual(self.car.current_speed(), 0)

        # Todo: use the object car to add speed 2 times.
        # Todo: use the object car to stop the car.
        # Todo: make sure that the current speed is 0 not -10.

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


class MediumTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_medium_input(self):
        # Todo: raise an exception if the user tried to start the car while it's already on.
        with self.assertRaises(Exception):
            self.car.start_car()

    def test_medium_input_two(self):
        # Todo: use the object car to remove speed 4 times.
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()

        self.assertEqual(self.car.current_speed(), 0)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


class HardTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_hard_input(self):
        # Todo: use the object car to add speed 2 times.
        self.car.add_speed()
        self.car.add_speed()

        # Todo: use the object car to remove speed 4 times.
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()

        # Todo: make sure that the current speed is 0. 
        self.assertEqual(self.car.current_speed(), 0)

    def test_hard_input_two(self):
        # Todo: use the object car to add speed 2 times.
        self.car.add_speed()
        self.car.add_speed()

        # Todo: stop the car 3 times.
        self.car.stop()
        self.car.stop()
        self.car.stop()

        # Todo: make sure that the current speed is 0.
        self.assertEqual(self.car.current_speed(), 0)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


if __name__ == '__main__':
    unittest.main()
