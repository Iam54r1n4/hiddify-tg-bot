from typing import List
import requests
import json
from abc import ABC,abstractmethod,abstractproperty

import config
from api.panel import model
class __API(ABC):
    
    _session = requests.session()

    @abstractmethod
    def build_api_url(self):
        pass
    @abstractmethod
    def me(self):
        pass
    

class PanelAdminAPI(__API):
    def __init__(self,admin_uuid) -> None:
        self.root_domain = config.HIDDIFY_ROOT_DOMAIN.removesuffix('/')
        self.proxy_path = config.HIDDIFY_PROXY_PATH.removesuffix('/')
        self.uuid = admin_uuid

        # skip ssl verification (remove the line on production)
        PanelUserAPI._session.verify = False

    def build_api_url(self):
        return f'{self.root_domain}/{self.proxy_path}/{self.uuid}/api/v2/admin/'
    
    def me(self) -> model.Admin_Me:
        api_url = self.build_api_url() + 'me/'
        try:
            res = PanelUserAPI._session.get(api_url)
            if res.status_code != 200:
                return None
            me = json.loads(res.content.decode(),object_hook= model.Admin_Me.from_dict)
            return me
        except:
            return None
    
class PanelUserAPI(__API):
    def __init__(self,uuid) -> None:
        self.root_domain = config.HIDDIFY_ROOT_DOMAIN.removesuffix('/')
        self.proxy_path = config.HIDDIFY_PROXY_PATH.removesuffix('/')
        self.uuid  = uuid
        # skip ssl verification (remove the line on production)
        PanelUserAPI._session.verify = False
        
    def build_api_url(self):
        return f'{self.root_domain}/{self.proxy_path}/{self.uuid}/api/v2/user/'
    
    def me(self) -> model.User_Me:
        try:
            api_url = self.build_api_url() + 'me/'
            res = PanelUserAPI._session.get(api_url)
            if res.status_code != 200:
                return None
            info = json.loads(res.content.decode(),object_hook = model.User_Me.from_dict)
            return info
        except:
            return None

    def short(self) -> str:
        try:
            api_url = self.build_api_url() + 'short/'
            res = PanelUserAPI._session.get(api_url)
            if res.status_code != 200:
                return None
            return json.loads(res.content.decode())['short']
        except:
            return None
    
    def mtproxies(self) -> List[model.User_Mtproto]:
        try:
            api_url = self.build_api_url() + 'mtproxies/'
            res = PanelUserAPI._session.get(api_url)
            if res.status_code != 200:
                return None
            mtprotos_json = json.loads(res.content.decode())
            mtprotos = []
            for item in mtprotos_json:
                mtproto = json.loads(json.dumps(item), object_hook=model.User_Mtproto.from_dict)
                mtprotos.append(mtproto)

            return mtprotos

        except:
            return None


    def all_configs(self) -> List[model.User_Config]:
        try:
            api_url = self.build_api_url() + 'all-configs/'
            res = PanelUserAPI._session.get(api_url)
            if res.status_code != 200:
                return None
            configs_json = json.loads(res.content.decode())
            configs = []
            for item in configs_json:
                conf = json.loads(json.dumps(item), object_hook=model.User_Config.from_dict)
                configs.append(conf)

            return configs

        except:
            return None