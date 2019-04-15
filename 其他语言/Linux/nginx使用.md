# Nginx使用

> 以CentOS7为例

## 1. 安装Nginx

```bash
yum install nginx
```

## 2. Nginx 安装目录

默认的安装目录是 **ect/nginx** 

## 3. 配置Nginx

nginx的配置文件为 **nginx.conf** 修改这个文件进行nginx的配置

下面是服务器上面的某项设置：

server中表示一个代理。

**listen：** 表示监听哪一个端口

**location：** 表示在监听路径上面的某一类路径的映射

+ **proxy_pass：** 表示映射到某一个URL上面
+ **alias：** 表示映射到某个文件目录

```conf
server {
        listen       50210 default_server;
        listen       [::]:50210 default_server;
        server_name  _;
        root         /html/mxjj;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
        }

		location /api/ {
			proxy_pass http://localhost:82;
		}

		location /image/ {
			alias /html/mxjj/upload/;
		}

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
```

## 4. 启动Nginx

```bash
systemctl start nginx.service
```

## 5.  重启Nginx

```bash
systemctl restart nginx.service
```

## 6. 注意事项

+ 在配置文件夹的时候，最好不要把文件夹防止在 **/root** 文件夹下面，因为这样很可能会导致 **403** 错误
+ alias 后面的路径必须以 **/** 结尾
