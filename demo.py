# encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import jieba
import jieba.posseg
import jieba.analyse

print('='*40)
print('1. ·Ö´Ê')
print('-'*40)

seg_list = jieba.cut("ÎÒÀ´µ½±±¾©Çå»ª´óÑ§", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # È«Ä£Ê½

seg_list = jieba.cut("ÎÒÀ´µ½±±¾©Çå»ª´óÑ§", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # Ä¬ÈÏÄ£Ê½

seg_list = jieba.cut("ËûÀ´µ½ÁËÍøÒ×º¼ÑÐ´óÏÃ")
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("Ð¡Ã÷Ë¶Ê¿±ÏÒµÓÚÖÐ¹ú¿ÆÑ§Ôº¼ÆËãËù£¬ºóÔÚÈÕ±¾¾©¶¼´óÑ§ÉîÔì")  # ËÑË÷ÒýÇæÄ£Ê½
print(", ".join(seg_list))

print('='*40)
print('2. Ìí¼Ó×Ô¶¨Òå´Êµä/µ÷Õû´Êµä')
print('-'*40)

print('/'.join(jieba.cut('Èç¹û·Åµ½postÖÐ½«³ö´í¡£', HMM=False)))
#Èç¹û/·Åµ½/post/ÖÐ½«/³ö´í/¡£
print(jieba.suggest_freq(('ÖÐ', '½«'), True))
#494
print('/'.join(jieba.cut('Èç¹û·Åµ½postÖÐ½«³ö´í¡£', HMM=False)))
#Èç¹û/·Åµ½/post/ÖÐ/½«/³ö´í/¡£
print('/'.join(jieba.cut('¡¸Ì¨ÖÐ¡¹ÕýÈ·Ó¦¸Ã²»»á±»ÇÐ¿ª', HMM=False)))
#¡¸/Ì¨/ÖÐ/¡¹/ÕýÈ·/Ó¦¸Ã/²»»á/±»/ÇÐ¿ª
print(jieba.suggest_freq('Ì¨ÖÐ', True))
#69
print('/'.join(jieba.cut('¡¸Ì¨ÖÐ¡¹ÕýÈ·Ó¦¸Ã²»»á±»ÇÐ¿ª', HMM=False)))
#¡¸/Ì¨ÖÐ/¡¹/ÕýÈ·/Ó¦¸Ã/²»»á/±»/ÇÐ¿ª

print('='*40)
print('3. ¹Ø¼ü´ÊÌáÈ¡')
print('-'*40)
print(' TF-IDF')
print('-'*40)

s = "´ËÍâ£¬¹«Ë¾Äâ¶ÔÈ«×Ê×Ó¹«Ë¾¼ªÁÖÅ·ÑÇÖÃÒµÓÐÏÞ¹«Ë¾Ôö×Ê4.3ÒÚÔª£¬Ôö×Êºó£¬¼ªÁÖÅ·ÑÇÖÃÒµ×¢²á×Ê±¾ÓÉ7000ÍòÔªÔö¼Óµ½5ÒÚÔª¡£¼ªÁÖÅ·ÑÇÖÃÒµÖ÷Òª¾­Óª·¶Î§Îª·¿µØ²ú¿ª·¢¼°°Ù»õÁãÊÛµÈÒµÎñ¡£Ä¿Ç°ÔÚ½¨¼ªÁÖÅ·ÑÇ³ÇÊÐÉÌÒµ×ÛºÏÌåÏîÄ¿¡£2013Äê£¬ÊµÏÖÓªÒµÊÕÈë0ÍòÔª£¬ÊµÏÖ¾»ÀûÈó-139.13ÍòÔª¡£"
for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))

print('-'*40)
print(' TextRank')
print('-'*40)

for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))

print('='*40)
print('4. ´ÊÐÔ±ê×¢')
print('-'*40)

words = jieba.posseg.cut("ÎÒ°®±±¾©Ìì°²ÃÅ")
for word, flag in words:
    print('%s %s' % (word, flag))

print('='*40)
print('6. Tokenize: ·µ»Ø´ÊÓïÔÚÔ­ÎÄµÄÆðÖ¹Î»ÖÃ')
print('-'*40)
print(' Ä¬ÈÏÄ£Ê½')
print('-'*40)

result = jieba.tokenize('ÓÀºÍ·þ×°ÊÎÆ·ÓÐÏÞ¹«Ë¾')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))

print('-'*40)
print(' ËÑË÷Ä£Ê½')
print('-'*40)

result = jieba.tokenize('ÓÀºÍ·þ×°ÊÎÆ·ÓÐÏÞ¹«Ë¾', mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
