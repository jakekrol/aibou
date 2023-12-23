# Dev

- [setuptools guide](https://setuptools.pypa.io/en/latest/userguide/)
- [uploading to PyPi](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

## Workflow

From the project directory:
``` bash
# 1. install
pip install -e .
# 2. make edits
...
# 3. test
python -m aibou
# 4. repeat 2 & 3
...
# 5. build
python3 -m pip install --upgrade build
python3 -m build
# 6. publish to testpypi
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
# 7. test install
python3 -m venv .venv
pip3 install --upgrade pip
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ aibou
# 8. publish to pypi
python3 -m twine upload dist/*
```

Tips:

- Double check `dist/*` contains all necessary data files. If not, edit `pyproject.toml`.
- Change version before pushing to PyPi


