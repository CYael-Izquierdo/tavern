from assertpy import assert_that, soft_assertions


def check_projects(response):
    r_json = response.json()
    projects = r_json.get('projects')
    with soft_assertions():
        assert_that(len(projects)).is_less_than_or_equal_to(25)
        for project in projects:
            assert_that(project.get('id')).is_type_of(int)
            # assert_that(project.get('name')).is_instance_of(str)
            # assert_that(project.get('identifier')).is_instance_of(str)
            # assert_that(project.get('description')).is_instance_of(str)
            assert_that(project.get('status')).is_type_of(int)
            assert_that(project.get('is_public')).is_type_of(bool)



