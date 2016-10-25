#!python3
# -*- coding: utf-8 -*-
import os
import time
import subprocess
import ctypes
import automation

window = automation.WindowControl(searchDepth = 1, ClassName = 'TdxW_MainFrame_Class')
print(window)
fbtn=automation.TreeItemControl(searchFromControl = window,Name="买入")
print(fbtn)
#fbtn.Click()
actionTree=automation.TreeControl(searchFromControl=window,AutomationId="59648")
print(actionTree)

def clickSwitchBtn(name):
    btn=automation.ButtonControl(searchFromControl=window,Name=name)
    btn.Invoke();
    
def buyAction(code,price,count):
    clickSwitchBtn("买入");
    panel=automation.PaneControl(searchFromControl=window,AutomationId="59649")
    print(panel)
    codeTxt=automation.EditControl(searchFromControl=panel,AutomationId="12005")
    codeTxt.SetValue(code)
    priceTxt=automation.EditControl(searchFromControl=panel,AutomationId="12006")
    priceTxt.SetValue(str(price))
    countTxt=automation.EditControl(searchFromControl=panel,AutomationId="12007")
    countTxt.SetValue(str(count))

    buyBtn=automation.ButtonControl(searchFromControl=panel,AutomationId="2010")
    buyBtn.Click(simulateMove=False)
    sureBtn=automation.ButtonControl(searchFromControl=window,AutomationId="7015")
    sureBtn.Click(simulateMove=False)


def sellAction(code,price,count):
    clickSwitchBtn("卖出");
    panel=automation.PaneControl(searchFromControl=window,AutomationId="59649")
    codeTxt=automation.EditControl(searchFromControl=panel,AutomationId="12005")
    codeTxt.SetValue(code)
    priceTxt=automation.EditControl(searchFromControl=panel,AutomationId="12006")
    priceTxt.SetValue(str(price))
    countTxt=automation.EditControl(searchFromControl=panel,AutomationId="12007")
    countTxt.SetValue(str(count))

    sellBtn=automation.ButtonControl(searchFromControl=panel,AutomationId="2010")
    sellBtn.Click(simulateMove=False)

    sureBtn=automation.ButtonControl(searchFromControl=window,AutomationId="7015")
    sureBtn.Click(simulateMove=False)
    sureBtn=automation.ButtonControl(searchFromControl=window,AutomationId="7015")
    sureBtn.Click(simulateMove=False)


def parseOrderInfo(stockItem):
    rst={}
    childs=stockItem.GetChildren()
    for i in range(0,len(childs)):
        #print(i)
        rst[orderInfoList[i]]=childs[i].Name
    return rst

orderInfoList=["time","code","name","action","state","price","count","id","dealprice","dealcount","type","account"]
def getOrdersInfo(itemList):
    rst=[]
    for item in itemList:
        if isinstance(item,automation.ListItemControl):
            rst.append(parseOrderInfo(item))

    return rst;

def getOrderInfo():
    clickSwitchBtn("撤单");
    stockPane=automation.ListControl(searchFromControl=window,AutomationId="1567")
    stocks=stockPane.GetChildren()
    stockList=getOrdersInfo(stocks);
    print(stockList)
    
    
def getTreeItem(tree,name):
    item=automation.TreeItemControl(searchFromControl = tree,Name=name)
    return item

def getTxtFromPane(panel,autoId):
    txt=automation.TextControl(searchFromControl=panel,AutomationId=autoId)
    return txt.Name

myInfoDic={
    "allmoney":"1012",
    "canuse":"1016",
    "freeze":"1013",
    "cantake":"1017",
    "stock":"1014",
    "all":"1015"
    }
def parseMyInfo(msg):
    msgs=msg.split("  ")
    rst={}
    for key in msgs:
        key=key.strip()
        if key.find(":")>=0:
            arr=key.split(":")
            rst[arr[0]]=arr[1]
    return rst

def getChildsByClz(pane,clz):
    rst=[]
    itemList=pane.GetChildren()
    for item in itemList:
        if isinstance(item,clz):
            rst.append(rst)

    return rst;

stockInfoList=["code","name","count","count","avg_cost","price","value","lost","lostpercent","account"]
def parseStockInfo(stockItem):
    rst={}
    childs=stockItem.GetChildren()
    for i in range(0,len(childs)):
        rst[stockInfoList[i]]=childs[i].Name
    return rst


def getStocksInfo(itemList):
    rst=[]
    for item in itemList:
        if isinstance(item,automation.ListItemControl):
            rst.append(parseStockInfo(item))

    return rst;
    
    
def getMyInfo():
    clickSwitchBtn("持仓")
    infoPane=automation.PaneControl(searchFromControl=window,AutomationId="59649")

    info=getTxtFromPane(infoPane,"1576")
    print(info)
    rst=parseMyInfo(info)
    stockPane=automation.ListControl(searchFromControl=infoPane,AutomationId="1567")
    stocks=stockPane.GetChildren()
    stockList=getStocksInfo(stocks);
    print(stockList)


    
def haha():
    for key in myInfoDic:
        rst[key]=getTxtFromPane(infoPane,myInfoDic[key])
        
    print(rst)
    
    
    
    
    
getMyInfo()
#buyAction("600213",14.00,100)
#sellAction("002751",100.00,100)
#getOrderInfo()
