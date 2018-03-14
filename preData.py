# Tianchi
import numpy as np
#
# def write_items(i):
#     np.savetxt( 'items.txt', i, fmt='%s' )
#
# def write_users(u):
#     np.savetxt( 'users.txt', u, fmt='%s' )
#
# def write_contexts(c):
#     np.savetxt( 'contexts.txt', c, fmt='%s' )
#
# def write_shops(s):
#     np.savetxt( 'shops.txt', s, fmt='%s' )

with open('round1_ijcai_18_train_20180301.txt') as f:
    mylist = [line.rstrip('\t').split(' ') for line in f]
    print(mylist[0])#查看所有变量 一共是 27个，其中有用户（性别-年龄-职业-口碑），商店（），商品（）
    print(mylist[1])#选取第一个样本条作为查看
    print(len(mylist[0]))#一共是 27个item数据，认真查看过，必须是按照空格分割
    # print(len( mylist ))#一共是4万多条样本数据

    for x in mylist[0]:
        print(x)
    for x in mylist[1]:
        print(x)
    # item 信息，注意查看数据信息，其中有 item_category_list 和 brand 的变化量有点多
    item = mylist[0][1:10]
    print(item)
    _item = mylist[1][1:10]
    print(_item)
    # user 信息
    user = mylist[0][10:15]
    print(user)
    _user = mylist[1][10:15]
    print(_user)
    # context 信息，其中包括 timesstamp，很重要
    context = mylist[0][15:19]
    print(context)
    _context = mylist[1][15:19]
    print(_context)
    # shop 信息，内容很多，注意：口碑分数，服务分数，快递分数，产品描述分数
    shop = mylist[0][19:26]
    print(shop)
    _shop = mylist[1][19:26]
    print(_shop)
    # label 信息，购买与否，可以先考虑到利用这个信息做有监督学习，然后不考虑这个 feature 下的无监督学习
    trade = mylist[0][-1]
    print(trade)
    _trade = mylist[1][-1]
    print(_trade)

    items = []
    users = []
    contexts =[]
    shops = []
    trades = []
    for line in mylist:
        items.append(line[1:10])
        users.append( line[10:15] )
        contexts.append(line[15:19])
        shops.append( line[19:26] )
        trades.append(line[-1])
    # write_items(items)
    # write_users(users)
    # write_contexts(contexts)
    # write_shops(shops)

    # import datetime
    #
    # ...: print(
    #     ...:     datetime.datetime.fromtimestamp(
    #     ...: int( "1284101485" )
    #     ...:     ).strftime( '%Y-%m-%d %H:%M:%S' )
    #     ...: )