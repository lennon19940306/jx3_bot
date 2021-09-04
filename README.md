<div align="center">

# JX3_ROBOT

_✨基于[nonebot2](https://github.com/nonebot/nonebot2)的剑网三群聊机器人，采用[jx3api](https://jx3api.com)作为数据源。✨_

</div>

<p align="center">
<a href="https://www.python.org/">
<img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="license"></a>
<a href="https://github.com/nonebot/nonebot2">
<img src="https://img.shields.io/badge/nonebot-2.0.0a15-yellow"></a>
<a href="https://github.com/Mrs4s/go-cqhttp">
<img src="https://img.shields.io/badge/go--cqhttp-v1.0.0--beta6-red"></a>
</p>

## 简介
基于nonebot2的剑网三的QQ群聊机器人，采用jx3api为数据接口，提供剑网三的一些查询，娱乐功能。

- 兼容windows，linux平台
- 全异步处理，支持多个群操作
- 使用websockets连接jx3api
- 适配nonebot2风格代码，自定义事件

## 部署机器人
### 安装环境
**项目需要python环境，且需要[python3.9+](https://www.python.org/downloads/)。**
```
apt-get install python3.9
```

**QQ协议端采用[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)。**

- go-cqhttp需要下载ffmpeg环境，windows点击[这里](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z)下载，具体安装请参考[文档](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%AE%89%E8%A3%85-ffmpeg)。

### 安装依赖
```
pip install -r requirements.txt
```

### 配置设置
#### configs.config.py
```
CHAT_NLP = {
    "secretId": "",  # 腾讯云API的secretId
    "secretKey": ""  # 腾讯云API的secretKey
}
CHAT_VOICE = {
    "appkey": "",  # 阿里云的语音接口appkey
    "access": "",  # 阿里云的语音接口access
    "secret": "",  # 阿里云的语音接口secret
}

# 其他设置参考打开文件自行修改
```
**使用腾讯云API进行闲聊操作，如果没有将使用[青云客API](http://api.qingyunke.com/)返回聊天**

- 申请地址：[点击申请](https://console.cloud.tencent.com/cam/capi) NLP自然语言处理：[点击申请](https://console.cloud.tencent.com/nlp)

- 申请成功后，获取访问密钥流程请参考[这里](https://cloud.tencent.com/document/product/598/45511)

**阿里云API进行语音合成，如果没有将不会发送语音信息。**
- appkey和access申请地址：[点击申请](https://nls-portal.console.aliyun.com/overview)

- 获取secret地址：[点击这里](https://usercenter.console.aliyun.com/)
#### .env.pord
```
NICKNAME=["团子", "小团子"] # 这里设置机器人的昵称
SUPERUSERS=[""] # 这里填超级用户的QQ号，超级用户是机器人的主人
```

### 启动
```
python bot.py
```
### 日志
**日志保存路径在：/log/，分为3个等级：ERROR，INFO，DEBUG，日志默认保存10天，以日期命名。**

## 功能列表
### 通用功能
|**插件**|**命令** |**说明**|
| :----: | :----: | :----: |
|自动插话|-|机器人会自动插话，可以修改活跃度|
|自动复读|-|机器人会自动复读|
|推送消息|-|推送官方新闻，奇遇播报，开服情况|
|签到|签到|简单的签到系统|
|智能闲聊|@机器人+你要说的话|默认使用腾讯API，辅助青云客API|
|查询功能|具体参考功能|提供查询消息接口，接口使用jx3api|

### 查询功能
|**功能**|**命令**|**说明**|
| :----: | :----: | :----: |
|日常查询|日常|查询绑定服务器当天日常|
|开服查询|开服|查询绑定服务器开服情况|
|金价查询|金价|查询绑定服务器金价|
|花价查询|花价|查询绑定服务器花价|
|配装查询|配装 [职业]|查询职业配装|
|奇穴查询|奇穴 [职业]|查询职业奇穴|
|小药查询|小药 [职业]|查询职业小药|
|宏查询|宏 [职业]|查询职业的宏|
|物价查询|物价 [外观]|查询外观的物价|
|奇遇前置|前置 [奇遇]|查询奇遇的前置条件|
|考试查询|考试 [题目]|查询题目答案，支持模糊搜索|
|器物谱|器物谱 [地图]|查询地图的家具|
|装饰查询|装饰 [装饰]|查询装饰的信息|
|奇遇查询|奇遇 [角色] [奇遇]|查询绑定服务器中该角色的该奇遇触发情况|
|挂件查询|挂件 [挂件]|查询挂件详情|
|角色装备属性|装备 [角色]|查询绑定服务器中该角色的装备属性|

### 管理功能
**管理功能需要群管理，或者超级用户才能使用**
|**功能**|**命令**|**说明**|
| :----: | :----: | :----: |
|绑定服务器|服务器 [服务器名]|更换群绑定的服务器|
|插件开关|设置 [插件名] [开/关]|开关某一个插件|
|活跃值|活跃值 [1-99]|设置机器人活跃值|
|更新信息|更新|手动更新群成员信息|

## 感谢
* [onebot](https://github.com/howmanybots/onebot)：聊天机器人应用接口标准。
* [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)：cqhttp的golang实现。
* [nonebot2](https://github.com/nonebot/nonebot2)：跨平台Python异步机器人框架。
* [jx3_api](https://jx3api.com/)：剑三API提供的数据支持。
