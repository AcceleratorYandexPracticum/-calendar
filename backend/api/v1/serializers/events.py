from django.db import transaction
from rest_framework import serializers

from events.models import Calendar, Category, Event


class CalendarSerializer(serializers.ModelSerializer):
    """
    Сериализатор календаря.
    Поле public исключено из выдачи.
    """

    owner = serializers.SlugRelatedField(read_only=True, slug_field='email')

    class Meta:
        model = Calendar
        fields = (
            'id',
            'name',
            'description',
            'owner',
        )
        extra_kwargs = {
            'name':
                {'required': True, 'error_messages':
                    {'required': 'Не задано название календаря',
                     'null': 'Название не может быть null',
                     }
                 },
        }

    @transaction.atomic
    def create(self, validated_data):
        """
        При POST запросе на создание экземпляра модели Calendar
        поле owner автоматически заполняется текущим аутентифицированным
        пользователем.
        """

        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['owner'] = request.user
            return super().create(validated_data)
        raise serializers.ValidationError(
            'Пользователь не аутентифицирован.')



class ShortCalendarSerializer(serializers.ModelSerializer):
    """
    Сериализатор с укороченным представлением. Необходим для передачи в
    эвенте только необходимых данных, вложенным сериализатором.
    """

    class Meta:
        model = Calendar
        fields = (
            'id',
            'name'
        )


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор объекта Category
    """

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'color',
        )


class ReadEventSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    calendar = ShortCalendarSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'datetime_start',
            'datetime_finish',
            'all_day',
            'name',
            'description',
            'day_off',
            'holiday',
            'category',
            'calendar',
        )


class WriteEventSerializer(serializers.ModelSerializer):
    """
    Сериализатор для записи данных.
    В extra_kwargs изменены стандартные ошибки DRF на кастомные.
    """

    class Meta:
        model = Event
        fields = (
            'id',
            'datetime_start',
            'datetime_finish',
            'all_day',
            'name',
            'description',
            'day_off',
            'holiday',
            'category',
            'calendar',
        )
        extra_kwargs = {
            'datetime_start':
                {'required': True, 'error_messages':
                    {'required': 'Дата начала мероприятия отсутствует',
                     'invalid': 'Неправильный формат даты и времени',
                     'null': 'Дата начала мероприятия не может быть null',
                     }
                 },
            'category':
                {'required': True, 'error_messages':
                    {'required': 'Не выбрана категория',
                     'invalid': 'Укажите id категории',
                     'null': 'Категория не может быть null',
                     }
                 },
            'calendar':
                {'required': True, 'error_messages':
                    {'required': 'Не выбран календарь',
                     'invalid': 'Укажите id календаря',
                     'null': 'Календарь не может быть null',
                     }
                 },
        }

    def to_representation(self, instance):
        """
        Метод переопределяет сериализатор для отображения после
        успешного запроса на изменение данных
        """

        return ReadEventSerializer(
            instance=instance, context=self.context).data
