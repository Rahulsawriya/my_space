import mathlib
#import pytest
#import sys

#@pytest.mark.skip(reason="i don't want to run this test case")
def test_calc_total():
	total = mathlib.calc_total(4, 5)
	assert total == 9

#@pytest.mark.skipif(sys.version_info > (3, 5), reason="i don't want to run this test case")
def test_calc_multiply():
	result = mathlib.calc_multiply(10, 3)
	assert result == 30

#note: python -m pytest: execute the all the testcases.
#to run testcases: py.test -v
#find out the reason of skip the test cases: py.test -v -rxs
#pytest -k multiply -v: for run only specific test cases those contain multiply
