# Struts2拦截器
Struts的核心功能的实现就是通过拦截器来实现的

## 什么是拦截器
Struts大多数核心功能都是通过拦截器来实现的
拦截器就是在Action执行之前或者在Action执行之后进行执行

### 拦截器栈
拦截器栈相当于多个拦截器的组合
实际上也是拦截器

### 工作原理
执行过程是一个递归的过程
例如:
Action执行之前执行了拦截器1和拦截器2
那么在Action执行完成之后产生的结果还会经过拦截器2和拦截器1处理之后才会返回给客户端

## 自定义拦截器
**两种方式**

+ 方式一:实现Interceptor接口
 这种方式还需要实现init()和destroy()方法,比较麻烦
 - void init():初始化拦截器所需的资源
 - void destroy():释放在init()中分配到资源
 - String intercept(ActionInvocation ai) throwsException
  + 实现拦截器功能
  + 利用ActionInvocation参数获取Action状态
  + 返回result字符串作为逻辑视图

+ 方式二:继承AbstractInterceptor类
 一般来说都会去继承这个父类
 - 提供了init()和destroy()方法的空实现
 - 只需要实现intercept方法即可

## 拦截器实例
### 计算Action的执行时间
思路:在调用Action之前调用拦截器记录时间,在Action调用之后再调用拦截器记录时间.
两者时间想减就得到Action的执行时间了

实现步骤:
 + 创建拦截器
 + 在配置文件中定义拦截器并引用它

**案例实现**

1. 在web.xml中配置控制器
 ```xml
<filter>
  	<filter-name>timerfilter</filter-name>
  	<filter-class>org.apache.struts2.dispatcher.ng.filter.StrutsPrepareAndExecuteFilter</filter-class>
  </filter>
  <filter-mapping>
  	<filter-name>timerfilter</filter-name>
  	<url-pattern>/*</url-pattern>
  </filter-mapping>
```

2. index.jsp
 设置一个连接去访问Action
```xml
<a href="timer">访问Action并计算执行Action花费的时间</a>
```

3. 定义Action类(TimerAction)
```java
package com.mengfly.action;

import com.opensymphony.xwork2.ActionSupport;

public class TimerAction extends ActionSupport {

	@Override
	public String execute() throws Exception {
		for(int i = 0;i < 1000; i ++) {
			System.out.println("I Love STRUTS");
		}
		return SUCCESS;
	}
	
}

```

4. 在struts.xml中配置action
```xml
<package name="default" namespace="/" extends="struts-default">
		<action name="timer" class="com.mengfly.action.TimerAction">
			<result>/success.jsp</result>
		</action>
		
</package>
```

5. 创建success.jsp作为访问Action成功的界面
```xml
<p>访问Action成功</p>
```

6. 创建拦截器类(TimerInterceptor)
```java
package com.mengfly.interceptor;

import com.opensymphony.xwork2.ActionInvocation;
import com.opensymphony.xwork2.interceptor.AbstractInterceptor;

/**
 * 计算执行Action花费的时间
 * @author mengfei
 *
 */
public class TimerInterceptor extends AbstractInterceptor {

	@Override
	public String intercept(ActionInvocation invocation) throws Exception {
		//1.执行Action之前
		long start = System.currentTimeMillis();
		//2.执行下一个拦截器,如果是最后一个拦截器,则执行目标Action
		String result = invocation.invoke();
		//3.执行Action之后
		long end = System.currentTimeMillis();
		
		System.out.println("执行Action花费的时间:" + (end - start) + "ms");
		return result;
	}

}
```

7. 在struts.xml中配置拦截器(也是在package下面)
```xml
<!-- 注册拦截器 -->
<interceptors>
	<interceptor name="mytimer" class="com.mengfly.interceptor.TimerInterceptor"></interceptor>
</interceptors>
```

8. 在Action下面引用拦截器
```xml
<action name="timer" class="com.mengfly.action.TimerAction">
	<result>/success.jsp</result>
	<!-- 引用拦截器 -->
	<interceptor-ref name="mytimer"></interceptor-ref>
</action>
```

## Struts2内建拦截器
这些内置的拦截器在struts2的jar包里面的配置文件里面都可以找到(struts-default.xml)
+ params 拦截器
 负责将请求的参数设置为Action属性
+ staticParams 拦截器
 将配置文件中action元素的子元素param参数设置为action属性
+ servletConfig 拦截器
 将源于Servlet API的各种对象注入到Action, 必须实现对应的接口
+ fileUpload 拦截器
 对文件上传提供支持,将文件和元数据设置到对应的Action属性
+ exception 拦截器
 捕获异常,并将异常映射到用户自定义的错误页面
+ alidation 拦截器
 调用验证框架进行数据验证
...

### 默认拦截器栈
只要在定义包的时候继承struts-default包,那么defaultStack将是默认的拦截器
当包中的某个Action显示指定了某个拦截器,则默认的拦截器不会起作用
拦截器栈中的各个拦截器的顺序很重要

也就是说如果我们为Action设置了自定义的拦截器而又想让默认的拦截器起作用的时候这个时候就需要我们手动将默认的拦截器添加上
一般会 先去引用默认的拦截器栈,再去引用我们自定义的拦截器
例如上面的例子中,对于timer这个Action默认的拦截器已经不起作用了,如果我们想让它继续起作用
就需要手工设置默认的拦截器
例如:
```xml
<action name="timer" class="com.mengfly.action.TimerAction">
	<result>/success.jsp</result>
	<!-- 手动设置默认的拦截器栈 -->
	<interceptor-ref name="defaultStack"></interceptor-ref>
	<!-- 引用拦截器 -->
	<interceptor-ref name="mytimer"></interceptor-ref>
</action>
```

### 小案例(开发权限验证拦截器)
**案例介绍**
 用户未登录不允许访问页面
**案例原理介绍:**
1. 用户点击登陆之后请求auth的action
2. 为auth.action配置拦截器
3. 在执行action之前进行判断,如果session中存在用户信息,那么就直接进入登陆成功界面
4. 如果用户信息不存在就进入登陆界面
5. 如果用户登陆成功,那么就保存用户信息
**代码如下**
+ 主界面(设置连接去访问auth.action)
```xml
<a href="auth">去登陆</a>
```
+ 用户登陆界面(访问login.action)
```xml
<h2>用户登陆</h2>
${loginError}
<form action="login" method="post">
	用户名 : <input type="text" name="username"><br /> 
	密 码 : <input type="password" name="password"><br> 
	<input type="submit" value="登陆">
</form>
```
+ 登陆成功页面(WEB-INF/page/manager.jsp,放在WEB-INF中的页面不会被外部直接访问到)
```xml
后台管理页面,只有已经登录的用户才能访问
```
+ LoginAction
```java
import java.util.Map;

import org.apache.struts2.interceptor.SessionAware;

import com.mengfly.entity.User;
import com.opensymphony.xwork2.ActionSupport;
import com.opensymphony.xwork2.ModelDriven;

public class LoginAction extends ActionSupport implements ModelDriven<User>, SessionAware{
	
	private User user = new User();
	private Map<String, Object> session;
	
	@Override
	public User getModel() {
		return user;
	}

	/**
	 * 获取Session
	 */
	@Override
	public void setSession(Map<String, Object> session) {
		this.session = session;
	}
	
	/**
	 * 处理登陆请求
	 */
	public String login() {
		if("admin".equals(user.getUsername()) && "123".equals(user.getPassword())) {
			//用户登陆成功
			session.put("loginInfo", user);
			return SUCCESS;
		} else {
			session.put("loginError", "用户名或密码不正确");
			return ERROR;
		}
	}

}

```
+ 设置拦截器
```java
package com.mengfly.interceptor;

import java.util.Map;

import com.opensymphony.xwork2.ActionContext;
import com.opensymphony.xwork2.ActionInvocation;
import com.opensymphony.xwork2.interceptor.AbstractInterceptor;

public class AuthInterceptor extends AbstractInterceptor {

	@Override
	public String intercept(ActionInvocation arg0) throws Exception {
		ActionContext context = ActionContext.getContext();
		Map<String, Object> session = context.getSession();
		if(session.get("loginInfo") != null) {
			String result = arg0.invoke();
			return result;
		} else {
			return "login";
		}
	}

}
```

+ 在struts.xml中配置Action和拦截器
 为了在action里面同时引用我们自定义的拦截器,我们创建了一个拦截器栈,把struts2默认的拦截器和我们自定义的拦截器放在了一起
```xml
<package name="default" namespace="/" extends="struts-default">
	<!-- 注册拦截器 -->
	<interceptors>
		<interceptor name="auth" class="com.mengfly.interceptor.AuthInterceptor"></interceptor>
		<interceptor-stack name="myStack">
			<interceptor-ref name="defaultStack"></interceptor-ref>
			<interceptor-ref name="auth"></interceptor-ref>
		</interceptor-stack>
	</interceptors>
	<!-- 通过这个Action去访问用户登陆成功页面,判断用户是否已经登陆,如果已经登陆,那么就直接进入登陆成功页面.如果没有登陆,那么就访问login.jsp -->
	<action name="auth">
		<!-- 引用自定义的拦截器栈  -->
		<result>/WEB-INF/page/manager.jsp</result>
		<result name="login">/login.jsp</result>
		<interceptor-ref name="myStack"></interceptor-ref>
	</action>
	<action name="login" class="com.mengfly.action.LoginAction" method="login">
		<result>/WEB-INF/page/manager.jsp</result>
		<result name="error">login.jsp</result>
	</action>
</package>
```

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
