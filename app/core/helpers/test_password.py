from unittest import TestCase
from . import password
import random, string


class TestPassword(TestCase):
    def gen_random(self, length=10) -> str:
        return "".join(random.choices(string.ascii_letters, k=length))

    def test_hash_and_verify(self) -> None:
        """
        confirm password is hashed and verified correctly
        """
        cleartext: str = self.gen_random()
        hashed: str = password.hash(str(cleartext))

        is_valid = password.verify(str(cleartext), hashed)
        self.assertTrue(is_valid)

    def test_hash_and_invalid_verify(self) -> None:
        """
        confirm invalid password hash is not confirmed as valid
        """
        pwd1: str = self.gen_random()
        hashed: str = password.hash(pwd1)

        pwd2: str = self.gen_random()
        self.assertNotEqual(pwd1, pwd2)

        is_valid = password.verify(pwd2, hashed)
        self.assertFalse(is_valid)
