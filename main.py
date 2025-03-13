#coding=utf=8
#Funcion para calcular el promedio
def calcular_promedio_generacion(cantidadGWh,total_eventos_generacion):
  if total_eventos_generacion == 0:
    return 0
  else:
    return(cantidadGWh / total_eventos_generacion)

print('Programa que identifica la generación de energía en diferentes fuentes')

# Variables
fuente_hidrica = 0
fuente_solar = 0
fuente_eolica = 0
fuente_termica = 0

cantidadGWh_hidrica = 0
cantidadGWh_solar = 0
cantidadGWh_eolica = 0
cantidadGWh_termica = 0

meta_generacionGWh = 5.0
cantidadGWh = 0

# Ciclo While
while cantidadGWh <= meta_generacionGWh:
    tipo_fuente = input('Ingrese el tipo de fuente de energia:').lower()
    if tipo_fuente != 'hidrica' and tipo_fuente != 'solar' and tipo_fuente != 'eolica'      and tipo_fuente != 'termica':
        print('El tipo de fuente ingresada no es valida, vuelva a intentarlo')
        continue
    else:
        try:
            cantidadGWh = float(input('Ingrese la cantidad de GWh que genera la fuente:'))
# Validación de datos
            if cantidadGWh < 0.75 or cantidadGWh > 1.25:
                print('La cantidad de GWh ingresada no es valida, vuelva a intentarlo')
                continue

            if tipo_fuente == 'hidrica':
                fuente_hidrica += 1
                cantidadGWh_hidrica += cantidadGWh

            elif tipo_fuente == 'solar':  
                fuente_solar += 1
                cantidadGWh_solar += cantidadGWh

            elif tipo_fuente == 'eolica':
                fuente_eolica += 1
                cantidadGWh_eolica += cantidadGWh

            elif tipo_fuente == 'termica':
                fuente_termica += 1
                cantidadGWh_termica += cantidadGWh

            cantidadGWh_actual = cantidadGWh_hidrica + cantidadGWh_solar + cantidadGWh_eolica + cantidadGWh_termica
            print(f'La cantidad de GWh registrada es de {cantidadGWh_actual}')

        except ValueError:
            print('El valor ingresado no es valido, vuelva a intentarlo')
            continue

# Calculo de promedios
promedio_hidrica = calcular_promedio_generacion(cantidadGWh_hidrica, fuente_hidrica)
promedio_solar = calcular_promedio_generacion(cantidadGWh_solar, fuente_solar)
promedio_eolica = calcular_promedio_generacion(cantidadGWh_eolica, fuente_eolica)
promedio_termica = calcular_promedio_generacion(cantidadGWh_termica, fuente_termica)

# Resultados
print('Los resultados finales fueron:')
print(f'Hidrica: {fuente_hidrica} eventos, {cantidadGWh_hidrica} GWh, y el promedio {promedio_hidrica} GWh/fuente')
print(f'Solar: {fuente_solar} eventos, {cantidadGWh_solar} GWh, y el promedio {promedio_solar} GWh/fuente')
print(f'Eolica: {fuente_eolica} eventos, {cantidadGWh_eolica} GWh, y el promedio {promedio_eolica} GWh/fuente')
print(f'Termica: {fuente_termica} eventos, {cantidadGWh_termica} GWh, y el promedio {promedio_termica} GWh/fuente')
