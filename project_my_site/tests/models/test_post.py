import pytest

from blog_app_jack.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published(post_published):
    assert post_published.title == 'pytest with factory'