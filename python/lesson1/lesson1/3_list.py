# -*- coding: utf-8 -*-
# =================================
#             РЎРїРёСЃРєРё
# =================================

a = [1, 3, 5, 3.45, 'ddd', 's', 333]
print(a)

# РЎРѕ СЃРїРёСЃРєР°РјРё РјРѕР¶РЅРѕ СЂР°Р±РѕС‚Р°С‚СЊ С‚Р°РєР¶Рµ, РєР°Рє Рё СЃРѕ СЃС‚СЂРѕРєР°РјРё:
print(a[0]) # РїРѕР»СѓС‡РёРј РїРµСЂРІС‹Р№ СЌР»РµРјРµРЅС‚ СЃРїРёСЃРєР°
print(a[-1]) # РїРѕСЃР»РµРґРЅРёР№ СЌР»РµРјРµРЅС‚ СЃРїРёСЃРєР°
print(a[0:-3]) # 3 РїРѕСЃР»РµРґРЅРёС… СЌР»РµРјРµРЅС‚Р° СЃРїРёСЃРєР°
print(a[0:3] + [7,8,9]) # РїРѕР»СѓС‡РёРј РЅРѕРІС‹Р№ СЃРїРёСЃРѕРє РёР· 6 СЌР»РµРјРµРЅС‚РѕРІ
print([3,'4']*3 + ['The end!']) # СЂР°Р·РјРЅРѕР¶РёРј СЃРїРёСЃРѕРє

# Р’ РѕС‚Р»РёС‡РёРµ РѕС‚ СЃС‚СЂРѕРє, СЌР»РµРјРµРЅС‚С‹ СЃРїРёСЃРєР° РјРѕР¶РЅРѕ РёР·РјРµРЅСЏС‚СЊ:
a[2] = a[2] + 4
print(a)

# Рђ С‚Р°РєР¶Рµ Р·Р°РјРµРЅСЏС‚СЊ С‡Р°СЃС‚СЊ СЌР»РµРјРµРЅС‚РѕРІ СЃ РїРѕРјРѕС‰СЊСЋ СЃСЂРµР·РѕРІ. Р—Р°РјРµРЅРёРј РїРµСЂРІС‹Рµ 3:
a[0:3] = [2,4,6]
print(a)

# СѓРґР°Р»РёРј РїРѕСЃР»РµРґРЅРёРµ 2
a[-2:] = []
print(a)

# РІСЃС‚Р°РІРёРј РЅРµСЃРѕР»СЊРєРѕ СЌР»РµРјРµРЅС‚РѕРІ РІРЅСѓС‚СЂСЊ
a[3:3] = ['this', 'is', 'some', 'elements']
print(a)

# РІСЃС‚Р°РІРёРј СЌР»РµРјРµРЅС‚ РІ РЅР°С‡Р°Р»Рѕ СЃРїРёСЃРєР°
a[:0] = [-1]
print(a)

# РљР°Рє Рё РґР»СЏ СЃС‚СЂРѕРє, РІСЃС‚СЂРѕРµРЅРЅР°СЏ С„СѓРЅРєС†РёСЏ len() РІРµСЂРЅРµС‚ РґР»РёРЅСѓ СЃРїРёСЃРєР°:
print(len(a))

# Р”РѕР±Р°РІРёС‚СЊ С‡С‚Рѕ-С‚Рѕ РІ РєРѕРЅРµС† СЃРїРёСЃРєР° РјРѕР¶РЅРѕ С‚Р°Рє:
a[len(a):] = [100]
print(a)

# РќРѕ С‡Р°С‰Рµ РІСЃРµ-С‚Р°РєРё РёСЃРїРѕР»СЊР·СѓРµС‚СЃСЏ С‚Р°РєР°СЏ Р±РѕР»РµРµ РїСЂРѕСЃС‚Р°СЏ РєРѕРЅСЃС‚СЂСѓРєС†РёСЏ (РїСЂРѕСЃС‚РѕРµ Р»СѓС‡С€Рµ СЃР»РѕР¶РЅРѕРіРѕ, РїРѕРјРЅРёС‚Рµ?):
a.append(200)
print(a)

# РњРѕР¶РЅРѕ СЃРѕР·РґР°РІР°С‚СЊ СЃРїРёСЃРєРё, СЃРѕРґРµСЂР¶Р°С‰РёРµ РґСЂСѓРіРёРµ СЃРїРёСЃРєРё:
b = [1, 2, 3, [11, 22, 33], 5, 6]
print(b[3][2])

a = '2' in b
print(a)
