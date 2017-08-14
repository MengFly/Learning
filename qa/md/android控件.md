# Android基础控件
[TOC]

## TextView
### 为TextView设置下划线[已解决]
 在不是URL地址或者是号码的时候也为文字添加下划线
```java
TextView tv = (TextView)findViewById(R.id.act_main_tv);
tv.setPaintFlag(Paint.UNDERLINE_TEXT_FLAG);
```

## EditText
### **EditText怎么不自动获取焦点，或者键盘不自动弹出**[已解决]
> 在它的父控件里面设置focusable=true以及focusableInTouchMode=true,让它的父控件截获焦点即可。

## TextInputLayout[已解决]
+ **属性和方法**
 + app:counterEnabled="true"	会在右下角出现一个数字进行计数
 + app:counterMaxLength="数字" 会以 数字/最大值 的方式出现
 + app:errorEnabled=true 开启错误显示
 + 调用setError(String);方法来设置显示的错误提示文字
 + 当不需要的时候调用app:errorEnabled(false)取消错误提示

+ **提示**
当使用app:counterMaxLength这个属性的时候
一定要设置app:counterOverflowTextAppearance属性
不然运行程序会报错，这个属性是设置当我们输入字符超过限定的个数的时候EditText的整体样式
它的属性是一个Style
例如：
```xml
<style name="errorInputStyle" parent="TextAppearance.AppCompat.Small">
	<item name="android:textColor">#f34567</item>
</style>
```
**这就设置了当输入个数超过限制后EditText的style**




