from capstone.main import configure_logging


def pytest_configure(config):
    configure_logging()
