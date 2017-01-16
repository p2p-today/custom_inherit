import six
import inspect

from custom_inherit import DocInheritMeta
from abc import ABCMeta, abstractmethod, abstractproperty
from types import MethodType, FunctionType

try:
    from inspect import signature
except ImportError:
    from inspect import getargspec as signature


def style(x, y): return "valid"


""" With ABC"""


@six.add_metaclass(DocInheritMeta(style=style, abstract_base_class=True))
class Parent(object):
    def method(self, x, y=None):
        """"""
        pass

    @classmethod
    def clsmthd(cls):
        """"""
        pass

    @staticmethod
    def static():
        """"""
        pass

    @property
    def prop(self):
        """"""
        return None

    @abstractmethod
    def absmthd(self):
        """"""
        pass

    @abstractproperty
    def absproperty(self):
        """"""
        return None


class Kid(Parent):

    def kid_method(self):
        """kid"""
        pass

    def method(self, x, y=None): pass

    @classmethod
    def clsmthd(cls): pass

    @staticmethod
    def static(): pass

    @property
    def prop(self): return None

    def absmthd(self): pass

    @property
    def absproperty(self): return None


def test_abc():
    assert isinstance(Parent, ABCMeta)
    assert isinstance(Kid, ABCMeta)


def test_sideeffect():
    assert inspect.getdoc(Kid.kid_method) == "kid"
    assert signature(Kid.method) == signature(Parent.method)


def test_method():
    assert isinstance(Kid().method, MethodType)
    assert inspect.getdoc(Kid.method) == "valid"


def test_classmethod():
    assert inspect.ismethod(Kid.clsmthd) and Kid.clsmthd.__self__ is Kid
    assert inspect.getdoc(Kid.clsmthd) == "valid"


def test_staticmethod():
    assert isinstance(Kid().static, FunctionType)
    assert inspect.getdoc(Kid.static) == "valid"


def test_property():
    assert isinstance(Kid.prop, property)
    assert inspect.getdoc(Kid.prop) == "valid"


def test_abstract_method():
    assert 'absmthd' in Parent.__abstractmethods__
    assert inspect.getdoc(Kid.absmthd) == "valid"


def test_abstract_property():
    assert 'absproperty' in Parent.__abstractmethods__
    assert inspect.getdoc(Kid.absproperty) == "valid"


""" Without ABC"""


@six.add_metaclass(DocInheritMeta(style=style))
class Parent2(object):
    def method(self, x, y=None):
        """"""
        pass

    @classmethod
    def clsmthd(cls):
        """"""
        pass

    @staticmethod
    def static():
        """"""
        pass

    @property
    def prop(self):
        """"""
        return None


class Kid2(Parent2):

    def kid_method(self):
        """kid"""
        pass

    def method(self, x, y=None): pass

    @classmethod
    def clsmthd(cls): pass

    @staticmethod
    def static(): pass

    @property
    def prop(self): return None
    
    
def test_sideeffect2():
    assert inspect.getdoc(Kid2.kid_method) == "kid"
    assert signature(Kid2.method) == signature(Parent.method)


def test_method2():
    assert isinstance(Kid2().method, MethodType)
    assert inspect.getdoc(Kid2.method) == "valid"


def test_classmethod2():
    assert inspect.ismethod(Kid2.clsmthd) and Kid2.clsmthd.__self__ is Kid2
    assert inspect.getdoc(Kid2.clsmthd) == "valid"


def test_staticmethod2():
    assert isinstance(Kid2.static, FunctionType)
    assert inspect.getdoc(Kid2.static) == "valid"


def test_property2():
    assert isinstance(Kid2.prop, property)
    assert inspect.getdoc(Kid2.prop) == "valid"
