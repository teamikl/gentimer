from PyQt5.QtCore import QCoreApplication  # type: ignore
from gentimer.timer_qt import gen_timer
import pytest


@pytest.mark.e2e
def test_qt_cancel():
    app = QCoreApplication([])

    def wait(count):
        for _ in range(count):
            yield 1

    def call_later(count, func):
        yield count
        func()
        func()  # cancel twice for partial case

    cancel = gen_timer(app, wait(30))
    gen_timer(app, wait(1))
    gen_timer(app, call_later(2, cancel), done=app.quit)
    app.exec_()


@pytest.mark.e2e
def test_qt_count_up():
    app = QCoreApplication([])

    def count_up(count):
        for _ in range(count):
            yield 1

    gen_timer(app, count_up(3), done=app.quit)
    app.exec_()
