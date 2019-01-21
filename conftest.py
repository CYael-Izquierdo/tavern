import pytest
from faker import Faker


class DeleteProjectHelper:
    project_name = ''
    project_identifier = ''


@pytest.fixture(name="generate_name")
def generate_name():
    faker = Faker()
    DeleteProjectHelper.project_name = faker.name()
    return DeleteProjectHelper.project_name


@pytest.fixture(name="generate_identifier")
def generate_identifier():
    DeleteProjectHelper.project_identifier = DeleteProjectHelper.project_name.replace(' ', '-').lower()
    return DeleteProjectHelper.project_identifier


@pytest.fixture(name="get_name")
def get_name():
    return DeleteProjectHelper.project_name


@pytest.fixture(name="get_identifier")
def get_identifier():
    return DeleteProjectHelper.project_identifier
