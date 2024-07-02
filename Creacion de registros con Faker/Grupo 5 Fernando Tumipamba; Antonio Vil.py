# Grupo 5 Fernando Tumipamba; Antonio Villegas; Leonardo Carvajal; Martin Aldas
# 500 registros

from faker import Faker
import random

fake = Faker()

# Función para truncar texto a una longitud máxima
def truncate(text, max_length):
    return text[:max_length] if len(text) > max_length else text

# Generar registros para la tabla Artista
artistas = []
for i in range(1, 101):  # Generando 100 artistas
    artista = {
        "ID_Artista": i,
        "nombreArtista": truncate(fake.first_name(), 10),
        "apellidoArtista": truncate(fake.last_name(), 10),
        "seudonimo": truncate(fake.user_name(), 10),
        "genero": truncate(fake.word(ext_word_list=['Rock', 'Pop', 'Jazz', 'Classical', 'HipHop', 'Electronic']), 10)
    }
    artistas.append(artista)

# Generar registros para la tabla Asiento
asientos = []
for i in range(1, 101):  # Generando 100 asientos
    asiento = {
        "ID_Asiento": i,
        "localIdeal": truncate(fake.word(ext_word_list=['VIP', 'General', 'Balcony']), 10),
        "bloque": truncate(fake.word(ext_word_list=['A', 'B', 'C', 'D']), 10),
        "fila": fake.random_int(min=1, max=20),
        "numero": fake.random_int(min=1, max=50),
        "costo": round(fake.random_number(digits=5, fix_len=True) / 100, 2)
    }
    asientos.append(asiento)

# Generar registros para la tabla Lugar
lugares = []
for i in range(1, 11):  # Generando 10 lugares
    lugar = {
        "ID_Lugar": i,
        "nombreLug": truncate(fake.company(), 10),
        "capacidad": fake.random_int(min=100, max=10000),
        "direccion": truncate(fake.address(), 10)
    }
    lugares.append(lugar)

# Generar registros para la tabla Evento
eventos = []
for i in range(1, 51):  # Generando 50 eventos
    evento = {
        "ID_Evento": i,
        "ID_Lugar": random.randint(1, 10),
        "nombreGira": truncate(fake.catch_phrase(), 10),
        "fecha": fake.date_between(start_date='-1y', end_date='+1y').strftime('%Y-%m-%d'),
        "horaInicio": fake.time(),
        "horaFin": fake.time()
    }
    eventos.append(evento)

# Generar registros para la tabla ArtistaXEvento sin duplicados
artista_x_eventos = []
combinaciones = set()
while len(artista_x_eventos) < 200:  # Generando 200 registros de Artista por Evento
    id_artista = random.randint(1, 100)
    id_evento = random.randint(1, 50)
    combinacion = (id_artista, id_evento)
    if combinacion not in combinaciones:
        combinaciones.add(combinacion)
        artista_x_evento = {
            "ID_Artista": id_artista,
            "ID_Evento": id_evento
        }
        artista_x_eventos.append(artista_x_evento)

# Generar registros para la tabla AsientoXEvento sin duplicados
asiento_x_eventos = []
combinaciones_asiento = set()
while len(asiento_x_eventos) < 200:  # Generando 200 registros de Asiento por Evento
    id_asiento = random.randint(1, 100)
    id_evento = random.randint(1, 50)
    combinacion_asiento = (id_asiento, id_evento)
    if combinacion_asiento not in combinaciones_asiento:
        combinaciones_asiento.add(combinacion_asiento)
        asiento_x_evento = {
            "ID_Asiento": id_asiento,
            "ID_Evento": id_evento
        }
        asiento_x_eventos.append(asiento_x_evento)

# Generar registros para la tabla Ticket
tickets = []
for i in range(1, 301):  # Generando 300 tickets
    ticket = {
        "ID_Ticket": i,
        "ID_Evento": random.randint(1, 50),
        "codigoTic": truncate(fake.uuid4(), 10)
    }
    tickets.append(ticket)

# Generar registros para la tabla MetodoPago
metodos_pago = []
for i in range(1, 6):  # Generando 5 métodos de pago
    metodo_pago = {
        "ID_MetodoPago": i,
        "metodoPag": truncate(fake.credit_card_provider(), 10)
    }
    metodos_pago.append(metodo_pago)

# Generar registros para la tabla Usuario asegurando unicidad en email y celular
usuarios = []
emails = set()
celulares = set()
for i in range(1, 101):  # Generando 100 usuarios
    email = truncate(fake.email(), 25)
    celular = truncate(fake.phone_number(), 10)
    while email in emails:
        email = truncate(fake.email(), 25)
    while celular in celulares:
        celular = truncate(fake.phone_number(), 10)
    emails.add(email)
    celulares.add(celular)
    usuario = {
        "ID_Usuario": i,
        "nombre": truncate(fake.first_name(), 10),
        "apellido": truncate(fake.last_name(), 10),
        "email": email,
        "celular": celular,
        "telefono": truncate(fake.phone_number(), 10),
        "fechaNac": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d')
    }
    usuarios.append(usuario)

# Generar registros para la tabla Compra
compras = []
for i in range(1, 501):  # Generando 500 compras
    compra = {
        "ID_Compra": i,
        "ID_Usuario": random.randint(1, 100),
        "ID_Ticket": random.randint(1, 300),
        "ID_MetodoPago": random.randint(1, 5),
        "iva": round(random.uniform(0.1, 0.2), 1),
        "codigoCompr": truncate(fake.uuid4(), 10),
        "fechaCompra": fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
    }
    compras.append(compra)

# Generar código SQL para insertar los datos generados
def generate_insert_sql(table_name, data):
    keys = data[0].keys()
    columns = ', '.join(keys)
    values = ', '.join([f"({', '.join(map(repr, record.values()))})" for record in data])
    return f"INSERT INTO {table_name} ({columns}) VALUES {values};"

# Crear el código SQL para cada tabla
sql_artistas = generate_insert_sql("Artista", artistas)
sql_asientos = generate_insert_sql("Asiento", asientos)
sql_lugares = generate_insert_sql("Lugar", lugares)
sql_eventos = generate_insert_sql("Evento", eventos)
sql_artista_x_eventos = generate_insert_sql("ArtistaXEvento", artista_x_eventos)
sql_asiento_x_eventos = generate_insert_sql("AsientoXEvento", asiento_x_eventos)
sql_tickets = generate_insert_sql("Ticket", tickets)
sql_metodos_pago = generate_insert_sql("MetodoPago", metodos_pago)
sql_usuarios = generate_insert_sql("Usuario", usuarios)
sql_compras = generate_insert_sql("Compra", compras)

# Guardar el código SQL generado en un archivo de texto
with open('insert_data.sql', 'w') as f:
    f.write(sql_artistas + '\n')
    f.write(sql_asientos + '\n')
    f.write(sql_lugares + '\n')
    f.write(sql_eventos + '\n')
    f.write(sql_artista_x_eventos + '\n')
    f.write(sql_asiento_x_eventos + '\n')
    f.write(sql_tickets + '\n')
    f.write(sql_metodos_pago + '\n')
    f.write(sql_usuarios + '\n')
    f.write(sql_compras + '\n')
