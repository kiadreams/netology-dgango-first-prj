import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        if '_quantity' not in kwargs:
            kwargs['_quantity'] = 7
        return baker.make(Course, *args, **kwargs)

    return factory


# QUANTITY = 7


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    courses: list = course_factory(_quantity=1)
    course_id = courses[0].id
    response = client.get(f'/api/v1/courses/{course_id}/')
    first_course = response.json()
    assert response.status_code == 200
    assert isinstance(first_course, dict)
    assert first_course.get('id') == courses[0].id


@pytest.mark.django_db
def test_get_list_of_courses(client, course_factory):
    courses: list = course_factory()
    count_of_courses = len(courses)
    response = client.get('/api/v1/courses/')
    list_of_courses = response.json()
    assert response.status_code == 200
    assert isinstance(list_of_courses, list)
    assert len(list_of_courses) == count_of_courses
    for i in range(count_of_courses):
        assert list_of_courses[i].get('id') == courses[i].id


@pytest.mark.django_db
def test_filter_by_course_name(client, course_factory):
    courses: list = course_factory()
    test_name = courses[5].name
    response = client.get('/api/v1/courses/', {'name': test_name})
    list_of_courses = response.json()
    assert response.status_code == 200
    assert isinstance(list_of_courses, list)
    assert len(list_of_courses) == 1
    assert list_of_courses[0].get('name') == test_name


@pytest.mark.django_db
def test_filter_by_course_id(client, course_factory):
    courses: list = course_factory()
    test_id = (courses[3].id, courses[4].id)
    response = client.get('/api/v1/courses/', {'id': test_id})
    list_of_courses = response.json()
    assert response.status_code == 200
    assert isinstance(list_of_courses, list)
    assert len(list_of_courses) == 2
    for i in range(2):
        assert list_of_courses[i].get('id') == test_id[i]


@pytest.mark.django_db
def test_create_course(client):
    course = {'name': 'Плавание'}
    response = client.post('/api/v1/courses/', data=course)
    curr_course = response.json()
    assert response.status_code == 201
    assert isinstance(curr_course, dict)
    assert curr_course.get('name') == course['name']


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses: list = course_factory()
    new_course_name = 'Плавание'
    response = client.patch(
        f'/api/v1/courses/{courses[3].id}/',
        {'name': new_course_name},
    )
    curr_course = response.json()
    assert response.status_code == 200
    assert isinstance(curr_course, dict)
    assert curr_course.get('name') == new_course_name


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses: list = course_factory()
    new_course_name = 'Плавание'
    response = client.patch(
        f'/api/v1/courses/{courses[3].id}/',
        {'name': new_course_name},
    )
    curr_course = response.json()
    assert response.status_code == 200
    assert isinstance(curr_course, dict)
    assert curr_course.get('name') == new_course_name


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses: list = course_factory()
    course_id = courses[3].id
    response = client.delete(f'/api/v1/courses/{course_id}/')
    assert response.status_code == 204
