#!/usr/bin/env python
# encoding=utf8
"""
This module implements the data model of the Instagram platform using the generic class model. Specifically, it implements the User and Node classes.
"""
__author__     = "Valentyna Melnyk"
__build__      = "Valentyna Melnyk"
__copyright__  = "All reserved by me."
__license__    = "GPL"
__title__      = "Instagram Class Model"
__version__    = "1.0.0"
__maintainer__ = "Valentyna Melnyk"
__email__      = "valentyna.melnyk.s@gmail.com"
__status__     = "Production"
__credits__    = "Valentyna Melnyk"

from classmodel import *


class User(Element):
    """
    Implements the Instagram User data model.
    """
    def __init__(self):
        super(User, self).__init__(
                                Attribute(name = "biography"),
                                Attribute(name = "blocked_by_viewer"),
                                Attribute(name = "country_block"),
                                Attribute(name = "external_url"),
                                Attribute(name = "external_url_linkshimmed"),
                                Attribute(name = "followed_by"),
                                Attribute(name = "followed_by_viewer"),
                                Attribute(name = "follows"),
                                Attribute(name = "follows_viewer"),
                                Attribute(name = "full_name"),
                                Attribute(name = "has_blocked_viewer"),
                                Attribute(name = "has_requested_viewer"),
                                Attribute(name = "id"),
                                Attribute(name = "is_private"),
                                Attribute(name = "is_verified"),
                                Attribute(name = "profile_pic_url"),
                                Attribute(name = "profile_pic_url_hd"),
                                Attribute(name = "requested_by_viewer"),
                                Attribute(name = "username"),
                                Attribute(name = "connected_fb_page")
                            )


    def get_attr(self, attr_name):
        attr = Attribute(name = attr_name)
        return super(User, self).get_attr(attr)

    def add_nodes(self, *nodes):
        for node in nodes:
            link = Link(node)
            self.set_link(link)


    def get_node(self, node_code):
        attrCode = Attribute(name = "code")
        nodes = self.get_links()
        for node in nodes:
            if node.get_attr(attrCode) == node_code:
                return node
        else:
            return None


    def get_all_nodes(self):
        return [link.element for link in self.get_links()]


    def __repr__(self):
        return self.get_attr("full_name") + ' @' + self.get_attr("username")


class Node(Element):
    """
    Implements the Instagram Node data model.
    """
    def __init__(self):
        super(Node, self).__init__(
                                Attribute(name = "__typename"),
                                Attribute(name = "id"),
                                Attribute(name = "comments_disabled"),
                                Attribute(name = "dimensions_height"),
                                Attribute(name = "dimensions_width"),
                                Attribute(name = "gating_info"),
                                Attribute(name = "media_preview"),
                                Attribute(name = "owner_id"),
                                Attribute(name = "thumbnail_src"),
                                Attribute(name = "thumbnail_resources"),
                                Attribute(name = "is_video"),
                                Attribute(name = "code"),
                                Attribute(name = "date"),
                                Attribute(name = "display_src"),
                                Attribute(name = "caption"),
                                Attribute(name = "comments_count"),
                                Attribute(name = "likes_count")
                            )

    def get_attr(self, attr_name):
        attr = Attribute(name = attr_name)
        return super(Node, self).get_attr(attr)

    def __repr__(self):
        return self.get_attr('code')


if __name__ == '__main__':

    # TEST INSTAGRAM CLASS MODEL.

    # User.
    myuser        = User()
    attrFull_name = Attribute(name = "full_name", value = "Valentyna Melnyk")
    attrUsername  = Attribute(name = "username", value = "valentyna")
    myuser.set_attr(attrFull_name, attrUsername)

    # Node 1.
    node1 = Node()
    attrCode1 = Attribute(name = "code", value = "code1")
    attrDate1 = Attribute(name = "date", value = "date1")
    node1.set_attr(attrCode1, attrDate1)

    # Node 2.
    node2 = Node()
    attrCode2 = Attribute(name = "code", value = "code2")
    attrDate2 = Attribute(name = "date", value = "date2")
    node2.set_attr(attrCode2, attrDate2)
    # print node2

    # Add nodes.
    myuser.add_nodes(node1, node2)
    print myuser, myuser.get_all_nodes()