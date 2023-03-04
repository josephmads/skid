from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from directory.views import *
from users.models import *

# Create your tests here.

class UserListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user([
            User(username='tim', first_name='Tim', last_name='Timons'),
            User(username='tina', first_name='Tina', last_name='Tester'),
            User(username='dj', first_name='DJ', last_name='Ango'),
            User(username='jim', first_name='Jim', last_name='Craig'),
            User(username='joe', first_name='Joe', last_name='Madsen'),
            User(username='pablo', first_name='Pablo', last_name='Hidalgo'),
        ])

    def test_users_view_url_exists_at_location(self):
        response = self.client.get('/directory/users/')
        self.assertEqual(response.status_code, 200)

    def test_users_view_url_accesible_by_name(self):
        response = self.client.get(reverse('directory:users'))
        self.assertEqual(response.status_code, 200)

    def test_user_list_template_content(self):
        response = self.client.get(reverse('directory:users'))
        self.assertContains(response, '<h2>All Users</h2>')
        self.assertContains(response, 1)
        self.assertContains(response, 2)
        self.assertContains(response, 3)
        self.assertContains(response, 4)
        self.assertContains(response, 5)
        self.assertContains(response, 6)

class UserDetailViewTest(TestCase):

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
        

    def test_user_detail_url_exists_at_location(self):
        response = self.client.get('/directory/users/1/')
        self.assertEqual(response.status_code, 200)

    def test_user_detail_url_accesible_by_name(self):
        response = self.client.get(reverse('directory:user_detail', kwargs={'id': '1'}))
        self.assertEqual(response.status_code, 200)

    def test_user_detail_template_login_required_to_view(self):
        response = self.client.get(reverse('directory:user_detail', kwargs={'id': '1'}))
        self.assertContains(response, "Must be logged in to view this page.")

    def test_user_detail_template_content(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/directory/users/1/')
        self.assertEqual(str(response.context['user']), 'testertim')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Must be logged in to view this page.")

    def test_user_detail_has_profile_content(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/directory/users/1/')
        self.assertContains(response, "tim.public@test.test")

class IdeaListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='testertim',
            first_name='Tim',
            last_name='Timons',
            email='tim.timons@test.test',
        )

        test_user = User.objects.get(id=1)

        Idea.objects.bulk_create([
            Idea(author=test_user, title='Test1', slug='test1', text='this is a test', status='p'),
            Idea(author=test_user, title='Test2', slug='test2', text='this is a test', status='p'),
            Idea(author=test_user, title='Test3', slug='test3', text='this is a test', status='p'),
            Idea(author=test_user, title='Test4', slug='test4', text='this is a test', status='p'),
            Idea(author=test_user, title='Test5', slug='test5', text='this is a test', status='p'),
            Idea(author=test_user, title='Test6', slug='test6', text='this is a test'),
        ])

    def test_idea_list_view_url_exists_at_location(self):
        response = self.client.get('/directory/ideas/')
        self.assertEqual(response.status_code, 200)

    def test_idea_list_view_url_accesible_by_name(self):
        response = self.client.get(reverse('directory:ideas'))
        self.assertEqual(response.status_code, 200)

    def test_idea_list_template_content(self):
        response = self.client.get(reverse('directory:ideas'))
        self.assertContains(response, '<h2>All Ideas</h2>')
        self.assertContains(response, 'Test1')

    def test_no_drafts_in_idea_list_content(self):
        response = self.client.get(reverse('directory:ideas'))
        self.assertNotContains(response, 'Test6')

class IdeaDetailViewTest(TestCase):
    
    def setUp(self):
        test_user = User.objects.create_user(
            username='testertim',
            first_name='Tim',
            last_name='Timons',
            password='te3hjsf82Dst',
            email='tim.timons@test.test',
        )

        test_user.save()

        test_idea = Idea.objects.create(
            author=test_user,
            title='Testing Ideas',
            text='This is a test.',
        )

        Comment.objects.create(
            idea=test_idea,
            commenter=test_user,
            text="This is a comment."
        )

    def test_idea_detail_url_exists_at_location(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/directory/ideas/testing-ideas/')
        self.assertEqual(response.status_code, 200)

    def test_idea_detail_url_accesible_by_name(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get(reverse('directory:idea_detail', kwargs={'slug': 'testing-ideas'}))
        self.assertEqual(response.status_code, 200)

    def test_idea_detail_template_content(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/directory/ideas/testing-ideas/')
        self.assertEqual(str(response.context['user']), 'testertim')
        self.assertContains(response, "This is a test.")

    def test_idea_detail_comment(self):
        self.client.login(username='testertim', password='te3hjsf82Dst')
        response = self.client.get('/directory/ideas/testing-ideas/')
        self.assertContains(response, "This is a comment.")
        