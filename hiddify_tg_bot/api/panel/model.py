import json
from abc import ABC, abstractstaticmethod

class __APIModelABC(ABC):
    @abstractstaticmethod
    def from_dict(d):
        pass


class User_Me(__APIModelABC):

    def __init__(self, admin_message_html, admin_message_url, profile_remaining_days, profile_reset_days,
                 profile_title, profile_url, profile_usage_current, profile_usage_total, telegram_bot_url,
                 brand_title, brand_icon_url, doh, lang) -> None:

        self.admin_message_html = admin_message_html
        self.admin_message_url = admin_message_url
        self.profile_remaining_days = profile_remaining_days
        self.profile_reset_days = profile_reset_days
        self.profile_title = profile_title
        self.profile_url = profile_url
        self.profile_usage_current = profile_usage_current
        self.profile_usage_total = profile_usage_total
        self.telegram_bot_url = telegram_bot_url
        self.brand_icon_url = brand_icon_url
        self.brand_title = brand_title
        self.doh = doh
        self.lang = lang

    @staticmethod
    def from_dict(d):
        return User_Me(
            d['admin_message_html'], d['admin_message_url'], d['profile_remaining_days'], d['profile_reset_days'],
            d['profile_title'], d['profile_url'], d['profile_usage_current'], d['profile_usage_total'],
            d['telegram_bot_url'], d['brand_title'], d['brand_icon_url'], d['doh'], d['def_lang']
        )


class User_Mtproto(__APIModelABC):
    def __init__(self, title, server_link) -> None:
        self.title = title
        self.link = server_link

    @staticmethod
    def from_dict(d):
        return User_Mtproto(
            d['title'], d['link']
        )


class User_Config(__APIModelABC):
    def __init__(self, name, domain, link, protocol, security, transport, type) -> None:
        self.name = name
        self.domain = domain
        self.link = link
        self.protocol = protocol
        self.security = security
        self.transport = transport
        self.type = type

    @staticmethod
    def from_dict(d):
        return User_Config(
            d['name'], d['domain'], d['link'], d['protocol'], d['security'], d['transport'], d['type']
        )

class Admin_Me(__APIModelABC):
    def __init__(self,name,mode,comment,uuid,telegram_id,can_add_admin,parent_admin_uuid,lang) -> None:
        self.name = name
        self.mode = mode
        self.comment = comment
        self.uuid = uuid
        self.telegram_id = telegram_id
        self.can_add_admin = can_add_admin
        self.parent_admin_uuid = parent_admin_uuid
        self.lang = lang

    @staticmethod
    def from_dict(d):
        return Admin_Me(
            d['name'],d['mode'],d['comment'],d['uuid'],d['telegram_id'],d['can_add_admin'],d['parent_admin_uuid'],d['lang']
        )
    

