from faker import Faker
import sqlite3
import os

fake = Faker()

# Ruta absoluta al archivo gimnasio.db
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../gimnasio.db'))
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Insertar 10 instructores falsos
for i in range(10):
    nombre = fake.name()
    edad = fake.random_int(min=20, max=60)
    direccion = fake.address()
    rol = fake.random_element(elements=["Musculacion", "Aerobicos-Zumba", "Aerobicos-Kombat"])
    turno_ini = fake.random_element(elements=["06:00", "08:00", "14:00", "18:00"])
    turno_fin = fake.random_element(elements=["10:00", "12:00", "16:00", "20:00"])
    user_name = fake.user_name()
    password = "1234"

    cursor.execute("""
    INSERT INTO instructores (nombre, edad, direccion, rol, turno_ini, turno_fin, user_name, password)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (nombre, edad, direccion, rol, turno_ini, turno_fin, user_name, password))

    print(f"✅ Instructor {i+1}: {nombre} - Usuario: {user_name}")

conn.commit()
conn.close()

print("\n🎉 ¡10 instructores generados con éxito!")