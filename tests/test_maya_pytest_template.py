from .conftest import HAS_MAYA

# Safeguard maya imports to avoid test discovery errors
if HAS_MAYA:
    import maya_pytest_template
    from maya import cmds


def test_version():
    assert maya_pytest_template.__version__ == "0.0.1"


def test_create_node():
    node = cmds.createNode("transform")
    assert node == "transform1"
