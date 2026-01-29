from rot88 import rot88
from unittest import TestCase

class TestRot88(TestCase):

    def process_file(self, path):
        with open(path, 'r') as file:
            message = file.read()
        assert rot88(rot88(message)) == message

    def test_message(self):
        self.process_file('tests/test_data/message.txt')

    def test_equations(self):
        self.process_file('tests/test_data/equations.txt')

    def test_pirsquared(self):
        self.process_file('tests/test_data/pirsquared.txt')

    def test_spanish(self):
        self.process_file('tests/test_data/spanish.txt')
