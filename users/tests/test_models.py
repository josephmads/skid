from django.test import TestCase

from users.models import *

# Create your tests here.

class TagModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Material.objects.create(material='iron')
        Material.objects.create(material='Leather')

        Skill.objects.create(skill='blacksmithing')
        Skill.objects.create(skill='Sewing')

        WorkType.objects.create(work_type='production')
        WorkType.objects.create(work_type='Prototype')

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

    def test_material_saves_lowercase(self):
        material = Material.objects.get(id=2)
        self.assertEqual(material.material, 'leather')

    def test_skill_saves_lowercase(self):
        skill = Skill.objects.get(id=2)
        self.assertEqual(skill.skill, 'sewing')

    def test_work_type_saves_lowercase(self):
        work_type = WorkType.objects.get(id=2)
        self.assertEqual(work_type.work_type, 'prototype')
        

class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username='testertim',
            first_name='Tim',
            last_name='Timons',
            email='tim.timons@test.test',
        )

        Profile.objects.filter(id=1).update(
            business_name="Tim's Testing Inc."
        )

    def test_get_absolute_url_for_Profile(self):
        skid_user = Profile.objects.get(id=1)
        self.assertEqual(skid_user.get_absolute_url(), '/directory/users/testertim/')
    
    def test_user_profile_extension(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.first_name, "Tim")
        self.assertEqual(user.profile.business_name, "Tim's Testing Inc.")
        