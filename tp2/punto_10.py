config_default={
    "timeout": 30,
    "max_retries":3,
    "ssl_verify":True,
    "log_level":"INFO"
}
config_admin={
    "max_retries":5,
    "log_level": "DEBUG",
    "alert_email": "admin@empresa.com"
}
config_default.update(config_admin) 
# config _default diccionario 1 
# config_admi diccionario 2   
# las claves y valor del diccionario 2 reemplaza al diccionario 1
print(config_default)
valores=[config_default.values()]
print(valores)
print(type(valores))