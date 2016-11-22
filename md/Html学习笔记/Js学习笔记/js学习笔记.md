#### js事件处理程序
+ Html事件处理程序

写在Html中的处理程序，例如

	<input type="button" value="按钮" id="btn" onclick="alert('hello')">

 这样的话hTML和js代码紧密耦合在一起

+ DOM0级事件处理程序，把一个函数赋值给一个事件处理程序的属性

+ DOM2级事件处理程序
 DOM2级事件处理程序定义了两个方法：
 addEventListener()和removeEventListener();
 接受三个参数（要处理的事件名，要设置的函数，是冒泡还是捕获)

+ IE事件处理程序
 attachEvent();
 detachEvent();
 接受两个参数：IE八之前的版本只支持这种方式
 经测试IE10里面已经不支持attachEvent这种方式的事件处理程序了
 [例子](Html事件处理程序.html)


#### DOM中的事件对象

#### 常用的属性
+ DOM中的事件对象
 1. type:用于获取事件类型
 2. target:用于获取事件目标
 3. stopPropagation() 方法，用于阻止事件冒泡
 4. preventDefault() 阻止默认行为
例如：
```javaScript
function stopDefault(event) {
	event.stopPropagation();//停止冒泡
	enent.preventDefault();//阻止默认行为
}
```

+ IE中的事件对象
 1.type
 2.srcElement(相当于DOM里面的target)
 3. cacelBubble 取消冒泡设置为true取消
 4. returnValue 取消默认行为设置为true取消
兼容IE和DOM可以这样
```javaScript
event = event || window.event;
var ele = event.target || event.srcElement;
```