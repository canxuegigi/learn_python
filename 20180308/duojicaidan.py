#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


exit_flag = False
current_layer = menu

"""
把字典助威列表，列表元素为字典
"""
layers = [menu]
print layers
"""
下面的代码很精简，多个循环使用一个循环处理，抽象出来
"""
while not  exit_flag:
    """当前层在变化，一会是字典一会是列表"""
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if choice == "b":
        current_layer = layers[-1]
        #print("change to laster", current_layer)
        layers.pop()
    elif choice not  in current_layer:continue
    else:
        """将上层的保留下来，方便后退"""
        layers.append(current_layer)
        current_layer = current_layer[choice]