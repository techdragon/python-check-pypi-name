import check_pypi_name


def test_known_package_name():
    assert check_pypi_name.check_pypi_name('pip')


def test_package_name_redirect():
    assert check_pypi_name.check_pypi_name('Pip')


def test_unknown_package_name():
    assert not check_pypi_name.check_pypi_name('testy_mctest_case_has_a_second_cousin_who_should_never_write_pacakages')
