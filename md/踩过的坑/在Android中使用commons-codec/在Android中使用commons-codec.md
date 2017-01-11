## 在Android中使用commons-codec
本来准备在项目里面是使用Commons-codec,原因是它里面对java加解密进行了封装,使用起来更方便,但是当我写完代码后却出现这样的错误
```xml
java.lang.NoSuchMethodError: org.apache.commons.codec.binary.Hex.encodeHexString
                                                                      at com.mengfly.todo.utils.en_de_code.impl.EncodeAES.endcodeString(EncodeAES.java:27)
                                                                      at com.mengfly.todo.utils.file.APPFileManager.saveItemDataFile(APPFileManager.java:60)
                                                                      at com.mengfly.todo.presenter.MainPresenter$2.run(MainPresenter.java:68)
```
为什么会找不到Method?我在它之前的方法里面使用这个包的md5加密的算法没有问题,使用Hex.decodeHex也没有问题,为什么偏偏就这个方法除了问题?要出问题也应该是都出问题才对啊,网上查了博客[ Android使用commons-codec-1.6 遇到的问题 ](http://blog.csdn.net/luoqintao/article/details/12019263)才知道原来是android内部库也有一个org.apache.commons.codecs.*的 jar，它里面没有提供encodeHexString这个方法,但是加载类的时候又是默认先加载他里面的类,所以就会出错.因此一个解决方法就是修改commons.codecs的源码.修改一下包名.
下面是步骤:
