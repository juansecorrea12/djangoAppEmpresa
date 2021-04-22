from rest_framework.test import APITestCase
from empleados.models import Empleados
from puestos.models import Puestos


class TestEmpleadosCRUD(APITestCase):

    def setUp(self):
        self.host = 'http://localhost:8000'
        self.puesto = Puestos.objects.create(
            nombre_cargo='cargo 1',
            salario_cargo=20000,
            descripcion='puesto muy importante',
        )
        self.empleados = Empleados.objects.create(
            nombre='empleado 1',
            apellido='empleado',
            edad=20,
            correo='empleado1@mail.com',
            telefono='11111111',
            ano_antiguedad=3,
            puestos=self.puesto
        )

    def test_get_empleados(self):
        response = self.client.get(f'{self.host}/empleados/')
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(self.empleados.id, response.data[0]['id'])

    def test_post_empleados(self):
        data = {
            "nombre": "empleado 2",
            "apellido": "empleado",
            "edad": 26,
            "correo": "empleado2@hotmail.com",
            "telefono": "3233406565",
            "ano_antiguedad": 3,
            "puestos": [self.puesto.id]
        }
        
        response = self.client.post(f'{self.host}/empleados/', data)
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(Empleados.objects.all().count(), 2)
