ip_bloqueadas = ["192.168.1.50","10.0.0.5","172.16.0.8","192.168.1.100"]
primer_ip= ip_bloqueadas.pop(0)
print("IP liberada")
print(primer_ip)
ip_bloqueadas.insert(0,"10.99.99.1")
print(ip_bloqueadas)
indice= ip_bloqueadas.index("172.16.0.8")
print("Esta ubicada en el indice: ")
print(indice)

