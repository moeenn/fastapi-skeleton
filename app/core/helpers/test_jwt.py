from unittest import TestCase
from . import jwt
import time


class TestJWT(TestCase):
    secret: str = "abc123123123"
    payload = jwt.JWTPayload(
        sub=300,
        role="ADMIN",
    )

    def test_create_and_validate(self) -> None:
        """
        valid JWT encode / decode test
        """
        token: str = jwt.create_token(self.secret, self.payload)
        self.assertTrue(isinstance(token, str))

        result: jwt.JWTPayload | None = jwt.validate_token(self.secret, token)
        self.assertIsNotNone(result)

        self.assertEqual(result.sub, self.payload.sub)
        self.assertEqual(result.role, self.payload.role)

    def test_create_and_invalid(self) -> None:
        """
        ensure expired / invalid jwts cannot be validated against valid or
        invalid secret keys
        """
        token: str = jwt.create_token(self.secret, self.payload, exp_seconds=15)

        invalid_result_one: jwt.JWTPayload | None = jwt.validate_token(
            secret=self.secret + "123",
            token=token,
        )
        self.assertIsNone(invalid_result_one)

        invalid_result_two: jwt.JWTPayload | None = jwt.validate_token(
            secret=self.secret,
            token=token + "123",
        )
        self.assertIsNone(invalid_result_two)

    def test_expired_token(self) -> None:
        """
        create a token which expires after n seconds, and check if its validation
        fails
        """
        token: str = jwt.create_token(self.secret, self.payload, exp_seconds=4)
        self.assertTrue(isinstance(token, str))

        time.sleep(5)
        result: jwt.JWTPayload | None = jwt.validate_token(self.secret, token)
        self.assertIsNone(result)
