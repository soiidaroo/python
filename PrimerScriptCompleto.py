#!/usr/bin/python3

print('Bienvenido a mi primer programa de escaneo')

import nmap

ip_add = input('INGRESE LA IP A ESCANEAR: ')
scanner = nmap.PortScanner()

print('LA IP QUE INGRESO ES: ',ip_add)
type(ip_add)

respuesta = input("""
Por favor seleccione el tipo de escaneo
    1 Sistema Operativo
    2) Puertos UDP
""")

print('Su seleccion fue: ', respuesta)

if respuesta == '1':
    before = input('Indique desde que puerto quiere empezar el escaneo: ')
    after = input('Indique hasta que puerto quiere finalizar el escaneo: ')
    print(f"""
    Nmap Version: {scanner.nmap_version()}
    -----------------------------------
    Iniciando el escaneo...
    Por favor aguarde a que finalice...
    -----------------------------------
    """)
    scanner.scan(ip_add, before+'-'+after, '-O', '-v')
    print(f"""
    =======================================
    DATOS OBJETIVO
    IP: {scanner[ip_add]['addresses']['ipv4']}
    Estado IP: {scanner[ip_add].state()}
    MAC: {scanner[ip_add]['addresses']['mac']}
    VENDOR: {scanner[ip_add]['vendor'][scanner[ip_add]['addresses']['mac']]}
    =======================================
    """)
    if len(scanner[ip_add].all_protocols()) > 0:
        print('=================== PUERTOS TCP ESCANEADOS ===================')
        for port in scanner[ip_add]['tcp']:
            if scanner[ip_add]['tcp'][port]['state'] == 'open':
                print(f"""
    .................................................
        PUERTO: {port}
        STATUS: {scanner[ip_add]['tcp'][port]['state']}
        NOMBRE: {scanner[ip_add]['tcp'][port]['name']}
        PRODUCTO: {scanner[ip_add]['tcp'][port]['product']}
        VERSION: {scanner[ip_add]['tcp'][port]['version']}
    .................................................
                """)
            else:
                print(f"""
    .................................................
        PUERTO: {port}
        STATUS: {scanner[ip_add]['tcp'][port]['state']}
        NOMBRE: {scanner[ip_add]['tcp'][port]['name']}
        PRODUCTO: {scanner[ip_add]['tcp'][port]['product']}
        VERSION: {scanner[ip_add]['tcp'][port]['version']}
    .................................................
                """)
    else:
        print("""
-----------------------------------
No se han encontrado puertos TCP.
-----------------------------------
        """)
elif respuesta == '2':
    before = input('Indique desde que puerto quiere empezar el escaneo: ')
    after = input('Indique hasta que puerto quiere finalizar el escaneo: ')
    print(f"""
    Nmap Version: {scanner.nmap_version()}
    -----------------------------------
    Iniciando el escaneo...
    Por favor aguarde a que finalice...
    -----------------------------------
    """)
    scanner.scan(ip_add, before+'-'+after, '-sU', '-v')
    print(f"""
    =======================================
    DATOS OBJETIVO
    IP: {scanner[ip_add]['addresses']['ipv4']}
    Estado IP: {scanner[ip_add].state()}
    MAC: {scanner[ip_add]['addresses']['mac']}
    VENDOR: {scanner[ip_add]['vendor'][scanner[ip_add]['addresses']['mac']]}
    =======================================
    """)
    
    if len(scanner[ip_add].all_protocols()) > 0:
        print('=================== PUERTOS UDP ESCANEADOS ===================')
        for port in scanner[ip_add]['udp']:
            if scanner[ip_add]['udp'][port]['state'] == 'open':
                print(f"""
    .................................................
        PUERTO: {port}
        STATUS: {scanner[ip_add]['udp'][port]['state']}
        NOMBRE: {scanner[ip_add]['udp'][port]['name']}
        PRODUCTO: {scanner[ip_add]['udp'][port]['product']}
        VERSION: {scanner[ip_add]['udp'][port]['version']}
    .................................................
                """)
            else:
                print(f"""
    .................................................
        PUERTO: {port}
        STATUS: {scanner[ip_add]['udp'][port]['state']}
        NOMBRE: {scanner[ip_add]['udp'][port]['name']}
        PRODUCTO: {scanner[ip_add]['udp'][port]['product']}
        VERSION: {scanner[ip_add]['udp'][port]['version']}
    .................................................
                """)
    else:
        print("""
-----------------------------------
No se han encontrado puertos UDP.
-----------------------------------
        """)

print("""
-----------------------------------
|                                  |
|                                  |
|     El escaneo a finalizado      | 
|                                  |
|                                  |
-----------------------------------
Ejecuta nuevamente el programa para volver a escanear.
""")