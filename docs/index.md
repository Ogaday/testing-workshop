# Testing 101

This workshop will cover the what, why and how of testing.

!!! none "Running this code"

    All code snippets and commands in this document can be executed directly! The source repo defines the requirements, which can be installed with `poetry install` from the root of the project.

## Why test?

Testing doesn't guarantee that our code works! We might not cover all code paths or edge cases, we might be testing the wrong thing, or there may be bugs in our tests themselves! Unless your code is [formally verified](https://en.wikipedia.org/wiki/Formal_verification) it's still possible to introduce bugs despite tests.

However, writing tests is the most effective way of preventing bugs in code, and the higher the quality of the tests, the more confidence we can have in our code. Without tests, it's much harder to sure that we're not breaking existing functionality or reintroducing old bugs with out new feature or fix. Think of testing as the main line of defence against introducing bugs!

However, I will also posit that, *tests can directly improve the code being tests*. Code that is easily tested will generally be organised into smaller units of functionality, without side effects. Furthermore, good test coverage will make it much easier improve your code through processes such as *TDD* and *red - green - refactor*.

### What types of tests are there?

- Unit testing
- Smoke testing
- Integration testing

We'll mostly be focusing on unit testing.

### What does good look like?

- Run quickly - Slow tests slow down development iterations and mean developers are more likely to skip running then.
- Are isolated - They don't rely on external resources such as databases or HTTP APIs. They don't have side affects, such as saving files that later need to be cleaned up by hand.
- Are deterministic - There is no randomness, reducing the probability of a test changing status when the code hasn't changed. There's nothing more frustrating than flaky tests.
- Are run automatically - Test automation ensures tests are run! This most commonly achieved by CICD pipelines.
- Are simple - If the tests are complicated and hard to understand, they'll be harder to update as requirements and functionality changes either leading to bugs or lower test coverage.

### Arrange, Act, Assert

A useful framework for writing unit tests is *Arrange, Act, Assert*. The basic principle is to split your tests into three logical sections. Firstly, set up the test case, eg. create any required objects, such as inputs and expected outputs. Then *act* - call the functionality that you are testing. Finally validate that your assumptions hold true.

## Fundamentals of Pytest

[Pytest](https://docs.pytest.org/) is the de facto third party library for unit testing in Python. It's an extensive, powerful library, and this document will cover a small subset of it's features.

### Test cases

Pytest will run test cases starting `test_` in modules starting with `test_` in the directory you supply.

An example of a test using [`unittest`](https://docs.python.org/3/library/unittest.html), the standard library unit testing module:

``` python
--8<-- "tests/test_unittest.py::26"
```

Compared with implementing the same test in pytest:

``` python
--8<-- "tests/test_unittest.py:29"
```

Additionally, pytest has no problem also running unittest test cases. Both of these test cases can be run as follows:

```bash
poetry run pytest tests/test_unittest.py
```

### Fixtures

Fixtures are pieces of setup & teardown code which can be reused across tests.

Given some basic code:

``` python
--8<-- "tests/test_fixture.py:0:12"
```

We can create an example user which is reused between tests.

``` python
--8<-- "tests/test_fixture.py:15:"
```

```bash
poetry run pytest tests/test_fixture.py
```

### Marks

Marks allow you to annotate and label your test cases, and pytest comes with a number of built in markers.

``` python
--8<-- "tests/test_mark.py:0:17"
```

You can also define your own markers. Some markers have their own effects, and markers can be selected with the `-m` flag.


``` python
--8<-- "tests/test_mark.py:18:"
```

Running this suite gives us:

```bash
poetry run pytest -vv tests/test_mark.py -m "not slow"
# 1 passed, 1 skipped, 1 deselected, 1 xfailed in 0.10s
```

### Parametrisation

Pytest "parametrize" is a powerful tool for running the same test across different pieces of data. it uses a special mark which accepts as arguments a string of the parameter names and a list of test cases parameters.

``` python
--8<-- "tests/test_parametrisation.py"
```

Running this module will create three test cases for each row.

```bash
poetry run pytest -vvv tests/test_parametrisation.py
# tests/test_parametrisation.py::test_mul[2-2-4] PASSED
# tests/test_parametrisation.py::test_mul[1-2-2] PASSED
# tests/test_parametrisation.py::test_mul[-1-2--2] PASSED
```

### Expected failures

Sometimes we want to check that our code fails in the way we expect it to fail. We can use pytest's `raises` to do exactly this:

``` python
--8<-- "tests/test_raises.py:0:19"
```

If our code doesn't raise the specified exception, the test will fail!

``` python
--8<-- "tests/test_raises.py:21:"
```

Running this suite gives us one pass and one (expected) failure:

```bash
poetry run pytest -vv tests/test_raises.py
# tests/test_raises.py::test_tantrum PASSED
# tests/test_raises.py::test_meditate XFAIL
```

### Configuration

Pytest configuration can be stored in pyproject.toml files. Additionally, it can be extended and modified in a very powerful (but somewhat complicated) way by implementing various hooks and callbacks. Pytest will automatically discover and use fixtures and extensions which are defined in a file call `conftest.py` at the root of your test directory. Read the [docs](https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files) for a more thorough introduction.

## Other Useful Tools

### Tempfile

Sometimes you want to test writing to a file or directory - the built in [tempfile](https://docs.python.org/3/library/tempfile.html) module allows you to make fixtures that clean up after themselves.

``` python
--8<-- "tests/test_tempfile.py"
```

The following doesn't leave any files behind.

```bash
poetry run pytest tests/test_tempfile.py
```

### Doctests

[Doctests](https://docs.python.org/3/library/doctest.html) run the code snippets in docstrings, providing a very easy way to test basic functionality of simple functions while also providing working examples.

Doctests are part of the standard library machinery, however, can also be run by pytest with:

```bash
poetry run pytest --doctest-modules <path-to-tests>
```

We've already seen doctests in our very first example!

``` python
--8<-- "tests/test_fibonacci.py"
```

Eg.

```bash
poetry run pytest --doctest-modules tests/test_fibonacci.py
```

### VCRpy

Allows us to save and replay our HTTP requests (cassettes).

``` python
--8<-- "tests/test_intensity.py"
```

### See also

- [Unittest.mock](https://docs.python.org/3/library/unittest.mock.html) for substituting objects for reproducibility & avoiding side effects.
- [Freezegun](https://github.com/spulec/freezegun) - For freezing time
- [Factoryboy](https://factoryboy.readthedocs.io/en/stable/) - For generating test data based on your classes
