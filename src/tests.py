from django.test import TestCase
from src.models import Consecucion, Objetivo


class ObjetivoTestCase(TestCase):
    objetivo = None

    def setUp(self):
        self.objetivo = Objetivo.objects.create(
            descripcion='description for test 1', 
            metrica='_test 1'
        )

        Consecucion.objects.create(
            objetivo = self.objetivo,
            descripcion = 'Mínimo',
            meta = '5.0',
            porcentaje_de_consecucion = '80.0',
        )

        Consecucion.objects.create(
            objetivo = self.objetivo,
            descripcion = 'Media',
            meta = '6.0',
            porcentaje_de_consecucion = '90.0',
        )

        Consecucion.objects.create(
            objetivo = self.objetivo,
            descripcion = 'Maximo',
            meta = '7.0',
            porcentaje_de_consecucion = '100.0',
        )

    def test_objetivo(self):
        """Objetivo correctly asigned"""
        self.objetivo = Objetivo.objects.get(metrica = "_test 1")
        self.assertEqual(self.objetivo.descripcion, 'description for test 1')

    def test_consecution(self):
        """Consecucions correctly asigned"""
        Mínimo = Consecucion.objects.filter(objetivo = self.objetivo.id, descripcion = 'Mínimo').first()
        self.assertEqual(Mínimo.meta, 5.0)
            
        Media = Consecucion.objects.filter(objetivo = self.objetivo.id, descripcion = 'Media').first()
        self.assertEqual(Media.meta, 6.0)
            
        Maximo = Consecucion.objects.filter(objetivo = self.objetivo.id, descripcion = 'Maximo').first()
        self.assertEqual(Maximo.meta, 7.0)
            