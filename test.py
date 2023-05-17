import unittest
from datetime import date, datetime
from ejercicios import Ejercicio
from errores_archivos import crea_fichero
import os
from models import User, NewTable
from ai import preguntar_chat_gpt
import openai




class TestEjercicio(unittest.TestCase):
    def setUp(self):
        self.facturas = '2022-05-01'
    def test_ejercicio_str(self):
        ejercicio = Ejercicio('Piernas', 'Respiración profunda', 'Principiante', 10, 'Qigong de las Cinco Áreas', 'Fortalece las piernas y mejora el equilibrio')
        self.assertEqual(str(ejercicio), "\nmusculos = Piernas\ntipo_respiracion = Respiración profunda\nnivel = Principiante\nrepeticiones = 10\ntipo = Qigong de las Cinco Áreas\ndescripcion = Fortalece las piernas y mejora el equilibrio")


    def test_mostrar_facturacion(self):
        today = date.today()
        fecha_facturas = datetime.strptime(self.facturas, '%Y-%m-%d').date()
        dias_transcurridos = (today - fecha_facturas).days
        self.assertGreaterEqual(dias_transcurridos, 13)

    def test_crea_fichero(self):
        fecha = datetime.now().strftime('%Y-%m-%d')
        name = "error_name"
        crea_fichero(name)
        file_path = os.path.join('static', 'errores', f"{fecha}.txt")
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn(name, content)

    def test_user_init(self):
        # Crear un objeto de usuario
        usuario = User('Jose', 'Díaz', 'josemanuel@gmail.com', 'Pilates', 25, 'foto23', 'curcuma')
        # Comprobar que los atributos del usuario se hayan establecido correctamente
        self.assertEqual(usuario.nombre, 'Jose')
        self.assertEqual(usuario.apellidos, 'Díaz')
        self.assertEqual(usuario.email, 'josemanuel@gmail.com')
        self.assertEqual(usuario.curso, 'Pilates')
        self.assertEqual(usuario.edad, 25)
        self.assertEqual(usuario.perfil, 'foto23')
        self.assertEqual(usuario.password, 'curcuma')

    def test_new_table_init(self):
        # Crear un objeto de la tabla de datos
        fecha_inicio = date.today()
        new_table = NewTable(1, fecha_inicio, 'facturas', 'ejercicios', 'cursos')
        # Comprobar que los atributos de la tabla de datos se hayan establecido correctamente
        self.assertEqual(new_table.user_id, 1)
        self.assertEqual(new_table.fecha_inicio, fecha_inicio)
        self.assertEqual(new_table.facturas, 'facturas')
        self.assertEqual(new_table.lista_ejercicios, 'ejercicios')
        self.assertEqual(new_table.cursos, 'cursos')

    def test_preguntar_chat_gpt(self):
        api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = api_key
        prompt = '¿Cuál es tu nombre?'
        respuesta_gpt = preguntar_chat_gpt(prompt)
        self.assertIsNotNone(respuesta_gpt)

if __name__ == '__main__':
    unittest.main()

