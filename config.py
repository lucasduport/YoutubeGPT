def getConfig(name):
    creds = dict()
    creds['open_ai_key'] = "sk-xxxx"
    creds['model'] = "text-davinci-003"
    creds['languages'] = ['en','af', 'ak', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bn', 'eu', 'be', 'bho', 'bs', 'bg', 'my', 'ca', 'ceb', 
'zh-Hans', 'zh-Hant', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 'en', 'eo', 'et', 'ee', 'fil', 'fi', 'fr', 'gl', 'lg', 'ka', 'de', 'el', 
'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km', 'rw', 'ko', 
'kri', 'ku', 'ky', 'lo', 'la', 'lv', 'ln', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'nso', 'no', 'ny', 
'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'sr', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'st', 'es', 
'su', 'sw', 'sv', 'tg', 'ta', 'th', 'ti', 'ts', 'tr', 'tk', 'uk', 'und', 'ur', 'ug', 'uz', 'vi', 'cy', 'fy', 'xh', 'yi', 'yo', 'zu']
    return creds[name]