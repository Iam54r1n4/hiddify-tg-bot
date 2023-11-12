from typing import List
import requests
import json

import config
from api.panel import model

class PanelAPI:
    __session = requests.session()
    def __init__(self,user_uuid:str) -> None:
        self.root_domain = config.HIDDIFY_ROOT_DOMAIN.removesuffix('/')
        self.proxy_path = config.HIDDIFY_PROXY_PATH.removesuffix('/')
        self.user_uuid  = user_uuid.removesuffix('/')
        self.hiddify_url = f'{self.root_domain}/{self.proxy_path}/{self.user_uuid}/'

        # skip ssl verification (remove the line on production)
        PanelAPI.__session.verify = False

    def info(self) -> model.Info:
        api_url = self.hiddify_url + 'info'
        res = PanelAPI.__session.get(api_url).content.decode('utf-8')
        info = json.loads(res,object_hook = model.Info.from_dict)
        return info

    def short(self) -> str:
        api_url = self.hiddify_url + 'short'
        res = PanelAPI.__session.get(api_url).content.decode('utf-8')
        return json.loads(res)['short']
    
    def mtproxies(self) -> List[model.Mtproto]:
        api_url = self.hiddify_url + 'mtproxies'
        res = PanelAPI.__session.get(api_url).content.decode('utf-8')
        mtprotos_json = json.loads(res)
        mtprotos = []
        for item in mtprotos_json:
            mtproto = json.loads(json.dumps(item), object_hook=model.Mtproto.from_dict)
            mtprotos.append(mtproto)

        return mtprotos


    def all_configs(self) -> List[model.Config]:
        api_url = self.hiddify_url + 'all-configs'
        res = PanelAPI.__session.get(api_url).content.decode('utf-8')
        configs_json = json.loads(res)
        configs = []
        for item in configs_json:
            conf = json.loads(json.dumps(item), object_hook=model.Config.from_dict)
            configs.append(conf)

        return configs