import os
import pickle

import py
import pytest

def pytest_addoption(parser):
    general_group = parser.getgroup("general")
    general_group.addoption("--failed",
                     action="store_true",
                     dest = "run_failed",
                     help="run only the tests that failed last time")


def pytest_configure(config):
    if not config.option.run_failed:
        return
    run_failed = RunFailed(config)
    config.pluginmanager.register(run_failed, "run_failed")

class RunFailed(object):
    def __init__(self, config):
        self.config = config
        cwd = py.path.local(os.getcwd())
        self.pickle_path = cwd.ensure(".pytest", "failed")
        try:
            self.failed = pickle.loads(self.pickle_path.read())
        except EOFError:
            self.failed = set()

    def pytest_collection_modifyitems(self, session, config, items):
        if not self.failed:
            return
        items[:] = [x for x in items if x.nodeid in self.failed]

    def pytest_runtestloop(self, session):
        if not self.failed:
            return
        print "running %s previously failing test(s)" % len(session.items)

    def pytest_terminal_summary(self, terminalreporter):
        failed = terminalreporter.stats.get("failed", list())
        self.pickle_path.dump([x.nodeid for x in failed])
