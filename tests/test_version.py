"""Unit tests for __version__.py."""

import scikit_zhangt20_lvl5


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(scikit_zhangt20_lvl5, "__version__")
    assert scikit_zhangt20_lvl5.__version__ != "0.0.0"
