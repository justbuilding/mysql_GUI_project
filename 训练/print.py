# -*- coding:utf-8 -*-
# Author: Jay-Q
import time
import prettytable as pt  # 请先安装prettytable模块，安装方式： pip install prettytable

balance = 1000  # 初始化余额
acount_log = [] # 初始化交易日志
class Bank:
    def __init__(self):
        """初始化"""
        global balance
        self.balance = balance
        self.acount_log = acount_log
    def deposit(self):
        """存款"""
        amount = float(input('请输入存款金额：'))
        self.balance += amount
        self.write_log(amount,'转入')
    def withdrawl(self):
        """取款"""
        amount = float(input('请输入取款金额：'))
        # 判断余额
        if amount > self.balance:
            print('余额不足')
        else:
            self.balance -= amount
            self.write_log(amount, '消费')
    def print_log(self):
        """打印交易日志"""
        tb = pt.PrettyTable()
        tb.field_names = ["交易日期", "摘要", "金额", "币种", "余额"]   # 设置表格头
        for info  in self.acount_log:
            # 判断转入还是消费，为金额前添加“+”或“-”
            if info[1] == '转入':
                amout = '+{}'.format(info[2])
            else:
                amout = '-{}'.format(info[2])
            tb.add_row([info[0],info[1],amout,'人民币',info[3]])
        print(tb)
    def write_log(self,amout,handle):
        """写入日志"""
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) # 获取创建时间
        data = [create_time, handle, amout, self.balance]   # 组装列表
        self.acount_log.append(data)    # 添加到日志列表

def show_menu():
    """显示菜单"""
    menu = '''菜单
    0：退出
    1：存款
    2：取款
    3：打印交易详情
    '''
    print(menu)
if __name__ == "__main__":
    show_menu()
    num = float(input('请根据菜单输入操作编号：'))
    bank = Bank()
    while num!= 0 :
        if num == 1:
            bank.deposit()
        elif num == 2:
            bank.withdrawl()
        elif num == 3:
            bank.print_log()
        else:
            print('您的输入有误！')
        num = float(input('请根据菜单输入操作编号：'))
    print('您已退出系统')

