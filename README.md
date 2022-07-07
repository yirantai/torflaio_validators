## torflaio_validators
```
Background: when using Python web frameworks, such as tornado, flask, aiohttp and so on, 
different people have different verification methods for interface input parameters, 
which makes the project very messy
In the past, when using the Django framework, the parameters of the serializers class in the Django rest 
framework were verified, it was very formal and had a very good experience
Therefore, it is developed with reference to the serializers parameter verification style of Django rest framework
It is used to unify the parameter verification methods of tornado, flask, aiohttp and other frameworks
```

### usage：
  pip install torflaio_validators

### usage example:
```
from torflaio_validators.base.base_validator import BaseValidator
from torflaio_validators.base.fields import IntegerField, CharField, BoolField, DictField

1.First define the parameters to be verified, and each field contains a field_ name field_ value, required,
 default, max_ length, min_ Length and other parameters,
You can choose according to whether the verified field is required, default value, etc

class PersonInfoValidator(BaseValidator):
    name = CharField()
    age = IntegerField()
    address = CharField()
    province = CharField()
    city = CharField()
    county = CharField()
    is_valid = BoolField(required=False, default=True)
    extra = DictField()
    
2.Introduce the validator class in view to verify whether the passed in parameters are legal
validator = PersonInfoValidator(data)
validator.validation()
validated_data = validator.validated_data   # the validated_data is valid.

3. If you want to verify not only the basic information of the field (whether it is required,
 default value, maximum length, minimum length, etc.), but also the business-related,
You can redefine the validated of the validated_data(property). Use the following:

from torflaio_validators.base.exceptions import ParamsValidationError
from torflaio_validators.base.fields import CharField, IntegerField, BoolField, DictField

class PersonInfoValidator(BaseValidator):
    name = CharField()
    age = IntegerField()
    address = CharField()
    province = CharField()
    city = CharField()
    county = CharField()
    is_valid = BoolField(required=False, default=True)
    extra = DictField()
    
    @propery
    def validated_data(self):
        validated_data = super().validated_data
        age = validated_data.get('age')
        if age < 18:
            raise ParamsValidationError(err_code=400, err_msg="the age should not under 18.")    
            # the ParamsValidationError class is the default Error class, you can customize the error class
        return validated_data
```

#### contact：
```
email: 896275756@qq.com
Due to the limited level, it is inevitable to have unknown bugs and thoughtless places. 
If you have good comments or suggestions, please email me to discuss and improve together 
Your comments or suggestions will be reflected in the next version update.
```
