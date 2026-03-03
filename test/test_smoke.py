def test_import_src():
    import importlib

    mod = importlib.import_module("src.cli")
    assert hasattr(mod, "main")
