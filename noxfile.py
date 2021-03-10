import nox

locations = ["src", "tests", "noxfile.py"]


@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python="3.8")
def isort(session):
    args = session.posargs or locations
    session.install("isort")
    session.run("isort", *args)


# TODO: watch lint?
@nox.session(python="3.8")
def lint(session):
    """
    COMMAND
    =======

        nox -rs lint-3.8

    """
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        # "flake8-isort",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python=["3.8", "3.7"])
def tests(session):
    """

    Commands
    =========

    > nox -r

    """
    # add suffix for output htmlcov dir
    htmlcov = f"html:htmlcov-{session.python}"

    args = session.posargs or [
        "--cov",
        "--cov-report",
        htmlcov,
        "-m",
        "not e2e",
    ]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
