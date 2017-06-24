import check_pypi_name


# TODO: Convert this to a doctest, doctest exists, but coverage is not yet configured to work properly with doctests.
def test_known_package_name():
    assert check_pypi_name.check_pypi_name('requests')


# TODO: Convert this to a doctest, doctest exists, but coverage is not yet configured to work properly with doctests.
def test_unknown_package_name():
    assert not check_pypi_name.check_pypi_name('testy_mctest_case_has_a_second_cousin_who_should_never_write_pacakages')
