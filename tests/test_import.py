import gentimer
import pytest


def test_submodule_ok():
    assert callable(gentimer.tk)
    pass


def test_unknown_submodule():
    with pytest.raises(AttributeError) as e:
        gentimer.xxx  # unkwnon submodule

    assert "module 'gentimer' has no attribute 'xxx'" in str(e.value)
