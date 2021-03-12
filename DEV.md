# developer document

## commands

- `nox -r`
- `nox -rs tests-3.8 -- -m e2e`


### Report coverage to HTML file.

```sh
poetry run pytest --cov --cov-report html
```

### gitignore

- https://github.com/github/gitignore/blob/master/Python.gitignore

## Deployment

- poetry build
- poetry publish -r testpypi
- poetry publish
- git tag -s vX.X.X

## TODO

- [x] nox -r
- [ ] isort / flake8 bugs


## References

- [SO: Using travis CI with wxPython tests](https://stackoverflow.com/questions/29290011/using-travis-ci-with-wxpython-tests)