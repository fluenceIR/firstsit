# Day 1
## SQLite
- 轻量级的嵌入式的数据库
- 特点是小
    - 常用场景
    - Android,IOS,WP
-数据库常规操作与MySQL相似

## 快捷键
- alt + enter
    - 自动添加函数，自动引入包，自动创建一些东西
- Tab(在html中输入以下代码后按下，自动生成元素)
    - ul>li
    - ul*5
    - ul>li*5
    - for
- ctrl + p
    - 查看函数的参数提示
- shift + F6
    - 重命名

## 实现一个请求
- 注册一个路由
    - urls中
        - url
            - 参数① 匹配规则 正则
        - 视图函数
            - 对应的是views中的一个函数
                - 没有括号
- 去views实现对应的试图函数
    - 第一个参数是request
    - 永远记得返回Response

## 模板配置
- 两种
    - 在App中进行模板配置
        - 只需在App的根目录创建templates文件夹即可
        -如果想让代码提示，我们应该标记文件夹为模板文件夹
    - 在项目目录中进行模板配置
        - 需要在项目目录中创建templates文件夹并标记
        - 需要在settings中进行注册
    - 在开发中使用第二种
        - 模板可以继承，复用

## 路由优化配置
- 项目如果逻辑过于复杂，可以进行拆分
- 拆分为多个App
- 继续拆分路由器urls
    -在App中创建自己的urls
        - urlpatterns 路由规则列表
        - 在根urls中进行子路由的包含
    - 子路由使用
        - 跟路由的规则，子路由的规则

## models使用了ORM技术
- Objects Relateional Mapping 对象关系映射
- 将业务逻辑进行了一个解耦合
    - object.save()
    - object.delate()
- 关系型数据库
    - DDL
    - 通过models定义实现数据库表的定义
- 数据操作（增删改查）
    - 存储 
        - sava()
    - 查询
        - 查所有 objects.all()
        - 查单个 objects.get(pk=xx)
    - 更新
        - 基于查询
        - 查找到的对象，修改属性，然后save()
    - 删除
        - 基于查询的
        - 调用delete()

## 链接mysql驱动
- mysqlclient
    - python2, 3都能直接使用
    - 致命缺陷
        - 对mysql安装有要求，必须指定位置存在配置文件
- python-mysql
    - python2支持很好
    - python3不支持
- pymysql
    -python2, python3都支持
    - 它还可以伪装成前面的库

## django shell
- 继承了python环境的shell终端
- 通常在终端中做一些调试工作

## 如何看待bug
- 看日志
    - 先看第一条
    - 再看最后一条
- 梳理思路
    - 程序在哪一个位置和预期出现偏差

## 表关系
- 1:1
- 1:N
- N:N