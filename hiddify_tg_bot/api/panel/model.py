import json
from abc import ABC, abstractstaticmethod


class __APIModelABC(ABC):
    @abstractstaticmethod
    def from_dict(d):
        pass


class Info(__APIModelABC):

    def __init__(self, admin_message_html, admin_message_url, profile_remaining_days, profile_reset_days,
                 profile_title, profile_url, profile_usage_current, profile_usage_total, telegram_bot_url,
                 brand_title, brand_icon_url, doh, def_lang) -> None:

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
        self.def_lang = def_lang

    @staticmethod
    def from_dict(d):
        return Info(
            d['admin_message_html'], d['admin_message_url'], d['profile_remaining_days'], d['profile_reset_days'],
            d['profile_title'], d['profile_url'], d['profile_usage_current'], d['profile_usage_total'],
            d['telegram_bot_url'], d['brand_title'], d['brand_icon_url'], d['doh'], d['def_lang']
        )


class Mtproto(__APIModelABC):
    def __init__(self, title, server_link) -> None:
        self.title = title
        self.link = server_link

    @staticmethod
    def from_dict(d):
        return Mtproto(
            d['title'], d['link']
        )


class Config(__APIModelABC):
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
        return Config(
            d['name'], d['domain'], d['link'], d['protocol'], d['security'], d['transport'], d['type']
        )
