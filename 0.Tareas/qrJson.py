import json
import qrcode

# Supongamos que tienes el siguiente objeto JSON:
data = {
    "nombre": "Jorge Rea",
    "edad": 30,
    "ciudad": "Madrid"
}

# Convertir el objeto JSON a una cadena de texto
json_string = json.dumps(data)

# Generar el código QR
img = qrcode.make(json_string)

# Guardar el código QR en un archivo
img.save("mi_codigo_qr.png")

# Si deseas mostrar el código
img.show()
