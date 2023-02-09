# SKID | Skills x Ideas

## Where Skills and Ideas Connect

This is a website for people with skills to collaborate with people with ideas.
This project was created as my capstone for the CodingNomads Django Web Development Course.

## Features

1. Directory of users who have skills in a given field or fields.
2. Directory of ideas for users to connect with their skills.
3. Users are able to add skills, materials and type of work to database for all users to access.
4. API available to GET Users, Ideas, Skills, Materials, and WorkType data.
5. API available to POST Skills, Materials, and WorkType data.

Users can sort both the USERS and IDEAS directories by the *Skill*, *Material*, or *Type of Work* that they are looking for.

## Getting Started

If you would like to test the live website visit [sk-id.info](http://sk-id.info):

- You can create an account with a username, password, first name, and last name (It doesn't need to be your real name).
- Fill out more profile detals.
- Create an Idea.
- Add Skills, Materials, or Types of Work that all users can add to their profiles or Ideas.

If you would like to download or clone this project and try it with the Django development server:

- Install requirements.txt in a virtual environment.
- Create a file called `.env` in the project's base directory with the following two lines:

    ```env
    SECRET_KEY='<replace with a secret key>'
    DEBUG='True'
    ```

## TODO

*This project is still in progress. I will continue to add features so that SKID can be as useful of a website as possible. Upcoming features are tracked in this repo's [Issues](https://github.com/josephmads/skid/issues) page.*

## Credit

The tagging system I used for the *Skill*, *Material*, and *Type of Work* tags was adapted from the [CtrlZ Blog](https://ctrlzblog.com/how-to-add-tags-to-your-blog-a-django-manytomanyfield-example/) by Alice Ridgway.
