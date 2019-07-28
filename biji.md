# 学习笔记

## 学习python相关知识

### 查看长度函数 len
* len函数可以查看 字符串、列表、字典、元组、集合长度



### 关键字 in
* "a" in "abcdefg"
* 1 in [1,2,3,4,5]
* "name" in {"name":"wangzhaorui","age":22}


### 数据类型  2
1. 列表 "list"

* 增、查、改、删

* 表示方法 [element1, element2, element3...]，有序的排列
* 通过index 访问其中的元素  list[index]
* 从左往右：index 从0开始，最大索引为 len（list）-1
* 从右往左：index 从-1开始，最小索引为 -len（list）
* append函数插入一个元素到list中。list.append(element)   (插入的元素在list中元素的末尾)
* pop 函数删除指定索引的元素。list.pop(i) ，默认删除末尾的元素 也就是删除list.pop(-1)
* 多维list
* 更新指定索引对应的值 list[index]=newValue

* 练习任务：新建一个100个相同元素的列表
```
a=['123']*100
print(a)
```
```
print([1]*100)
```


2. 字典"dict"
* 由键值对构成的 {key1:value1,key2:value2} ,,key是唯一的

* 查询指定key的value，dic[key] 或者是dict.get(key)

* 增加一对键值对，直接赋值dict[newKey]=newValue

* 修改指定key的value，赋值dict[key]=newValue

* pop函数删除一对键值对。dict.pop(key)




3. 元组 "tuple"

* 查看

* 元组：(element1,element2,element3)，一旦初始化之后就不可再更改,那就没有新增或删除，只能查看



4. 集合 "set"
* set() 元素是不会重复的，和数学中的集合概念很类似

* 作用1：去除一个list 里面的重复元素
```
set_a=set(list_c)
list_c=list(set_a)

list_c=list(set(list_c))
```

* 差集、并集、交集：对比两个list中的相同元素和不同元素。.difference、.union、.intersection。（A与B的差集是A-A交B,B与A的差集是B-A交B）


### 条件语句

```
if conditon：
    xxxx
else:
    xxxx

if condition:
    xxxx
else if:
    xxxx
...
else:
    xxxx
```

* 请用户输入一个成绩，判断优秀、良好、一般、不及格。90以上优秀、80-99良好、60-79一般、低于60不及格

```
a=float(input("请用户输入一个成绩："))
if a>=90:
    print("优秀")
elif (90>a>=80):
    print("良好")
elif (80>a>=60):
    print("一般")
else :
    print("不及格")
```

### 任务
1. 输入三条边的长度如果能构成三角形就计算周长和面积
2. 用户身份验证输入用户名和密码，管理员、用户、超级用户。
已知管理员身份有以下：方开-123、刘晨-12345。
用户：张旭-123321、沈章-123456、许景-123456
访客：其他（字母或者中文构成的用户名）-guset



## 学习web相关知识

### JavaScript

1. JavaScript和Java没有直接的关系，JavaScript吸收了一些Java的特性，简称js。

2. JavaScript是解释型语言，无需编译就可以随时运行，哪怕是部分语法书写有误，也照样运行，但是可能会得不到想要的结果，没有语法错误的还能正常运行。

### JS入门
1. 
```
<script type=”text/javascript”
        alert(new Data().toLocaleDateString());
</script>
```
2. 
```
 JavaScript代码放在<script> 标签中，script 可以放到<head>、<body>等任意位置，而且可以有不止一个<script>标签。alert函数是弹出消息窗口，new Date()是创建一个Date类的对象，默认值就是当前时间。
 ```

3.
```
 除了可以在页面中声明js外，还可以将JavaScript写到单独的js文件中，然后再页面中引入：<script src=“test.js” type=“text/javascript”></script>。声明到单独的js文件可以和其他页面共享、并且减小网络流量
 ```


### JS变量

1. JS中可以使用双引号声明字符串，也可以使用单引号声明字符串。主要是为了方便和html集成，避免转义符的麻烦
JS是弱类型，声明变量的时候不能使用 int i=0; 只能通过var i=0; 

2. Js中也可以不用var来声明变量，直接用，这样的变量就是全局变量，如非特殊需要，尽量先声明

3. Js是动态类型的，所以var i=0; i=“abc”;是合法的


### 函数声明

1. JS中函数声明的方式：
```
      function add(i1,i2){
	      return i1+i2；
               }
```

2. 不需要声明返回值类型、参数类型。函数定义以function开头
```
 	var r=add(1,2);
	alert(r);
	r=add(“你好”，”tom”);
	alert(r); 
```

3. Js中不像其他语言中那样要求所有路径都有返回值，没有返回值就是undefined


### Js面向对象基础

* JS中没有类的语法，都是用函数闭包模拟出来的，下面讲解的时候使用C#中的类、构造函数的概念，js中String、date等“类”都叫做“对象”

```
function Person(name,age){
    this.name=name;
    this.age=age;
    this.SayHello=function(){
	alert(“你好，我是”+this.name+”，我”+this.age+”岁了”)；
        }
    }
var p1=new Pweson(“tom”,20);
p1.SayHello();
```
必须要声明类名，function Person(name,age)可以看做是声明构造函数


```web
<html>
<head>
   此处放css和js，有title标题
   <style type="text/css">
   
   </style>
   <script type="text/javascript">
   
   </script>
   
</head>
<body>
    <input type="button"  value="这是一个按钮"/>
	  <a href="https://www.baidu.com">这是一个百度超链接</a>
</body>
</html>
```



