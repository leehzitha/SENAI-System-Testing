from autenticar import autenticar

def test_login_valido():
    assert autenticar("admin", 1234) == "Welcome!"

def test_login_user_invalido():
    assert autenticar("user", 1234) == "Invalid user or password"

def test_login_senha_invalida():
    assert autenticar("admin", 0000) == "Invalid user or password"

def test_login_ambos_invalidos():
    assert autenticar("a", 1) == "Invalid user or password"
