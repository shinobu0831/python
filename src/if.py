#age = int(input('input age:'))
# if age < 18:
#     print('no vote1')
# elif age < 20:
#     print('no vote2')
# else:
#     print('no vote3')

# 三項演算子
#print('A' if age < 10 else 'B')
# 内包表記
#data = [10**n for n in range(1, 11)]
# print(data)
# リスト[]:重複可、順序保持、変更可
listA = ['1', 2, 3, 4, 5, 6, 7, 7]
listA.append(8)
print(type(listA), listA)
# タプル():重複可、順序保持、変更不可
tupleA = ('1', 2, 3, 4, 5, 6, 7, 7)
print(type(tupleA), tupleA)
# セット{}:重複不可、順不同
setA = {'1', 2, 3, 4, 5, 6, 7, 7}
setA.add(8)
print(type(setA), setA)
# 辞書
dictA = {"name": "私", "age": "36"}
dictA['memo'] = 'hoge'
print(type(dictA), dictA)
