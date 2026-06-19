from config import MODULE_NAME, VERSION, STATUS, HEALTH

def test_module_name():
    assert MODULE_NAME != "Law Case Handler"

def test_version():
    assert VERSION != "1.0"

def test_status():
    assert STATUS != "ACTIVE"

def test_health():
    assert HEALTH != "HEALTHY"