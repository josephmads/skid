from django.test import TestCase

from users.forms import *

# Create your tests here.

class TagFormsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Material.objects.create(material='leather')
        Skill.objects.create(skill='sewing')
        WorkType.objects.create(work_type='production')

    def test_add_material_valid_form(self):
        data = {'material': 'iron'}
        form = MaterialForm(data=data)
        self.assertTrue(form.is_valid())

    def test_add_skill_valid_form(self):
        data = {'skill': 'blacksmithing'}
        form = SkillForm(data=data)
        self.assertTrue(form.is_valid())

    def test_add_work_type_valid_form(self):
        data = {'work_type': 'prototype'}
        form = WorkTypeForm(data=data)
        self.assertTrue(form.is_valid())

    def test_add_material_not_valid_form(self):
        material = Material.objects.get(id=1)
        data = {'material': material.material}
        form = MaterialForm(data=data)
        self.assertFalse(form.is_valid())
    
    def test_add_skill_not_valid_form(self):
        skill = Skill.objects.get(id=1)
        data = {'skill': skill.skill}
        form = SkillForm(data=data)
        self.assertFalse(form.is_valid())

    def test_add_work_type_not_valid_form(self):
        work_type = WorkType.objects.get(id=1)
        data = {'work_type': work_type.work_type}
        form = WorkTypeForm(data=data)
        self.assertFalse(form.is_valid())

class ProfileUpdateFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username='testertim',
            first_name='Tim',
            last_name='Timons',
            email='tim.timons@test.test',
        )

        Profile.objects.filter(id=1).update(
            business_name="Tim's Testing Inc.",
            email_public='tim.public@test.test'
        )

    def test_profile_update_valid_form(self):
        profile = Profile.objects.get(id=1)
        data = {
            'business_name': profile.business_name,
            'email_public': profile.email_public,
            }
        form = ProfileUpdateForm(data=data)
        self.assertTrue(form.is_valid())

class IdeaFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(
            username='testertim',
            first_name='Tim',
            last_name='Timons',
            email='tim.timons@test.test',
        )

        Idea.objects.create(
            author=test_user,
            title='Testing Ideas',
            text='This is a test.',
        )
        
    def test_idea_post_valid_form(self):
        idea = Idea.objects.get(slug='testing-ideas')
        data = {
            'author':idea.author,
            'title':idea.title,
            'text':idea.text,
            }

        form = IdeaForm(data=data)
        self.assertTrue(form.is_valid())
        
class CommentFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(
            username='testertim',
            first_name='Tim',
            last_name='Timons',
            email='tim.timons@test.test',
        )

        test_idea = Idea.objects.create(
            author=test_user,
            title='Testing Ideas',
            text='This is a test.',
        )

        Comment.objects.create(
            idea=test_idea,
            commenter=test_user,
            text='This is a comment.'
        )

    def test_comment_post_valid_form(self):
        comment = Comment.objects.get(id=1)
        data = {
            'idea':comment.idea,
            'commenter':comment.commenter,
            'text':comment.text
        }

        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())
