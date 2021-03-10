def test_run_timer_tk() -> None:
    from gentimer.timer_tk import main

    main()


def test_run_timer_wx() -> None:
    from gentimer.timer_wx import main

    main()


def test_run_timer_qt() -> None:
    from gentimer.timer_qt import main

    main()


def test_run_timer_sched() -> None:
    from gentimer.timer_sched import main

    main()
