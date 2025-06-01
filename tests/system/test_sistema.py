import unittest
from app import app

class SistemaTestCase(unittest.TestCase):

    def setUp(self):
        # Configura el cliente de pruebas de Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_pagina_principal(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Iniciar Sesi', response.data)

    def test_login_invalido(self):
        response = self.app.post('/login', data=dict(
            username='usuario_invalido',
            password='malacontra'
        ), follow_redirects=True)
        self.assertIn(b'Credenciales incorrectas', response.data)

    def test_login_valido_y_logout(self):
        response = self.app.post('/login', data=dict(
            username='admin',
            password='1234'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cerrar sesi', response.data)

        logout = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(logout.status_code, 200)
        self.assertIn(b'Iniciar Sesi', logout.data)

if __name__ == '__main__':
    unittest.main()
