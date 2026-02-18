from django.test import TestCase
from django.urls import reverse


class PortfolioPagesTests(TestCase):
    def test_single_page_loads(self):
        response = self.client.get(reverse("profiles:dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_single_page_has_sections(self):
        response = self.client.get(reverse("profiles:dashboard"))
        content = response.content.decode()
        self.assertIn('id="about"', content)
        self.assertIn('id="skills"', content)
        self.assertIn('id="contact"', content)
