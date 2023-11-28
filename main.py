
precio = 0

preciototal = 0

codigo = 0

while codigo != "salir":
    print("Menu")
    print(" microndas " "= " "A023D4 " "20 unidades " "40$")
    print(" horno " "= ""POM56S " "10 unidades " "60$")
    print(" refrigerador " "= " "458JM3 " "10 unidades " "90$")
    print(" televisor " "= ""Tl2309a " "5 unidades " "100$")
    print(" computadora " "= " "Ce490n " "5 unidades " "100$")
    print(" kitdepintura " "= " "P87nFb " "20 unidades " "20$")
    print(" cuboruby " "= ""CM91nT " "20 unidades " "20$")
    print(" vaso " "= " "Vv78k39 " "100 unidades " "1$")
    print(" inodoro " "= ""P1289s " "10 unidades " "50$")
    print(" papel " "= " "Piu923e " "100 unidades " "1$")
    print("Si quieres salirte pon salir en vez de el codigo")

    codigo = input("Pon el codigo por favor ")

    if codigo == "salir":
        break


    unidadacomprar = int(input("Cual es el numero de unidad del producto que vas a comprar ")) 

    if codigo == "A023D4":
        if int(unidadacomprar) > 20:
            print("Fuera de unidades")
        else:
            precio = 40 * int(unidadacomprar)
            preciototal = preciototal + precio
    elif codigo == "POM56S":
        if int(unidadacomprar) > 10:
            print("Fuera de unidades")
        else:
            precio = 60 * int(unidadacomprar)
            preciototal = preciototal + precio
    elif codigo == "458JM3":
        if int(unidadacomprar) > 10:
            print("Fuera de unidades")
        else:
            precio = 90 * int(unidadacomprar)
            preciototal = preciototal + precio
    elif codigo == "Tl2309a":
        if int(unidadacomprar) > 5:
            print("Fuera de unidades")
        else:
            precio = 100 * int(unidadacomprar)
            preciototal = preciototal + precio
    elif codigo == "Ce490n":
        if int(unidadacomprar) > 5:
            print("Fuera de unidades")
        else:
            precio = 100 * int(unidadacomprar)
            preciototal = preciototal + precio
    elif codigo == "P87nFb":
        if int(unidadacomprar) > 20:
            print("Fuera de unidades")
        else:
            precio = 20 * int(unidadacomprar)
            preciototal = preciototal + precio
    elif codigo == "CM91nT":
        if int(unidadacomprar) > 20:
            print("Fuera de unidades")
        else:
            precio = 20 * int(unidadacomprar)
            preciototal = preciototal + precio
    elif codigo == "Vv78k39":
        if int(unidadacomprar) > 100:
            print("Fuera de unidades")
        else:
            precio = 1 * int(unidadacomprar)
            preciototal = preciototal + precio
    elif codigo == "P1289s":
        if int(unidadacomprar) > 10:
            print("Fuera de unidades")
        else:
            precio = 50 * int(unidadacomprar)
            preciototal = preciototal + precio
    elif codigo == "Piu923e":
        if int(unidadacomprar) > 100:
            print("Fuera de unidades")
        else:
            precio = 1 * int(unidadacomprar)
            preciototal = preciototal + precio

print(f"Total = {preciototal}")    