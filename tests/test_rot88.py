from rot88 import rot88
from settings import test_data_path
from unittest import TestCase

class TestRot88(TestCase):

    def process_file(self, filename):
        with open(test_data_path / filename, 'r') as file:
            message = file.read()
        ciphertext = rot88(message)
        assert rot88(ciphertext) == message

    def test_message(self):
        self.process_file('message.txt')

    def test_equations(self):
        self.process_file('equations.txt')

    def test_pirsquared(self):
        self.process_file('pirsquared.txt')

    def test_spanish(self):
        self.process_file('spanish.txt')
