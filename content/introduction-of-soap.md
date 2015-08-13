Title: Introduction of SOAP
Date: 2015-08-13 10:14
Modified: 2015-08-13 10:14
Category: it
Tags: soap webservice
Slug: introduction-of-soap
Author: caimaoy


###SOAP

- 这里说的SOAP不是肥皂，和捡肥皂也没有关系
- 先来看一下官方介绍,以下内容来自[wiki](https://zh.wikipedia.org/wiki/SOAP)


```
SOAP（原为Simple Object Access Protocol的首字母缩写，即简单对象访问协议）是交换数据的一种协议规范，使用在计算机网络Web服务（web service）中，交换带结构信息。SOAP为了简化网页服务器（Web Server）从XML数据库中提取数据时，节省去格式化页面时间，以及不同应用程序之间按照HTTP通信协议，遵从XML格式执行资料互换，使其抽象于语言实现、平台和硬件。此标准由IBM、Microsoft、UserLand和DevelopMentor在1998年共同提出，并得到IBM，莲花（Lotus），康柏（Compaq）等公司的支持，于2000年提交给万维网联盟（World Wide Web Consortium；W3C），目前SOAP 1.1版是业界共同的标准，属于第二代的XML协定（第一代具主要代表性的技术为XML-RPC以及WDDX）。

用一个简单的例子来说明SOAP使用过程，一个SOAP消息可以发送到一个具有Web Service功能的Web站点，例如，一个含有房价信息的数据库，消息的参数中标明这是一个查询消息，此站点将返回一个XML格式的信息，其中包含了查询结果（价格，位置，特点，或者其他信息）。由于数据是用一种标准化的可分析的结构来传递的，所以可以直接被第三方站点所利用。

```

- 上面的话翻译一下，就是SOAP 是基于 XML 的简易协议，可使应用程序在 HTTP 之上进行信息交换。
- 或者更简单地说：SOAP 是用于访问网络服务的协议。
- 还是不够清晰？ 看看实例吧
- 在下面的例子中，一个 GetStockPrice 请求被发送到了服务器。此请求有一个 StockName 参数，而在响应中则会返回一个 Price 参数。此功能的命名空间被定义在此地址中： "http://www.example.org/stock"

####SOAP 请求:

```
POST /InStock HTTP/1.1
Host: www.example.org
Content-Type: application/soap+xml; charset=utf-8
Content-Length: nnn

<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

  <soap:Body xmlns:m="http://www.example.org/stock">
    <m:GetStockPrice>
      <m:StockName>IBM</m:StockName>
    </m:GetStockPrice>
  </soap:Body>

</soap:Envelope>
```

####SOAP 响应：

```
HTTP/1.1 200 OK
Content-Type: application/soap+xml; charset=utf-8
Content-Length: nnn

<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

  <soap:Body xmlns:m="http://www.example.org/stock">
    <m:GetStockPriceResponse>
      <m:Price>34.5</m:Price>
    </m:GetStockPriceResponse>
  </soap:Body>

</soap:Envelope>
```

### 各种问题

- 现在问题来了，SOAP只是一个传输协议
- 那我们传输什么？
- 给谁传输？
- 为什么要这样传输？


### Web Service

- 要解答问题就要先了解[Web服务](https://zh.wikipedia.org/wiki/Web%E6%9C%8D%E5%8A%A1)

```
Web服务是一种服务导向架构的技术，通过标准的Web协议提供服务，目的是保证不同平台的应用服务可以互操作。

根据W3C的定义，Web服务（Web service）应当是一个软件系统，用以支持网络间不同机器的互动操作。网络服务通常是许多应用程序接口（API）所组成的，它们透过网络，例如国际互联网（Internet）的远程服务器端，执行客户所提交服务的请求。

尽管W3C的定义涵盖诸多相异且无法介分的系统，不过通常我们指有关于主从式架构（Client-server）之间根据SOAP协议进行传递XML格式消息。无论定义还是实现，WEB服务过程中会由服务器提供一个机器可读的描述（通常基于WSDL）以辨识服务器所提供的WEB服务。另外，虽然WSDL不是SOAP服务端点的必要条件，但目前基于Java的主流WEB服务开发框架往往需要WSDL实现客户端的源代码生成。一些工业标准化组织，比如WS-I，就在WEB服务定义中强制包含SOAP和WSDL。
```

- 提问：我们为什么要用web服务？
- 回答：Webservice的一个最基本的目的就是提供在各个不同平台的不同应用系统的协同工作能力
- 我肤浅的认为WebService有以下几个好处：
    - 计算处理压力放在服务端
    - 计算处理过程在服务端，更新升级，影响面小
    - 调用同语言无关

- 提问：我们为什么不用基于URI的方式来请求Web服务？
- 回答：基于URI的方式的确是一种方法，是Web Service 的另一种解决方案：REST，这里不详细说明了
- 基于SOAP传输，是考虑到数据类型多样化和服务器解析压力小两个原因

### WSDL

- 好像还是有问题
- 提问：我如何去哪请求服务？请求参数是什么啊？
- 回答：WSDL 是 Web Services Description Language 的所写，也就是 Web 服务的描述
- 简单的说它描述了你向哪个地址和端口发送消息、请求消息格式、接收消息格式等信息
- 客户端有了这些信息就可以像调用一个本地函数一样调用一个Web Service
- 下面为python调用web Service的一种方法：

```
from suds.client import Client
test=Client('http://localhost:7789/SOAP/?wsdl')
print test.service.addition(1,2)
```
