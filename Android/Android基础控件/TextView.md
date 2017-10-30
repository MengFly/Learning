## TextView
### 为TextView设置下划线
 在不是URL地址或者是号码的时候也为文字添加下划线
```java
TextView tv = (TextView)findViewById(R.id.act_main_tv);
tv.setPaintFlag(Paint.UNDERLINE_TEXT_FLAG);
```