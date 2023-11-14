from typing import List
import requests
import json
from abc import ABC,abstractmethod,abstractproperty

import config
from api.panel import model
class __API(ABC):
    
    @property
    @abstractmethod
    def __session():
        return requests.session()

    @abstractmethod
    def hiddify_url(self):
        pass
    @abstractmethod
    def me(self):
        pass
    

class PanelAdminAPI(__API):
    def __init__(self,admin_uuid) -> None:
        self.uuid = admin_uuid

    def hiddify_url(self):
        return f'{self.root_domain}/{self.proxy_path}/{self.uuid}/'
    
    def me(self) -> model.Admin_Me:
        api_url = self.hiddify_url() + 'me/'
        res = PanelUserAPI.__session.get(api_url).content.decode()
        me = json.loads(res,object_hook= model.Admin_Me.from_dict)
        return me
    
class PanelUserAPI(__API):
    def __init__(self,uuid) -> None:
        self.root_domain = config.HIDDIFY_ROOT_DOMAIN.removesuffix('/')
        self.proxy_path = config.HIDDIFY_PROXY_PATH.removesuffix('/')
        self.uuid  = uuid
        # skip ssl verification (remove the line on production)
        PanelUserAPI.__session.verify = False
        
    def hiddify_url(self):
        return f'{self.root_domain}/{self.proxy_path}/{self.uuid}/'
    
    def me(self) -> model.User_Me:
        api_url = self.hiddify_url() + 'me/'
        res = PanelUserAPI.__session.get(api_url).content.decode()
        info = json.loads(res,object_hook = model.User_Me.from_dict)
        return info

    def short(self) -> str:
        api_url = self.hiddify_url() + 'short/'
        res = PanelUserAPI.__session.get(api_url).content.decode()
        return json.loads(res)['short']
    
    def mtproxies(self) -> List[model.User_Mtproto]:
        api_url = self.hiddify_url() + 'mtproxies/'
        res = PanelUserAPI.__session.get(api_url).content.decode()
        mtprotos_json = json.loads(res)
        mtprotos = []
        for item in mtprotos_json:
            mtproto = json.loads(json.dumps(item), object_hook=model.User_Mtproto.from_dict)
            mtprotos.append(mtproto)

        return mtprotos


    def all_configs(self) -> List[model.User_Config]:
        api_url = self.hiddify_url() + 'all-configs/'
        res = PanelUserAPI.__session.get(api_url).content.decode()
        configs_json = json.loads(res)
        configs = []
        for item in configs_json:
            conf = json.loads(json.dumps(item), object_hook=model.User_Config.from_dict)
            configs.append(conf)

        return configs