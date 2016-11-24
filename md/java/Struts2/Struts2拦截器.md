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



  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
