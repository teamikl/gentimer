from typing import Any
import nox
from nox.sessions import Session

locations = ["src", "tests", "noxfile.py", "docs/conf.py"]


@nox.session(python="3.8")
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python="3.8")
def isort(session: Session) -> None:
    """Run isort formatter.""" # TODO: remove
    args = session.posargs or locations
    session.install("isort")
    session.run("isort", *args)


# TODO: watch lint?
@nox.session(python="3.8")
def lint(session: Session) -> None:
    """Lint using flake8.

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
def tests(session: Session):
    """Run the test suite.

    Commands
    =========

    > nox -r tests -- [args]

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


@nox.session(python="3.8")
def docs(session: Session) -> None:
    """Build the documentation."""
    session.run("poetry", "install", external=True)
    session.install(
        "sphinx",
        "sphinx-autodoc-typehints",
        # "recommonmark",
        "m2r2",
    )
    session.run("sphinx-build", "docs", "docs/_build")
