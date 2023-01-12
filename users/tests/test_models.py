from django.test import TestCase

from users.models import *

# Create your tests here.

class TagModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Material.objects.create(material='iron')
        Skill.objects.create(skill='blacksmithing')
        WorkType.objects.create(work_type='production')

    def test_material_label(self):
        material = Material.objects.get(id=1)
        field_label = material._meta.get_field('material').verbose_name
        self.assertEqual(field_label, 'material')

    def test_skill_label(self):
        skill = Skill.objects.get(id=1)
        field_label = skill._meta.get_field('skill').verbose_name
        self.assertEqual(field_label, 'skill')

    def test_work_type_label(self):
        work_type = WorkType.objects.get(id=1)
        field_label = work_type._meta.get_field('work_type').verbose_name
        self.assertEqual(field_label, 'work type')

class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Profile.objects.create(
            username='testertim',
            first_name='Tim',
            last_name='Timons',
            email_address='tim.timons@test.test',
        )

    def test_get_absolute_url_for_slug(self):
        skid_user = Profile.objects.get(id=1)
        self.assertEqual(skid_user.get_absolute_url(), '/directory/testertim/')