text = ''' 
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested. 
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambxiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those! 
'''

#使用字典dict统计文本中单词出现的次数
print('文本单词出现的次数如下：\n')
t1 = text.split()
t2 = []
for x in t1:
    if x.isalpha():  #判断是否是英文字母
        t2.append(x)
        
dict1 = {}
dict1 = dict1.fromkeys(t2)
text_1 = list(dict1.keys())
for x in text_1:
    dict1[x] = t2.count(x)
print(dict1)
        
print('\n按照出现的次数从多到少输出所有单词：\n')
dict2 = {}
dict2 = sorted(dict1.items(),key=lambda d : d[1],reverse=True)
dict2 = dict(dict2)
print(dict2)