import pytest

# Whether the tests are running in mayapy or not.
HAS_MAYA: bool
try:
    import maya.standalone
except ImportError:
    HAS_MAYA = False
else:
    HAS_MAYA = True


def pytest_sessionstart(session: pytest.Session):
    # Initialize maya standalone only if it is running in mayapy.
    if HAS_MAYA:
        maya.standalone.initialize()


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    # Uninitialize maya standalone only if it is running in mayapy.
    if HAS_MAYA:
        maya.standalone.uninitialize()
