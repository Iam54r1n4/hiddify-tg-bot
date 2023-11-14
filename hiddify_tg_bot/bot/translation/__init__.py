import i18n
import config
from bot import bot,redis_storage
from storage import HiddifyStateRedisStorage,BotUserData

if config.TRASLATION_FOLDER not in i18n.load_path:
    i18n.load_path.append(config.TRASLATION_FOLDER)

i18n.set('file_format', 'json')
i18n.set('filename_format', '{locale}.{format}')
i18n.set('skip_locale_root_data', True)

def translator(lang,key:str,translation_values:dict=None) -> str:
    i18n.set('locale',lang)
    return i18n.t(key,translation_values) if translation_values else i18n.t(key)