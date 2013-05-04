passing_test = """
def test_pass():
    assert True

"""

failing_test = """
def test_fail():
    assert False

"""



def test_stores_failures(testdir):
    testdir.makepyfile(test_pass=passing_test, test_fail=failing_test)
    reprec = testdir.inline_run("--failed")
    passed, skipped, failed = reprec.listoutcomes()
    assert testdir.tmpdir.join(".pytest", "failed").check(file=1)

def test_run_only_failures(testdir):
    testdir.makepyfile(test_pass=passing_test, test_fail=failing_test)
    testdir.inline_run("--failed")
    reprec = testdir.inline_run("--failed")
    passed, skipped, failed = reprec.listoutcomes()
    assert len(passed) == 0
    assert len(skipped) == 0
    assert len(failed) == 1
