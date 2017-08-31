#!/usr/bin/env python
# encoding=utf8
"""
This module parses and loads the data of an Instagram user given by https://www.instagram.com/<user>/?__a=1 in the igmodel class model.
"""
__author__     = "Valentyna Melnyk"
__build__      = "Valentyna Melnyk"
__copyright__  = "All reserved by me."
__license__    = "GPL"
__title__      = "Parsing & Load Data from Instagram"
__version__    = "1.0.0"
__maintainer__ = "Valentyna Melnyk"
__email__      = "valentyna.melnyk.s@gmail.com"
__status__     = "Production"
__credits__    = "Valentyna Melnyk"

import json
from igmodel import *


def make_ig_user(json_file):
    """
    This function returns an Instagram User object from the data in the json file.
    """
    with open(json_file, "r") as fjson:

        # Parse the data in the json file.
        account = json.loads(fjson.read())
        biography                = account["user"]["biography"]
        blocked_by_viewer        = account["user"]["blocked_by_viewer"]
        country_block            = account["user"]["country_block"]
        external_url             = account["user"]["external_url"]
        external_url_linkshimmed = account["user"]["external_url_linkshimmed"]
        followed_by              = account["user"]["followed_by"]
        followed_by_viewer       = account["user"]["followed_by_viewer"]
        follows                  = account["user"]["follows"]
        follows_viewer           = account["user"]["follows_viewer"]
        full_name                = account["user"]["full_name"]
        has_blocked_viewer       = account["user"]["has_blocked_viewer"]
        has_requested_viewer     = account["user"]["has_requested_viewer"]
        id_                      = account["user"]["id"]
        is_private               = account["user"]["is_private"]
        is_verified              = account["user"]["is_verified"]
        profile_pic_url          = account["user"]["profile_pic_url"]
        profile_pic_url_hd       = account["user"]["profile_pic_url_hd"]
        requested_by_viewer      = account["user"]["requested_by_viewer"]
        username                 = account["user"]["username"]
        connected_fb_page        = account["user"]["connected_fb_page"]

        # Creates the attributes of the Instagram User object.
        attr_biography                = Attribute(name = "biography", value = biography)
        attr_blocked_by_viewer        = Attribute(name = "blocked_by_viewer", value = blocked_by_viewer)
        attr_country_block            = Attribute(name = "country_block", value = country_block)
        attr_external_url             = Attribute(name = "external_url", value = external_url)
        attr_external_url_linkshimmed = Attribute(name = "external_url_linkshimmed", value = external_url_linkshimmed)
        attr_followed_by              = Attribute(name = "followed_by", value = followed_by)
        attr_followed_by_viewer       = Attribute(name = "followed_by_viewer", value = followed_by_viewer)
        attr_follows                  = Attribute(name = "follows", value = follows)
        attr_follows_viewer           = Attribute(name = "follows_viewer", value = follows_viewer)
        attr_full_name                = Attribute(name = "full_name", value = full_name)
        attr_has_blocked_viewer       = Attribute(name = "has_blocked_viewer", value = has_blocked_viewer)
        attr_has_requested_viewer     = Attribute(name = "has_requested_viewer", value = has_requested_viewer)
        attr_id                       = Attribute(name = "id", value = id_)
        attr_is_private               = Attribute(name = "is_private", value = is_private)
        attr_is_verified              = Attribute(name = "is_verified", value = is_verified)
        attr_profile_pic_url          = Attribute(name = "profile_pic_url", value = profile_pic_url)
        attr_profile_pic_url_hd       = Attribute(name = "profile_pic_url_hd", value = profile_pic_url_hd)
        attr_requested_by_viewer      = Attribute(name = "requested_by_viewer", value = requested_by_viewer)
        attr_username                 = Attribute(name = "username", value = username)
        attr_connected_fb_page        = Attribute(name = "connected_fb_page", value = connected_fb_page)

        # Creates the Instagram User object.
        ig_user = User()
        ig_user.set_attr(   attr_biography,
                            attr_blocked_by_viewer,
                            attr_country_block,
                            attr_external_url,
                            attr_external_url_linkshimmed,
                            attr_followed_by,
                            attr_followed_by_viewer,
                            attr_follows,
                            attr_follows_viewer,
                            attr_full_name,
                            attr_has_blocked_viewer,
                            attr_has_requested_viewer,
                            attr_id,
                            attr_is_private,
                            attr_is_verified,
                            attr_profile_pic_url,
                            attr_profile_pic_url_hd,
                            attr_requested_by_viewer,
                            attr_username,
                            attr_connected_fb_page
                        )

        # Parse and create the Instagram User nodes.
        for node in account["user"]["media"]["nodes"]:
            attr___typename          = Attribute(name = "__typename", value = node["__typename"])
            attr_id                  = Attribute(name = "id", value = node["id"])
            attr_comments_disabled   = Attribute(name = "comments_disabled", value = node["comments_disabled"])
            attr_dimensions_height   = Attribute(name = "dimensions_height", value = node["dimensions"]["height"])
            attr_dimensions_width    = Attribute(name = "dimensions_width", value = node["dimensions"]["width"])
            attr_gating_info         = Attribute(name = "gating_info", value = node["gating_info"])
            attr_media_preview       = Attribute(name = "media_preview", value = node["media_preview"])
            attr_owner_id            = Attribute(name = "owner_id", value = node["owner"]["id"])
            attr_thumbnail_src       = Attribute(name = "thumbnail_src", value = node["thumbnail_src"])
            attr_thumbnail_resources = Attribute(name = "thumbnail_resources", value = node["thumbnail_resources"])
            attr_is_video            = Attribute(name = "is_video", value = node["is_video"])
            attr_code                = Attribute(name = "code", value = node["code"])
            attr_date                = Attribute(name = "date", value = node["date"])
            attr_display_src         = Attribute(name = "display_src", value = node["display_src"])
            attr_caption             = Attribute(name = "caption", value = node["caption"])
            attr_comments_count      = Attribute(name = "comments_count", value = node["comments"]["count"])
            attr_likes_count         = Attribute(name = "likes_count", value = node["likes"]["count"])

            ig_node = Node()
            ig_node.set_attr(   attr___typename,
                                attr_id,
                                attr_comments_disabled,
                                attr_dimensions_height,
                                attr_dimensions_width,
                                attr_gating_info,
                                attr_media_preview,
                                attr_owner_id,
                                attr_thumbnail_src,
                                attr_thumbnail_resources,
                                attr_is_video,
                                attr_code,
                                attr_date,
                                attr_display_src,
                                attr_caption,
                                attr_comments_count,
                                attr_likes_count
                            )

            # Add the nodes to the User.
            ig_user.add_nodes(ig_node)

        return ig_user


if __name__ == '__main__':

    # TEST LOAD IG DATA.
    victoriassecret = make_ig_user('victoriasecret.json')
    print victoriassecret.get_attr("full_name")
    print victoriassecret
    print "Nodes:", victoriassecret.get_all_nodes()
    # enriqueiglesias = make_ig_user('enriqueiglesias.json')
    # print enriqueiglesias
    # nodes = enriqueiglesias.get_all_nodes()
    # for node in nodes:
    #     print node.get_attr("code"), node.get_attr("caption")