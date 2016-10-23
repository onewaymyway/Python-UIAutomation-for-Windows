#!python3
# -*- coding: utf-8 -*-
import os
import time
import subprocess
import ctypes
import automation

window = automation.WindowControl(searchDepth = 1, Name = '网上股票交易系统5.0')
print(window)
fbtn=automation.TreeItemControl(searchFromControl = window,Name="卖出[F2]")
print(fbtn)
#fbtn.Click()
actionTree=automation.TreeControl(searchFromControl=window,AutomationId="129")


def buyAction(code,price,count):
    window.SendKeys("{F1}")
    panel=automation.PaneControl(searchFromControl=window,ClassName="#32770")
    print(panel)
    codeTxt=automation.EditControl(searchFromControl=panel,AutomationId="1032")
    codeTxt.SetValue(code)
    priceTxt=automation.EditControl(searchFromControl=panel,AutomationId="1033")
    priceTxt.SetValue(str(price))
    countTxt=automation.EditControl(searchFromControl=panel,AutomationId="1034")
    countTxt.SetValue(str(count))

    buyBtn=automation.ButtonControl(searchFromControl=panel,AutomationId="1006")
    buyBtn.Click(simulateMove=False)

    alertwindow=automation.PaneControl(searchDepth = 1,searchFromControl=window,ClassName="#32770")

    sureBtn=automation.ButtonControl(searchFromControl=alertwindow,AutomationId="6")
    print(sureBtn)
    sureBtn.Click(simulateMove=False)
    #sureBtn.Click(simulateMove=False)

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

def getMyInfo():
    btn=getTreeItem(actionTree,"资金股票")
    btn.Click(simulateMove=False)
    infoPane=automation.PaneControl(searchFromControl=window,AutomationId="59649")
    rst={}
    #rst["allmoney"]=getTxtFromPane(infoPane,"1012")
    for key in myInfoDic:
        rst[key]=getTxtFromPane(infoPane,myInfoDic[key])
        
    print(rst)
    

    
    
    
    
    
getMyInfo()
#buyAction("600213",14.00,100)
