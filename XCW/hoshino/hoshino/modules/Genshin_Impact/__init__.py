from hoshino import Service


sv = Service("原神帮助")


help_txt1 = '''
原神相关插件
插件仓库在 https://github.com/H-K-Y/Genshin_Impact_bot.git
'''.strip()
help_txt2 = '''
抽卡指令：
- [@bot相遇之缘]：10连抽卡
- [@bot纠缠之缘]：90连抽卡
- [@bot原之井]：180连抽卡
- [原神卡池]：查看当前UP池，这个指令也可以用来重载卡池配置文件，config.json保存的是当前卡池信息
- [原神卡池切换]：切换其他原神卡池
'''.strip()
help_txt3 = '''
丘丘语指令：
[丘丘一下 丘丘语句] ：翻译丘丘语,注意这个翻译只能把丘丘语翻译成中文，不能反向
[丘丘词典 丘丘语句] ：查询丘丘语句的单词含义
'''.strip()
help_txt4 = '''
查找资源指令：
-[找风神瞳 <神瞳编号>]：让机器人发送风神瞳的位置，神瞳编号为可选参数，不写编号机器人会随机一个编号，风可以换成岩来找岩神瞳
-[找到神瞳了 <神瞳编号>]：让机器人记录这个神瞳编号，以后机器人不会给你发送这个编号
-[@bot删除找到神瞳 <神瞳编号>]：在你已经找到的神瞳记录里删除这个编号
-[@bot重置风神瞳找到记录] ： 删除所有风神瞳的找到记录，这个指令会有二次确认，风可以换成岩来重置岩神瞳的记录
-[@bot找到多少神瞳了] ： 查看当前你找到多少神瞳了
-[@bot没找到的风神瞳] ： 查看没有找到的风神瞳地图位置和编号
-[XXX哪里有]：查询XXX的位置图，XXX是资源的名字
-[原神资源列表]：查询所有的资源名称
'''.strip()
help_txt5 = '''
圣遗物收集:
- [原神副本] ： 查询当前有哪些副本，掉落哪个套装  
- [刷副本 副本名称] ： 刷一次副本，可获得狗粮点数和圣遗物  
- [查看圣遗物仓库 1] ： 查询仓库第一页有哪些圣遗物  
- [强化圣遗物10级 5] ： 把仓库编号为5的圣遗物强化10级  
- [圣遗物洗点 5] ： 把仓库编号为5的圣遗物洗点，洗点后返还50%的强化点数，强化等级降为0，全属性重新随机  
- [圣遗物详情 5] ： 查看圣遗物详情
- [转换狗粮 5] ： 把仓库编号为5的圣遗物销毁转化为狗粮，会返还80%狗粮点数  
- [查看体力值] ： 查看自己体力值  
- [氪体力 @群友] ： 给群友氪体力，这个命令只有机器人管理员才能执行  
'''.strip()


@sv.on_fullmatch("原神帮助")
async def help(bot, ev):
    uid = ev['user_id']
    gid = ev['group_id']
    data_all = []
    data1 ={
            "type": "node",
            "data": {
                "name": 'Q群原神管家',
                "uin": '2854196310',
                "content": help_txt1
            }
            }
    data2 ={
            "type": "node",
            "data": {
                "name": 'Q群原神管家',
                "uin": '2854196310',
                "content": help_txt2
            }
            }
    data3 ={
            "type": "node",
            "data": {
                "name": 'Q群原神管家',
                "uin": '2854196310',
                "content": help_txt3
            }
            }
    data4 ={
            "type": "node",
            "data": {
                "name": 'Q群原神管家',
                "uin": '2854196310',
                "content": help_txt4
            }
            }
    data5 ={
            "type": "node",
            "data": {
                "name": 'Q群原神管家',
                "uin": '2854196310',
                "content": help_txt5
            }
            }
    data_all=[data1,data2,data3,data4]
    await bot.send_group_forward_msg(group_id=ev['group_id'], messages=data_all)


