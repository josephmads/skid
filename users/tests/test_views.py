from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from users.models import *

# Create your tests here.

class HomePageTest(TestCase):

    def test_homepage_url_exists_at_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_accesible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class TagViewsTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            username='testertim',
            first_name='Tim',
            last_name='Timons',
            password='te3hjsf82Dst',
            email='tim.timons@test.test',
        )

        test_user.save()

        Material.objects.create(material='leather')
        Skill.objects.create(skill='sewing')
        WorkType.objects.create(work_type='prototype')

    # Material
    def test_logged_in_add_material_uses_correct_template(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get(reverse('users:add_material'))
        self.assertEqual(str(response.context['user']), 'testertim')
        self.assertEqual(response.status_code, 200)

    def test_add_material_view_requires_login(self):
        response = self.client.get(reverse('users:add_material'))
        self.assertEqual(response.status_code, 302)

    def test_add_material_url_exists_at_location(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/add-material/')
        self.assertEqual(response.status_code, 200)

    def test_add_material_view_content(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/add-material/')
        self.assertContains(response, 'leather')

    # Skill
    def test_logged_in_add_skill_uses_correct_template(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get(reverse('users:add_skill'))
        self.assertEqual(str(response.context['user']), 'testertim')
        self.assertEqual(response.status_code, 200)

    def test_add_skill_view_requires_login(self):
        response = self.client.get(reverse('users:add_skill'))
        self.assertEqual(response.status_code, 302)

    def test_add_skill_url_exists_at_location(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/add-skill/')
        self.assertEqual(response.status_code, 200)

    def test_add_skill_view_content(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/add-skill/')
        self.assertContains(response, 'sewing')

    # Work Type
    def test_logged_in_add_work_type_uses_correct_template(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get(reverse('users:add_work_type'))
        self.assertEqual(str(response.context['user']), 'testertim')
        self.assertEqual(response.status_code, 200)

    def test_add_work_type_view_requires_login(self):
        response = self.client.get(reverse('users:add_work_type'))
        self.assertEqual(response.status_code, 302)

    def test_add_work_type_url_exists_at_location(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/add-work-type/')
        self.assertEqual(response.status_code, 200)

    def test_add_work_type_view_content(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/add-work-type/')
        self.assertContains(response, 'prototype')

class UserProfileViewsTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            username='testertim',
            first_name='Tim',
            last_name='Timons',
            password='te3hjsf82Dst',
            email='tim.timons@test.test',
        )

        test_user.save()

        profile = Profile.objects.filter(id=1).update(
            business_name="Tim's Testing Inc.",
            email_public="tim.public@test.test",
            phone_number="15555555555",
            address="123 Test Dr.",
            city="Test Town",
            state_province="TX",
            country="USA",
            about="I'm a testing wonk!",
        )

    # User Profile
    def test_logged_in_profile_uses_correct_template(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get(reverse('users:profile', kwargs={'id': '1'}))
        self.assertEqual(str(response.context['user']), 'testertim')
        self.assertEqual(response.status_code, 200)

    def test_profile_view_requires_login(self):
        response = self.client.get(reverse('users:profile', kwargs={'id': '1'}))
        self.assertEqual(response.status_code, 302)

    def test_user_profile_url_exists_at_location(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/1/')
        self.assertEqual(response.status_code, 200)

    def test_user_profile_url_accesible_by_name(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get(reverse('users:profile', kwargs={'id': '1'}))
        self.assertEqual(response.status_code, 200)

    def test_user_profile_has_updated_profile_content(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/1/')
        self.assertContains(response, "tim.public@test.test")
        self.assertContains(response, "Test Town")

    # Edit User Profile
    def test_edit_user_profile_prepopulates_fields(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/1/edit/')
        self.assertContains(response, "Timons")
        self.assertContains(response, "tim.public@test.test")

    def test_edit_user_profile_url_exists_at_location(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/1/edit/')
        self.assertEqual(response.status_code, 200)

    def test_edit_profile_view_requires_login(self):
        response = self.client.get(reverse('users:profile', kwargs={'id': '1'}))
        self.assertEqual(response.status_code, 302)

    def test_edit_user_profile_url_accesible_by_name(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get(reverse('users:edit_profile', kwargs={'id': '1'}))
        self.assertEqual(response.status_code, 200)

class IdeaViewsTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            username='testertim',
            first_name='Tim',
            last_name='Timons',
            password='te3hjsf82Dst',
            email='tim.timons@test.test',
        )

        test_user.save()

        test_idea1 = Idea.objects.create(
            author=test_user,
            title='Test Idea 1',
            text='This is a test.',
            status='p',
        )

        test_idea2 = Idea.objects.create(
            author=test_user,
            title='Test Idea 2',
            text='This is also a test.',
        )

    # Create Idea
    def test_logged_in_create_idea_uses_correct_template(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get(reverse('users:create_idea', kwargs={'id': '1'}))
        self.assertEqual(str(response.context['user']), 'testertim')
        self.assertEqual(response.status_code, 200)

    def test_create_idea_view_requires_login(self):
        response = self.client.get(reverse('users:create_idea', kwargs={'id': '1'}))
        self.assertEqual(response.status_code, 302)

    def test_create_idea_url_exists_at_location(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/1/create-idea/')
        self.assertEqual(response.status_code, 200)

    # Edit Idea
    def test_logged_in_edit_idea_uses_correct_template(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get(reverse('users:edit_idea', kwargs={
            'id': '1',
            'slug': 'test-idea-1',
            }))
        self.assertEqual(str(response.context['user']), 'testertim')
        self.assertEqual(response.status_code, 200)

    def test_edit_idea_view_requires_login(self):
        response = self.client.get(reverse('users:edit_idea', kwargs={
            'id': '1',
            'slug': 'test-idea-1',
            }))
        self.assertEqual(response.status_code, 302)

    def test_edit_idea_url_exists_at_location(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/1/edit-idea/test-idea-1')
        self.assertEqual(response.status_code, 200)

    def test_edit_idea_prepopulates_data(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/1/edit-idea/test-idea-1')
        self.assertContains(response, 'This is a test.')

    # Delete Idea
    def test_logged_in_delete_idea_uses_correct_template(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get(reverse('users:delete_idea', kwargs={
            'id': '1',
            'slug': 'test-idea-1',
            }))
        self.assertEqual(str(response.context['user']), 'testertim')
        self.assertEqual(response.status_code, 200)

    def test_delete_idea_view_requires_login(self):
        response = self.client.get(reverse('users:delete_idea', kwargs={
            'id': '1',
            'slug': 'test-idea-1',
            }))
        self.assertEqual(response.status_code, 302)

    def test_delete_idea_url_exists_at_location(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/1/delete-idea/test-idea-1')
        self.assertEqual(response.status_code, 200)

    # View Ideas
    def test_logged_in_view_ideas_uses_correct_template(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get(reverse('users:view_ideas', kwargs={'id': '1'}))
        self.assertEqual(str(response.context['user']), 'testertim')
        self.assertEqual(response.status_code, 200)

    def test_view_ideas_view_requires_login(self):
        response = self.client.get(reverse('users:view_ideas', kwargs={'id': '1'}))
        self.assertEqual(response.status_code, 302)

    def test_view_ideas_url_exists_at_location(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/1/view-ideas/')
        self.assertEqual(response.status_code, 200)

    def test_view_ideas_table_content(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/users/1/view-ideas/')
        self.assertContains(response, 'Published')
        self.assertContains(response, 'Draft')
