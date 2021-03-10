from gentimer.timer_wx import gen_timer
import pytest
import wx  # type: ignore


@pytest.mark.e2e
def test_wx_cancel_gen() -> None:
    app = wx.App()
    win = wx.Frame(None, wx.ID_ANY)
    win.Hide()

    def wait(count: int):
        yield count

    def call_later(count, func):
        yield count
        func()
        func()  # twice for partial case

    cancel = gen_timer(wait(10))
    gen_timer(wait(1))
    gen_timer(call_later(3, cancel), done=win.Close)
    app.MainLoop()


@pytest.mark.e2e
def test_wx_count_up() -> None:
    app = wx.App()
    win = wx.Frame(None, wx.ID_ANY)
    win.Hide()

    def count_up(count):
        for _ in range(count):
            yield 1

    gen_timer(count_up(3), done=win.Close)
    app.MainLoop()
