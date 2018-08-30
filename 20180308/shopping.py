#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

is_exit = 0
goods_list=[
    [0,'phone',2500],
    [1,'book',80],
    [2,'T-shirt',50],
    [3,'frut',25]
]
buy_goodsd_list=[]

while not is_exit:
    salary=int(raw_input('your slalary:'))
    print 'your money is:',salary
    #不要修改这种不变的值，初始值是不会变的
    leave_money = salary

    #goods_list，商品会反复选，所以要嵌一个循环
    while not is_exit:
        buy_goodsd_id = -1
        print 'here some goods to choose:'
        for i in goods_list:
            print i
        #处理可能的异常
        try:
            buy_goodsd_id_str=raw_input("choose goods'number to buy")
            buy_goodsd_id = int(buy_goodsd_id_str)
        except:
            if buy_goodsd_id_str == 'q':
                is_exit = 1
                print 'your choose exit'
                print 'now,your money is:', leave_money
                print 'your goods list are:'
                for goods in buy_goodsd_list:
                    print goods
                break
            else:
                print 'choose wrong,please choose again'
                continue
        if (buy_goodsd_id >= 0 and buy_goodsd_id <= len(goods_list) - 1):
            leave_money = leave_money-int(goods_list[buy_goodsd_id][2])
            if leave_money < 0:
                print 'sorry your money is not enouth,please choose again'
                #记得把钱补回去
                leave_money = leave_money + int(goods_list[buy_goodsd_id][2])
                continue
            else:
                print 'now,your money is:', leave_money
                print 'your goods list are:'
                buy_goodsd_list.append(goods_list[buy_goodsd_id])
                for goods in buy_goodsd_list:
                    print goods
        else:
            print 'choose wrong'


