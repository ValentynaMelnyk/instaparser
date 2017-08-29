#!/usr/bin/env python
# encoding=utf8
"""
This module implements a generic class model that allows to categorize Elements, their Attributes and Links to other Elements.
"""
__author__     = "Valentyna Melnyk"
__build__      = "Valentyna Melnyk"
__copyright__  = "All reserved by me."
__license__    = "GPL"
__title__      = "Generic Class Model"
__version__    = "1.0.0"
__maintainer__ = "Valentyna Melnyk"
__email__      = "valentyna.melnyk.s@gmail.com"
__status__     = "Production"
__credits__    = "Valentyna Melnyk"

import inspect


class Element(object):
    """
    Implements the Element class.
    """
    def __init__(self, *attributes):
        self.attributes = dict()
        self.links      = list()
        for attribute in attributes:
            self.attributes[attribute.name] = attribute.value

    def set_attr(self, *attributes):
        for attribute in attributes:
            self.attributes[attribute.name] = attribute.value

    def get_attr(self, attribute):
        if self.attributes.has_key(attribute.name):
            return self.attributes[attribute.name]
        else:
            print attribute.name
            raise IndexError

    def get_all_attr(self):
        return self.attributes

    def set_link(self, *links):
        self.links.extend(links)

    def get_links(self):
        return self.links


class Attribute(object):
    """
    Implements the class Attribute to be used by each class Element.
    """
    def __init__(self, name, value = None):
        self.name  = name
        self.value = value

    def set(self, name, value):
        self.__init__(name, value)

    def get(self):
        return self.name, self.value

    def __repr__(self):
        value = self.value if self.value else "None"
        return self.name + ' : ' + value


class Link(object):
    """
    Implements the Links class that allows to link the Elements.
    """
    def __init__(self, element):
        self.element = element

    def set(self, element):
        self.__init__(element)

    def get(self):
        return self.element

    @staticmethod
    def __get_name(self):
        parent_frame = inspect.currentframe().f_back
        matches = {k: v for k,v in parent_frame.f_globals.items() if v is self}
        return matches.keys()[0] if matches else None

    def __repr__(self):
        return self.__class__.__get_name(self.element)



if __name__ == '__main__':

    # TEST GENERIC CLASS MODEL.

    # Father's data.
    father_name = Attribute(name = "name", value = "Peter")
    father_age  = Attribute(name = "age", value = 35)
    father      = Element(father_name, father_age)

    # Mother's data.
    mother_name = Attribute(name = "name", value = "Marie")
    mother_age  = Attribute(name = "age", value = 30)
    mother      = Element(mother_name, mother_age)

    # Data of the son Jhon.
    son_name = Attribute(name = "name", value = "Jhon")
    son_age  = Attribute(name = "age", value = 8)
    son      = Element(son_name, son_age)

    # Data of the daughter Karen.
    daughter_name = Attribute(name = "name", value = "Karen")
    daughter_age  = Attribute(name = "age", value = 12)
    daughter      = Element(daughter_name, daughter_age)

    # Links.
    to_father   = Link(father)
    to_mother   = Link(mother)
    to_son      = Link(son)
    to_daughter = Link(daughter)
    to_wife     = to_mother
    to_husband  = to_father
    to_brother  = to_son
    to_sister   = to_daughter
    
    father.set_link(to_wife, to_son, to_daughter)
    mother.set_link(to_husband, to_son, to_daughter)
    son.set_link(to_father, to_mother, to_sister)
    daughter.set_link(to_father, to_mother, to_brother)


    print "* Father data:"
    print father.get_all_attr()
    print "Links to:"
    print father.get_links(), "\n"

    print "* Mother data:"
    print mother.get_all_attr()
    print "Links to:"
    print mother.get_links(), "\n"

    print "* Son data:"
    print son.get_all_attr()
    print "Links to:"
    print son.get_links(), "\n"

    print "* Daughter data:"
    print daughter.get_all_attr()
    print "Links to:"
    print daughter.get_links(), "\n"