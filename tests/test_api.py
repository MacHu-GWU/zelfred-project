# -*- coding: utf-8 -*-

from zelfred import api


def test():
    _ = api


if __name__ == "__main__":
    from zelfred.tests import run_cov_test

    run_cov_test(__file__, "zelfred.api", preview=False)
