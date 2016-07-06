# -*- coding:utf-8 -*-

"""
create on July 6,2016
@author:Wayne
Function: 基于TF-IDF算法构建垃圾词汇库

步骤：

一，先对所有的垃圾短信采用TF-IDF算法，进行主题词提取，组成S_Dic词库。
二，再对所有的正常短信采用TF-IDF算法，进行主题词体术，组成N_Dic词库。
三，垃圾词汇库Spam_Dic = S_Dic - S_Dic intersection N_Dic
"""

