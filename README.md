## 前言
`CPCS`是一个商品比价系统，它通过爬取购物网站的商品信息，为用户提供了方便的比价功能。目前，该系统支持京东、淘宝和苏宁易购这三个知名购物网站，用户可以轻松地找到适合自己的商品，享受最优惠的购物体验。

## 项目介绍
`CPCS`项目是一套电商比价系统，它包含了前台商城系统和后台管理系统。在 Python 爬虫方面，采用了 selenium 技术；前端使用了 HTML、CSS、jQuery 和 BootStrap 技术；后端则基于 Python 和 Django 实现；数据库方面采用了 MySQL。该系统包含了首页门户、商品搜索、商品展示、分页搜索等功能模块，为用户提供了全面而便捷的购物体验。

## 项目演示
<div>
  <video controls width="640" height="360">
        <source src="movie.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>
![系统功能演示](./document/resource/show1.png)

### 组织结构

``` lua
CPCS
├── app01 -- 包含所有代码
      ├── grab_goods -- 爬取商品数据代码
      ├── migrations -- django生成数据库的代码
      ├── static -- 前端CSS和JS代码包
      ├── templates -- 前端网页模板代码
      ├── utils -- 工具类及通用代码
      └── views -- 前后端交互代码
```

### 技术选型

| 技术                 | 说明                | 官网                                           |
| -------------------- | ------------------- | ---------------------------------------------- |
| Django               | Web应用开发框架      | https://www.djangoproject.com/         |
| selenium             | 自动化Web浏览器操作工具 | https://www.selenium.dev/           |

#### 架构图

##### 系统架构图

![系统架构图](./document/resource/CPCS_system_arch.jpg)

##### 业务架构图

![业务架构图](./document/resource/CPCS_business_arch.jpg)

#### 功能介绍

- 商品搜索：[功能结构图-商品.jpg](document/resource/mind_product.jpg)
- 商品展示：[功能结构图-订单.jpg](document/resource/mind_order.jpg)
- 分页跳转：[功能结构图-促销.jpg](document/resource/mind_sale.jpg)
- 排序方式：[功能结构图-内容.jpg](document/resource/mind_content.jpg)

#### 开发进度

![项目开发进度图](./document/resource/re_mall_dev_flow.jpg)

## 环境搭建

### 开发工具

| 工具          | 说明                | 官网                                            |
| ------------- | ------------------- | ----------------------------------------------- |
| pycharm       | 开发IDE             | https://www.jetbrains.com/pycharm/download      |
| Axure         | 原型设计工具        | https://www.axure.com/                          |
| Typora        | Markdown编辑器      | https://typora.io/                              |

### 开发环境

| 工具          | 版本号 | 下载                                                         |
| ------------- | ------ | ------------------------------------------------------------ |
| Python        | 3.1    | https://www.python.org/downloads/release/python-3123/        |
| MySQL         | 8.0    | https://www.mysql.com/                                       |
