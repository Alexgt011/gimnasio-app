import unittest
import sqlite3

class TestClientes(unittest.TestCase):
    def setUp(self):
        # Crear la base de datos en memoria
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                nit_carnet TEXT NOT NULL,
                plan TEXT,
                fecha_nac TEXT,
                fecha_inicio_plan TEXT,
                fecha_fin_plan TEXT
            )
        ''')

    def tearDown(self):
        self.conn.close()

    def test_insertar_cliente(self):
        self.cursor.execute('''
            INSERT INTO clientes (nombre, nit_carnet, plan, fecha_nac, fecha_inicio_plan, fecha_fin_plan)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('Juan Perez', '12345678', 'Mensual', '1990-01-01', '2025-06-01', '2025-07-01'))
        self.conn.commit()

        self.cursor.execute("SELECT * FROM clientes WHERE nombre = ?", ('Juan Perez',))
        cliente = self.cursor.fetchone()
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente[1], 'Juan Perez')

    def test_listar_clientes_vacio(self):
        self.cursor.execute("SELECT * FROM clientes")
        resultados = self.cursor.fetchall()
        self.assertEqual(len(resultados), 0)

    def test_eliminar_cliente(self):
        self.cursor.execute('''
            INSERT INTO clientes (nombre, nit_carnet, plan, fecha_nac, fecha_inicio_plan, fecha_fin_plan)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('Maria Lopez', '87654321', 'Anual', '1995-05-05', '2025-06-01', '2026-06-01'))
        self.conn.commit()

        self.cursor.execute("DELETE FROM clientes WHERE nombre = ?", ('Maria Lopez',))
        self.conn.commit()

        self.cursor.execute("SELECT * FROM clientes WHERE nombre = ?", ('Maria Lopez',))
        resultado = self.cursor.fetchone()
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
