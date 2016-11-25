# java密码之Base64

[TOC]

## 安全和密码
### 密码常用术语
> 明文，密文，加密，加密算法，加密密钥，解密，解密算法，解密密钥，密码分析，主动攻击，被动攻击，密码体制，密码协议，密码系统，柯克霍夫原则（对密钥保密，对算法公开）


## 密码分类以及java的安全组成
### 根据时间分类
+ **古典密码**：以字符为基本加密单元**
非对称密码算法**
+ **现代密码**：以信息块为基本加密单元

### 根据保密内容：
+ **受限制算法**（军事领域，算法保密，类别：古典密码）
+ **基于密钥的算法**（算法公开，密钥保密，类别：现代密码）

### 根据密码体制：
+ **对称密码**：单钥密码或私钥密码（加密密钥和解密密钥相同）
+ **非对称密码**：双密钥密码或公钥密码（加密密钥和解密密钥不同，密钥分为公钥和私钥）

**对称密码算法**
**非对称密码算法**

### 根据明文处理方法：
+ **分组密码**：对明文分组分别进行加密，多用于网络加密
+ **流密码**：也称序列密码，指加密时每次加密一位或者一个字节明文

### 散列函数（验证数据的完整度）
+ **特点**：
 长度不受限制
 哈希值容易计算
 散列运算过程不可逆

+ **相关算法**：
 MD5（消息摘要算法）
 SHA（安全散列算法）
 MAC（消息认证算法）

### 数字签名（针对以数字形式存储的消息进行的处理）

### OSI安全体系
+ **网络通信**：
	物理层--> 数据链路层 --> 网络层 --> 传输层 --> 会话层 --> 表示层 --> 应用层

+ **安全机制**：
	加密机制、数字签名机制、访问控制机制、数据完整性机制、认证机制、业务流填充机制、路由控制机制、公证机制。

+ **安全服务**：
	认证（鉴别），访问控制服务（防止非法访问），数据保密性服务（确保数据安全有效），数据完整性服务（保证数据不被篡改），抗否认行服务。

### TCP/IP安全体系
 网络接口层、网络层、传输层、应用层。

### Java的安全组成
 + **JCA**（java加密体系结构，提供基本的加密框架）
 + **JCE**(java加密扩展包)
 + **JSSE**（java套接字的扩展包，基于SSL的加密功能，只要用在网络传输中）
 + **JAAS**（java鉴别于安全服务，用户身份的验证功能）

### JDK相关包及第三方扩展
+ **相关的包、类**
    **java.security**(消息摘要)
    **javax.crypto**(安全消息摘要，消息认证（鉴别），码)
    **java.net.ssl**(安全套接字)

+ **第三方java扩展**
	- **Bouncy Castle**
		两种支持方式：
        1）.配置（配置文件位置：%JAVA_HONE%/jre/lib/security/java.security文件）
        2）调用，在代码中通过addProvider函数进行设置

    - **Commons Codec**
		- Apache
		- Base64、二进制、十六进制、字符集编码
		- Url编码/解码


### Base64算法介绍
> 基于64个字符的编码算法

+ **算法实现**
	+ jdk
	+ commons codec
	+ bouncy castle

+ **应用场景**：
	+ e-mail
	+ 密钥
	+ 证书文件


## 例子
### 要进行加密的字符串

```java
String src = "I'm Learing Base64";
```

### jdk:
```java
/**
	 * 通过jdk实现base64加密
	 * import sun.misc.BASE64Decoder;
	 */
void jdkBase64() {
	// 进行编码
	BASE64Encoder encoder = new BASE64Encoder();
	String encodeStr = encoder.encode(src.getBytes());
	System.out.println("encodeStr:" + encodeStr);
	// 进行解码
	String decodeStr = null;
	BASE64Decoder decoder = new BASE64Decoder();
	try {
		decodeStr = new String(decoder.decodeBuffer(encodeStr));
	} catch (IOException e) {
		e.printStackTrace();
	}
	System.out.println("decodeStr:" + decodeStr);
}

```
### commonsCodec:

```java
/**
 * 使用CommonsCodec进行加密
 * import org.apache.commons.codec.binary.Base64;
 */
public static void commonsCodecBase64() {
    //进行加密
    byte[] encodeBytes = Base64.encodeBase64(src.getBytes());
    System.out.println("encodeBytes:" + new String(encodeBytes));
    byte[] decodeBytes = Base64.decodeBase64(encodeBytes);
    System.out.println("decodeBytes:" + new String(decodeBytes));
}
```

### bouncyCastle:
```java
/**
 * 使用bouncyCastleBase64进行加密和解密
 */
public static void bouncyCastleBase64() {
    byte[] encodeBytes = org.bouncycastle.util.encoders.Base64.encode(src.getBytes());
    System.out.println("encodeStr:" + new String(encodeBytes));

    byte[] decodeBytes = org.bouncycastle.util.encoders.Base64.decode(encodeBytes);
    System.out.println("decodeStr:" + new String(decodeBytes));
}
```
