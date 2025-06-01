import unittest
from app import app, get_db
import os
import tempfile

class ClienteIntegrationTest(unittest.TestCase):
    def setUp(self):
        # Configuración de entorno de prueba
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.client = app.test_client()

        with app.app_context():
            db = get_db()
            db.executescript('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    nit_carnet TEXT,
                    plan TEXT,
                    fecha_nac TEXT,
                    fecha_inicio_plan TEXT,
                    fecha_fin_plan TEXT
                );
            ''')
            db.commit()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_insertar_y_listar_cliente(self):
        # Insertar cliente
        response = self.client.post('/clientes', data={
            'nombre': 'Carlos Tester',
            'nit_carnet': '1234567',
            'plan': 'Mensual',
            'fecha_nac': '1990-01-01',
            'fecha_inicio_plan': '2025-06-01',
            'fecha_fin_plan': '2025-07-01'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Verificar que aparece en la lista
        self.assertIn(b'Carlos Tester', response.data)

if __name__ == '__main__':
    unittest.main()
