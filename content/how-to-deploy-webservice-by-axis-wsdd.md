Title: 如何用axis的wsdd方法部署WebService
Date: 2015-08-05 15:36
Modified: 2015-08-05 15:36
Category: it
Tags: java, webservice, axis, wsdd
Slug: how-to-deploy-webservice-by-axis-wsdd
Author: caimaoy


## 编写 deploy.wsdd 文件

- 放置于 %Tomcat_Home%\webapps\axis\WEB-INF 中
- 内容如下

```
<?xml version="1.0" encoding="UTF-8"?>
<deployment xmlns="http://xml.apache.org/axis/wsdd/"
    xmlns:java="http://xml.apache.org/axis/wsdd/providers/java">
    <service name="WSDD" provider="java:RPC">
        <parameter name="className" value="com.caimaoy" />
        <!-- * 代表所有的方法都暴露 -->
        <parameter name="allowedMethods" value="*" />
        <parameter name="scope" value="request" />
    </service>
</deployment>

```

- service标签代表一个WebService服务，HelloWorldWSDD就是当前WebService的名称
- provider是java的WebService类型，分别有： RPC、Document、Wrapped、Message、EJB、RMI
- 有兴趣的可以看看org.apache.axis.providers.java包下面的WebService的实现类或是文档
- parameter的参数className代表当前WebService的class类路径
- allowedMethods代表暴露的方法，那些方法在客户端可以调用；
- <parameter name="scope" value="request" />
- 这个是当前WebService的作用域，它有3个值，分别是：request、session、application
- request代表为每个WebService SOAP的请求都产生一个服务对象，和Spring的scope很像，在服务请求频繁的话会消耗很多资源
- session 是给每个调用当前WebService的客户端创建一个服务对象
- application 是个当前所有的请求创建一个服务对象


## 发布 WebService
- 写完配置后，就需要用axis提供的AdminClient工具类帮我们发布WebService，直到生成server-config.wsdd
- 步骤如下:
- 启动Tomcat
- 运行cmd命令，然后进入当前工程发布的目录，即%tomcat_home%/webapps/project/WEB-INF


- 输入命令
```
java -Djava.ext.dirs=lib org.apache.axis.client.AdminClient deploy.wsdd
java -Djava.ext.dirs=lib org.apache.axis.client.AdminClient -p 8082 -s /axis/servlet/AxisServlet deploy.wsdd
```
- -p 表示端口Tomcat端口号，AdminClient 默认为__8080__
- 这里的deploy.wsdd是我们刚才定制的wsdd文件，java当然是jvm的命令
- -Djava.ext.dirs=lib设置当前命令的依赖包
- AdminClient是axis提供的工具类，这个类本来是可以在官方的工程中admin可以直接运行的（这里不可以，下载下来的少了AdminServlet，有兴趣的可以研究下，就是前面说的官方的示例）；

如果运行命令后，看到：

```
Processing file deploy.wsdd
<Admin>Done processing</Admin>
```

- 就代表快成功了，why？快！看看deploy.wsdd同级目录有没有生成server-config.wsdd如果有这个文件就成功了，没有就失败了
- 如果失败了还有解决办法，首先你得启动tomcat，将我们的工程发布出去。然后在重复上面的命令，不行就换命令行代码如下：

```
java -Djava.ext.dirs=lib org.apache.axis.client.AdminClient -lhttp://localhost:8080/AxisWebService/services/AdminService deploy.wsdd
```

- -lhttp://localhost:8080/AxisWebService/services/AdminService是因为你的端口可能被axis占用了，我们将指定AdminService来完成转换，运行上面命令就没有问题了。

## WebService 客户端

- 我这里只说一种客户端的实现方法，在网上看了好像有超过6种以上的方法
- 大概的代码如下：

```
import org.apache.axis.client.Call;
import org.apache.axis.client.Service;
import javax.xml.namespace.QName;

public class TestClient {
    public static void main(String [] args) {
    try {
        String endpoint = "http://caimaoy.com/axis/services/WSDD?wsdl=1&test=test";

        Service  service = new Service();
        Call  call  = (Call) service.createCall();

        call.setTargetEndpointAddress(new java.net.URL(endpoint) );
        call.setOperationName(new QName("http://soapinterop.org/", "querySingle"));

        String ret = (String) call.invoke(new Object[] { "Hello!" } );

        System.out.println("got:" + ret);
    } catch (Exception e) {
    System.err.println(e.toString());
    }
}
}
```

## FAQ

- 提问：如果我出现了 java.lang.reflect.InvocationTargetException 这样的异常如何处理？
- 回答：这是映射出错，我遇到的情况是在 %Tomcat_Home%\webapps\axis\WEB-INF 中添加缺失是jar包

- 提问：作为一个WebService能够获取到客户端的IP、请求的requestString吗？
- 回答：可以大概的获取方式如下,获取到了 HttpServletRequest requsest,也就有了想要的东西了

```
import javax.servlet.http.HttpServletRequest;

import org.apache.axis.MessageContext;
import org.apache.axis.transport.http.HTTPConstants;

public class HelloWorld {

    public String getClientInfo(String asYouLike) {

    	/* get HttpRequest*/
    	MessageContext mc = null;
        HttpServletRequest request = null;
        try {
            //mc = MessageContext.getCurrentMessageContext();
            mc = MessageContext.getCurrentContext();
            if (mc == null)
                throw new Exception("无法获取到MessageContext");
            request = (HttpServletRequest) mc.getProperty(HTTPConstants.MC_HTTP_SERVLETREQUEST);
            System.out.println("remote  ip:  " + request.getRemoteAddr());
            System.out.println("request URI:  " + request.getRequestURI());
            System.out.println("quesryString :  " + request.getQueryString());

        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
}
```
