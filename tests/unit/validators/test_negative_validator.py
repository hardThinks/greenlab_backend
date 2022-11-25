from validators import NegativeValidator
from validators.base_validator import BaseValidator


class TestNegativeValidator:
    def setup_method(self):
        self.validator = NegativeValidator('balance_change')

        assert self.validator.key == 'balance_change'
        assert isinstance(self.validator, BaseValidator) is True

    def test_is_valid(self):
        args = {'balance_change': -10}
        assert self.validator.is_valid(args)

    def test_is_valid_no_value(self):
        args = {}
        assert self.validator.is_valid(args)

    def test_is_valid_negative(self):
        args = {'balance_change': 19}
        assert not self.validator.is_valid(args)

    def test_error(self):
        result = self.validator.error()

        assert result['message'] == 'Number must be negative'
        assert result['key'] == 'error_not_negative_value'
