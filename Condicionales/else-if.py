ingreso_mensual = 5000

if ingreso_mensual > 10000:
    print("Tienes un buen ingreso para cualquier parte del mundo")
    
elif ingreso_mensual > 1000:
    print("Tienes un Buen ingreso si vives en latinoamerica")
    
else:
    print("Tus ingresos son muy bajos")
    
#if anidaddos y else if (elif)    
ingreso_mensual = 81000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en Deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Tus Ingresos estan Bien")
    else:
        print("Tus gastos son muy altos, debes organizar tus gastos")
elif ingreso_mensual > 1000:
    print("Tus ingresos son buenos para vivir en Latinoamerica")
    
elif ingreso_mensual > 500:
    print("Tus ingresos estan bien para vivir en Argentina")
    
elif ingreso_mensual > 200: 
    print("Tus ingresos estan bien para vivir en Venezuela")
    
else: 
    print("Tus ingresos son muy bajos para vivir en cualquier pais")