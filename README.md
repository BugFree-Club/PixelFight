# Pixel-Fight

----

A Game Framework For Programmable AI

## 基本信息

* 该程序提供两个语言版本(python/C#),目前python版本已完成初始Demo可以进行使用与测试,C#版本尚未开发完成
* 该游戏方法与规则见(比赛规则),规则会不断更新与调整以适应玩家需求
* Python版本目前极度不完善,欢迎提出改进意见与Bug反馈

## 使用方法(Python)

* 运行环境:win10/Linux - python3.6及以上
* 本程序分为服务端与客户端两个部分,首先设置规则开启服务,其次运行客户端脚本(即玩家编写的AI逻辑部分)即可
* 运行方法
  * 进入PixelFight/pfproject_py文件夹
  * 修改游戏规则standard-rule.txt或者使用默认规则
  * 进入python运行环境或者linux终端
  * 运行服务端脚本tmp_server.py
  * 编写游戏AI逻辑部分attack_method.py
  * 运行客户端脚本(一个或多个)
  * 服务端会通过刷新图片的方式,实时显示游戏信息