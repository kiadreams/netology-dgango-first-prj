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
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    courses: list[Course] = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/1/')
    first_course = response.json()
    assert response.status_code == 200
    assert isinstance(first_course, dict)
    assert len(first_course) == 3
    assert first_course.get('id', None) == courses[0].id


