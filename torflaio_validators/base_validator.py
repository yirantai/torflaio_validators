# coding: utf-8


class BaseValidator(object):
    """
    Usage:

    class TestValidator(BaseValidator):
        field_name_1 = IntegerField()
        field_name_2 = CharField()
        field_name_3 = ListField()

    validator = TestValidator(data)
    validator.validation()
    validated_data = validator.validated_data

    if you want to custom TestValidator,
    Recover validation function to custom TestValidator validate or Extended validation

    this class does not allow extend any attributes or functions
    """

    def __init__(self, data):
        self.__data = data

    def __field_names(self):
        field_names = [item for item in dir(self) if
                       not callable(self)
                       and '__' not in item
                       and not 'validation' == item
                       and not 'validated_data' == item
                       ]
        return field_names

    def validation(self):
        field_names = self.__field_names()
        for field_name in field_names:
            instance = getattr(self, field_name)

            field_value = self.__data.get(field_name, None)
            instance.field_value = field_value
            instance.field_name = field_name
            instance.validate()
        return

    @property
    def validated_data(self):
        validated_data = {}
        for field_name in self.__field_names():
            instance = getattr(self, field_name)
            validated_data.update({field_name: instance.field_type(instance.field_value)})
        return validated_data
