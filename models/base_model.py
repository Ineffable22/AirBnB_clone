#!/usr/bin/python3
""" Class base for AirBnB clone - the console.

    Classes:
        BaseModel
"""
import uuid
import models
from datetime import datetime

date_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ BaseModel Class definition.

        ...

        Attributes
        ----------
        id : str
            Unique identication of the instance
        created_at : datetime
            Object creation date and time
        updated_at : datetime
            Object modification date and time

        Methods
        -------
        save():
            Stores the modifcation date and time of the object
        to_dict():
            Returns a dictionary containing all key/values of the instance
        __str__():
            Returns information(type, id, __dict__) of the instance
    """
    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize attribute of an instance.
            If argument kwargs is not empty, the key/values are added to
            the instance. Otherwise, create new instance.

            Parameters
            ----------
            args : list, optional
                pass
            kwargs: dict, optional
                Contains key/values to add to the instance
        """
        self.id = str(uuid.uuid4())
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"] and type(value) is str:
                    value = datetime.strptime(value, date_format)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """ Stores the modifcation date and time of the object.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all key/values of the instance.

            Returns
            -------
            rpr : str
                Dictionary that contains key/values of the instance
        """
        rpr = self.__dict__.copy()
        if "created_at" in list(rpr.keys()):
            rpr['created_at'] = rpr['created_at'].strftime(date_format)
        if "updated_at" in list(rpr.keys()):
            rpr['updated_at'] = rpr['updated_at'].strftime(date_format)
        rpr['__class__'] = self.__class__.__name__
        return rpr

    def __str__(self):
        """ Returns information(type, id, __dict__) of the instance.

            Returns
            -------
            data : str
                Information of the instance in string format
        """
        data = "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        return data
