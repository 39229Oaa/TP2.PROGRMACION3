perfil_usuario={
    "id":8472,
    "username":"dark_knight",
    "password":"hashed_pw_881",
    "email":"dk@mail.com",
    "rol":"admin"
}
perfil_usuario.pop("password",None)
print(perfil_usuario)
perfil_usuario.pop("email",None)
print(perfil_usuario)
for clave, valor in perfil_usuario.items():
    print("Clave Valor")
    print(f"[{clave}] {valor}")
