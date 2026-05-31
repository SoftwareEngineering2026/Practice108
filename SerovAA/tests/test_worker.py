import pytest
import string
from worker.worker import generate_password

def test_generate_password_default():
    pwd = generate_password(12, True, True)
    assert len(pwd) == 12
    allowed = string.ascii_letters + string.digits + '!@#$%^&*()'
    assert all(c in allowed for c in pwd)

def test_generate_password_no_digits():
    pwd = generate_password(8, use_digits=False, use_special=False)
    assert len(pwd) == 8
    assert not any(c.isdigit() for c in pwd)
    assert not any(c in '!@#$%^&*()' for c in pwd)

def test_generate_password_only_letters():
    pwd = generate_password(10, use_digits=False, use_special=False)
    assert pwd.isalpha()

def test_generate_password_with_special():
    pwd = generate_password(15, use_digits=False, use_special=True)
    allowed = string.ascii_letters + string.digits + '!@#$%^&*()'
    assert all(c in allowed for c in pwd)
    # (можно также проверить, что хотя бы один спецсимвол встречается, но это не гарантировано)
