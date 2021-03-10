from gentimer.timer_tk import gen_timer
import pytest
import tkinter as tk


@pytest.mark.e2e
def test_tk_cancel():
    root = tk.Tk()
    root.withdraw()

    def wait(count: int):
        yield count

    def call_later(count, func):
        yield count
        func()
        func()  # twice for partial case

    gen_timer(root, wait(1))
    cancel = gen_timer(root, wait(30))
    gen_timer(root, call_later(3, cancel), done=root.quit)
    root.mainloop()
    root.destroy()


@pytest.mark.e2e
def test_tk_count_up():
    from gentimer.timer_tk import gen_timer
    import tkinter as tk

    root = tk.Tk()
    root.withdraw()

    def count_up(count):
        for _ in range(count):
            yield 1

    # NOTE: this test requires to consume 3 seconds
    gen_timer(root, count_up(3), done=root.quit)
    root.mainloop()
    root.destroy()
