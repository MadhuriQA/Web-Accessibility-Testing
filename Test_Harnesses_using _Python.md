# Overview

-Test harness or automated test framework is a collection of software & test data configured to test a program unit by running it under varying conditions and monitoring its behavior and outputs.

**It has 2 main parts-** 
1)	Test execution engine
2)	Test script repository

**Automation of tests** – they can call functions with supplied parameters & print out & compare the results to the desired value.

-Test harness is a hook to the developed code which can be tested using automation framework.

# Objectives of a test harness **(fulfilled by unit test framework tools, stubs or drivers)** -
1)	Automate the testing process
2)	Execute test suites of test cases
3)	Generate associated test reports

# Benefits–
1)	Increased productivity due to automation of testing process.
2)	Useful for regression testing
3)	High quality of software components
4)	Repeated ability of subsequent test runs
5)	Offline testing
6)	Access to conditions and/or use cases that are otherwise difficult to simulate(eg- load)

# Python testing Frameworks-
1)	Zope.testing –The zope.testing package only supports traditional Python test styles like unittest and doctest, and not the radically simpler styles permitted by the more recent frameworks.
2)	Py.test – The elegant and Pythonic idioms it introduced for test writing have made it possible for test suites to be written in a far more compact style than was possible before
3)	Nose – support the same test idioms that had been pioneered by py.test, but in a package that is easier to install and maintain.

# Python test harnesses through py.test

- Using “assert” - Assertions are a systematic way to check that the internal state of a program is as the programmer expected, with the goal of catching bugs. In particular, they're good for catching false assumptions that were made while writing the code, or abuse of an interface by another programmer. Assertions are not a substitute for unit tests or system tests, but rather a complement. Because assertions are a clean way to examine the internal state of an object or function, they provide "for free" a clear-box assistance to a black-box test that examines the external behaviour.

- Example - assertion $ pytest failure_demo.py
```
======= test session starts ========
 arg1 = 3, arg2 = 6
 def test_gen(arg1, arg2):
 >    assert arg1 * 2 < arg2
 Execution ->  assert (3 * 2) < 6
 failure_demo.py:16: AssertionError
```
 _______TestFailing.test_simple________
 
 ```
 self = <failure_demo.TestFailing object at 0xdeadbeef>
 def test_compare(self):
 def f():
    return 42
 def g():
    return 43
 > assert f() == g()
Execution->    assert 42 == 43
Execution->    +  where 42 = <function TestFailing.test_simple.<locals>.f at 0xdeadbeef>()
Execution->    +  and   43 = <function TestFailing.test_simple.<locals>.g at 0xdeadbeef>()
failure_demo.py:29: AssertionError
```
_______ TestSpecialisedExplanations.test_eq_text ________
```
self = <failure_demo.TestSpecialisedExplanations object at 0xdeadbeef>
		 def test_eq_text(self):
>       assert 'spam' == 'eggs'
Execution-> AssertionError: assert 'spam' == 'eggs'
Execution-> - spam
Execution-> + eggs
failure_demo.py:43: AssertionError
```
# Places to consider putting assertions:
•	checking parameter types, classes, or values
•	checking data structure invariants
•	checking "can't happen" situations (duplicates in a list, contradictory state variables.)
•	after calling a function, to make sure that its return is reasonable

# TOX -
Tox is a generic virtualenv management and test command line tool you can use for:
•	checking your package installs correctly with different Python versions and interpreters
•	running your tests in each of the environments, configuring your test tool of choice
•	acting as a frontend to Continuous Integration servers, greatly reducing boilerplate and merging CI and shell-based testing.

**Basic example**
First, install tox with pip install tox or easy_install tox. Then put basic information about your project and the test environments you want your project to run in into a tox.ini file residing right next to your setup.py file:
```
Comment - content of: tox.ini , put in same dir as setup.py
[tox]
envlist = py26,py27
[testenv]
deps=pytest       # install pytest in the venvs
commands=py.test  # or 'nosetests'
```
