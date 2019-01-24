import pytest
from faker import Faker


class ProjectHelper:
    project_name = ''
    project_identifier = ''
    project_description = ''


@pytest.fixture(name="generate_name")
def generate_name():
    faker = Faker()
    ProjectHelper.project_name = faker.name()
    return ProjectHelper.project_name


@pytest.fixture(name="get_name")
def get_name():
    return ProjectHelper.project_name


@pytest.fixture(name="generate_identifier")
def generate_identifier():
    ProjectHelper.project_identifier = ProjectHelper.project_name.replace(' ', '-').lower()
    return ProjectHelper.project_identifier


@pytest.fixture(name="get_identifier")
def get_identifier():
    return ProjectHelper.project_identifier


@pytest.fixture
def generate_description():
    faker = Faker()
    ProjectHelper.project_description = faker.text()
    return ProjectHelper.project_description


@pytest.fixture
def get_description():
    return ProjectHelper.project_description
