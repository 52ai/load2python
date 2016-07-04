# coding = utf-8

# <。)#)))≦
# function: data cutting
"""
现有100万条短信，80万条标注好的训练集，20万条没有标注的测试集。初步将80万训练集分出切分10万条，将前8万条作为训练集用于训练模型，后2万条作为测试集，用于测试分类效果。

input: 80w_train.txt
output:10w_cut.txt

input:10w_cut.txt
output:8w_train_cut.txt 2w_test_cut.txt

"""

