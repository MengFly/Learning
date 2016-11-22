# Struts2学习笔记
[TOC]


## Struts是什么
Struts2是 Java程序员必须掌握的一门课程
Struts : 支柱,枝干,来源于建筑和旧时飞机的框架
Apache软件基金会
基于MVC设计模式的Web应用框架
减少在运用MVC设计模型来开发Web应用的时间

### MVC模式
+ Model
+ View
+ Controller
**在改进和个性化定制界面及用户交互的同时,不需要重新编写业务逻辑**
用户输入 --> Controller --> Model --> View --> 用户
在Struts中,Controller就是Action


### Struts发展简史
Struts1	2001年
Struts2 2007年 是在WebWork基础上进行设计的,是WebWork的一个升级
吸收了Struts1和WebWork两者的优点


### Struts2环境搭建
#### Apache Struts2环境基础
**Servlet Api 2.4**
**JSP API 2.0**
**Java 5以上(因为要用到注解)**

#### 搭建Struts2环境步骤
1. 下载相关的jar包
2. 创建Web项目
3. 创建并完善相关配置文件
4. 创建Action并测试启动

#### Struts官方网站
http://struts.apache.org/

#### Struts2最基础的Jar包
Commons-fileupload
Commons-io
Commons-lang
Commons-logging
javassist
freemarker	模版引擎
Struts-core	Struts核心包
xwork-core
ongl


#### 在Web.xml中进行配置
**设置过滤器**
```xml
<filter>
 	<filter-name>struts2</filter-name>
 	<filter-class>org.apache.struts2.dispatcher.ng.filter.StrutsPrepareAndExecuteFilter</filter-class>
 </filter>

 <filter-mapping>
 	<filter-name>struts2</filter-name>
 	<url-pattern>/*</url-pattern>
 </filter-mapping>

```
 filter和filter-mapping中的filter-name要相同
 filter-class中是Struts2中的过滤器

####  创建struts.xml文件
```xml
 <?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE struts PUBLIC
	"-//Apache Software Foundation//DTD Struts Configuration 2.3//EN"
	"http://struts.apache.org/dtds/struts-2.3.dtd">

<struts>
</struts>
```

#### 创建Action
```java
package com.mengfly.action;

import com.opensymphony.xwork2.ActionSupport;

public class HelloStruts2Action extends ActionSupport {

	@Override
	public String execute() throws Exception {
		System.out.println("执行Action");
		return SUCCESS;
	}
}
```

#### 在struts.xml配置Action
```xml
<package name="default" namespace="/" extends="struts-default">
	<action name="hellostruts" class="com.mengfly.action.HelloStruts2Action">
		<result>/result.jsp</result>

	</action>

</package>
```

#### 创建result.jsp文件
```xml
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Insert title here</title>
</head>
<body>
	This is result.jsp
</body>
</html>
```

#### 之后部署,执行Action就可以了

### Struts2的工作原理以及文件结构
在web.xml文件中配置的filter会过滤请求
找到具体的action请求再在struts.xml中找到具体的执行类

#### struts2核心文件
##### web.xml
任何MVC框架都需要与Web应用整合,这就需要借助web.xml
只有配置在web.xml中的Servlet才会被应用加载
所有的MVC框架都需要Web应用加载一个核心控制器,对于Struts2框架而言需要加载**StrutsprepareAndExecuteFilter**,
只要加载了**StrutsPrepareAndExecuteFilter**,**StrutsPrepareAndExecuteFilter**就会加载Struts2框架


##### struts.xml
struts2的核心配置文件
主要负责管理Action映射,以及Action包含的Result定义
###### struts.xml中包含的内容:
1. 全局属性
2. 用户请求和相应Action之间的对应关系
3. Action可能用到的参数和返回结果
4. 这种拦截器的配置

使用include包含其他的struts文件

+ package标签
	package的名字必须是唯一的,package可以扩展
	当一个package扩展另一个package时,该package会在本身配置上加入扩展的package的配置,父package必须在子package前配置
 - name:包名
 - entends:继承的父package的包名
 - namespace:定义package命名空间,该命名空间影响url地址,例如定义为/test,访问它下面的user.action的话,需要访问.../test/user.action
 - global-results:
  全局的result配置

 - action
	一个Action可以被多次映射(只要action中配置的name不同)
   + name:action的名称
		....name.action
   + class:Action的类名
   + method指定要执行的方法
	在Action中也可以设置拦截器以及result


+ constant
		在这个标签里面配置的常量,就等同于在struts.properties中配置的属性

###### struts.properties
struts2框架的全局属性文件.自动加载
放置的位置和struts.xml放在同一个位置
包含很多key-value简直对
这个文件可以不要,这些可以在struts.xml中进行配置

#### 访问Servlet Api
Servlet
 + doGet
 + doPost

**提供了三种方式去访问Sevlet Api**
1、ActionContext
2、实现***Aware接口
3、ServletActionContext

#### Action搜索顺序
http://localhost:8080/struts2/path1/path2/path3/student.action
第一步：判断package是否存在，如：path1/path2/path3/
如果存在，就去寻找是否有Action
如果Action存在，则没有问题
如果Action不存在，则会报错
如果不存在，检查上一级的package是否存在，重复第一步

#### 动态方法调用
解决一个Action处理过个请求的情况
**三种解决方式**

1. 指定method属性
```xml
<action name="hellostruts" method = "add" class="com.mengfly.action.HelloStruts2Action">
<result>/result.jsp</result>
</action>
```
这样就会在相关的Action中找到method中指定的方法去执行

2. 感叹号方式
> 官方不太推荐的方式

要使用感叹号方式，就需要开启一个功能（在struts.xml中）
```xml
<constant name="struts.enable.DynamicMethodInvocation" value="true"></constant>
<action name="hellostruts" class="com.mengfly.action.HelloStruts2Action">
<result>/result.jsp</result>
<result name="add">/add.jsp</result>
</action>
```
这个时候再Action类里面就得给响应的方法返回result的值才会执行响应的result
例如result的name为add，那么方法就应该返回"add"
访问的时候：
http://localhost:8080/HelloStruts2/hellostruts!add.action

3. 通配符方式
```xml
<action name="hellostruts_*" method="{1}" class="com.mengfly.action.HelloStruts2Action">
<result>/{1}.jsp</result>
</action>
```

#### 指定多个配置文件
	例如：
		<include file="login.xml"></inclide>
		<include file="system.xml"></include>

#### 默认Action
	当找不到Action的时候就可以访问默认的Action

#### Struts2后缀
	<constant name="struts.action.extension" value="action,html"></constant>

### 接受参数
1. 使用Action的属性接收
**实例:模拟登陆**
**JSP**
```xml
<body>
	<form action="LoginAction.action" method="post">
		用户名:<input type="text" name="userName">
		密  码 :<input type="password" name="password">
		<input type="submit" value="提交"> 
	<form>
</body>
```
**struts.xml**
```xml
<action name="LoginAction" method="login" class="com.mengfly.action.LoginAction">
	<result>/success.jsp</result>
</action>
```

**	LoginAction**
```java
package com.mengfly.action;

import com.opensymphony.xwork2.ActionSupport;

public class LoginAction extends ActionSupport {

	private String userName;

	private String password;

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String login() {
		System.out.println(userName);
		return SUCCESS;
	}
}
```


2. DomainModel接受参数
**代码 :**
**JSP**
```xml
<form action="LoginAction.action" method="post">
	用户名:<input type="text" name="user.userName">
	密  码 :<input type="password" name="user.password">
	<input type="submit" value="提交"> 
</form>
```

**struts.xml**
```xml
<action name="LoginAction" method="login" class="com.mengfly.action.LoginAction">
	<result>/success.jsp</result>
</action>
```

**	LoginAction**
```java
package com.mengfly.action;

import com.mengfly.entity.User;
import com.opensymphony.xwork2.ActionSupport;

public class LoginAction extends ActionSupport {

	private User user;

	public User getUser() {
		return user;
	}

	public void setUser(User user) {
		this.user = user;
	}

	public String login() {
		System.out.println(user.getUserName());
		return SUCCESS;
	}
}
```

**User类**
```java
package com.mengfly.entity;

public class User {

	private String userName;

	private String password;

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

}
```

3. 使用ModelDeiven接受参数
**实现ModelDeiven接口**
**推荐使用这种方式**
**JSP**
```xml
<form action="LoginAction.action" method="post">
	用户名:<input type="text" name="userName">
	 密  码 :<input type="password" name="password">
	<input type="submit" value="提交">
</from>
```

**struts.xml(不变)**

**User(不变)**

**LoginAction**
```java
package com.mengfly.action;

import com.mengfly.entity.User;
import com.opensymphony.xwork2.ActionSupport;
import com.opensymphony.xwork2.ModelDriven;

public class LoginAction extends ActionSupport implements ModelDriven<User>{

	private User user = new User();

	public String login() {
		System.out.println(user.getUserName());
		return SUCCESS;
	}

	@Override
	public User getModel() {
		return user;
	}
}
```

如果要对List进行赋值的话,再JSP中的name应该写成这样
bookList[0]

### 处理结果类型
Struts2处理流程
	用户请求 --> Struts2框架 --> 控制器(Action) --> Struts框架 --> 视图资源
处理的结果是字符串
```xml
<result name="success">/success.jsp</result>
```
带有斜杠的就是项目绝对路径

结果类型:
	SUCCESS	正确执行
	NONE
	ERROR
	LOGIN
	INPUT

### 处理结果类型
处理结果是通过在struts.xml中使用<result/>标签配置结果
根据位置不同,分为两种结果:
+ 局部结果
将result作为action的子元素进行配置
+ 全局结果
将result作为global-result元素的子元素进行配置
global-result标签是配置在package标签下面的













