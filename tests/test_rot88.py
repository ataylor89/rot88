from tests import project_root
from encrypt import encrypt
from decrypt import decrypt
from unittest import TestCase

class TestRot88(TestCase):

    @classmethod
    def setUpClass(cls):
        message_path = project_root / 'tests' / 'test_data' / 'message.txt'
        with open(message_path, 'r') as file:
            cls.message = file.read()

        equations_path = project_root / 'tests' / 'test_data' / 'equations.txt'
        with open(equations_path, 'r') as file:
            cls.equations = file.read()

        pirsquared_path = project_root / 'tests' / 'test_data' / 'pirsquared.txt'
        with open(pirsquared_path, 'r') as file:
            cls.pirsquared = file.read()

        spanish_path = project_root / 'tests' / 'test_data' / 'spanish.txt'
        with open(spanish_path, 'r') as file:
            cls.spanish = file.read()

    def encrypt_decrypt(self, content):
        assert decrypt(encrypt(content)) == content

    def test_message(self):
        self.encrypt_decrypt(self.message)

    def test_equations(self):
        self.encrypt_decrypt(self.equations)

    def test_pirsquared(self):
        self.encrypt_decrypt(self.pirsquared)

    def test_spanish(self):
        self.encrypt_decrypt(self.spanish)
