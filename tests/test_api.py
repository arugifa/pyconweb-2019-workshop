from workshop.demo import adopt_cats
from workshop.models import Cat


def test_list_cats(client, db):
    cats = adopt_cats()
    result = [Cat(**data) for data in client.get('/cats/').json]

    for actual, expected in zip(result, cats):
        assert actual.name == expected.name
        assert actual.country == expected.country
