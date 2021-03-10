def test_sched_count_up() -> None:
    import gentimer
    import sched

    scheduler = sched.scheduler()

    def long_wait(count: int):
        yield count

    cancel = gentimer.sched(scheduler, long_wait(30))

    # testing to call cancel
    def call_later(count, func):
        yield count
        func()
        func()  # cancel twice to pass partial case

    gentimer.sched(scheduler, call_later(1, cancel))

    scheduler.run()
