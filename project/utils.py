from assertpy import assert_that, soft_assertions


def check_projects(response):
    r_json = response.json()
    projects = r_json.get('projects')
    with soft_assertions():
        assert_that(len(projects)).is_less_than_or_equal_to(25)
        for project in projects:
            assert_that(project.get('id')).described_as('id').is_not_none().is_type_of(int)
            assert_that(project.get('name')).described_as('name').is_not_none().is_type_of(str)
            assert_that(project.get('identifier')).described_as('identifier').is_not_none().is_type_of(str)
            if project.get('description', False):
                assert_that(project.get('description')).described_as('description').is_not_none().is_type_of(str)
            assert_that(project.get('status')).described_as('status').is_not_none().is_type_of(int)
            assert_that(project.get('is_public')).described_as('is_public').is_not_none().is_type_of(bool)



