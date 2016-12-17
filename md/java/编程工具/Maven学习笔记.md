## Maven学习笔记

Maven 可以帮助我们管理项目，管理项目所依赖的第三方插件

### Maven 下载地址
http://maven.apache.org/

### 环境搭建
#### 配置环境变量
**M2_HOME**:配置Maven的安装目录
在Path中配置：%M2_HOME%\bin
mvn -v	: 查看Maven版本

### Maven的目录结构
src
  --main
    --java
      --package
  --test
    --java
      --package
  --resources

### Maven命令
- mvn compile 	: 对项目进行编译
- mvn package 	: 对项目进行打包
- mvn test	: 用来测试
- mvn clean	: 删除target
- mvn install	: 安装项目到本地仓库

### MVN自动构建项目骨架
archetype插件
用于创建符合maven规定的目录骨架
使用命令 mvn archetype:generate
使用命令 mvn archetype:generate -DarchetypeCatalog=internal 让它不要从远程服务器上取catalog:
之后会依次提示输入groupId(一般是公司网址反写+项目名),artifacId(项目名-模块名),version(版本号), package(项目所在的包名).  

### 更改本地仓库的地址
Settings.xml --> localRepository

