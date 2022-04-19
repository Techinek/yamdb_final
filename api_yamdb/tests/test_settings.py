from api_yamdb import settings


class TestSettings:

    def test_settings(self):
        db_settings = settings.DATABASES['default']['ENGINE']
        assert not settings.DEBUG, ('Проверьте, что DEBUG в настройках '
                                    'Django выключен')
        assert db_settings == ('django.db.backends.postgresql',
                               'Проверьте, что используете базу данных '
                               'postgresql')
