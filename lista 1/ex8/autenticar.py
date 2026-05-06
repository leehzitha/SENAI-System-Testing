def autenticar(user, password):
    usuario = "admin"
    senha = 1234
    if user != usuario or senha != password:
        return "Invalid user or password"
    return "Welcome!"