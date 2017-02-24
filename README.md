## PyBaseQuiz1

---

本次测试有四道题:

- 熟悉 submit 的过程
- 矩阵的转置
- 实现 myTitle 函数
- 词频统计

---

### 熟悉 submit 的过程

首先,你需要在打开命令行,输入到这个目录:

    python register.py # 注册新的账号

输入你的邮箱,并且进入到你的邮箱确认你的邮箱地址.

当你下载了我们提供的作业文档时,通常会有以下文件:

- lib
	- ...
- config.json
- rawdata.bin
- solution.py
- submit.py
- register.py
- token.py
- ...

lib 文件夹里面的文件主要和 submit 的过程有关

config.json 是本次作业的描述,以及必需函数

rawdata.bin 是判定集

submit.py 负责提交你的作业结果

register.py 主要提供账号注册服务

以上文件不需要你修改,属于内置文件

你的作业,主要完成在 solution.py 下,按照文件的要求,完成相应的内容即可

这次我们来熟悉一下提交的环境,完成一个**加法函数**,将你的内容完成在 add 函数下之后进行 submit

每个函数下 return None 的意义在于提示判定器本函数未完成,你可以在以后的作业中使用 return None 的办法让判定器知道是否需要判定该函数.

在每次的上传结果中,我们只会取你的最新的提交结果,而不会选取提交中的最好结果.

### 矩阵的转置

本次作业我们将列表看做一个矩阵,来实现列表的转置.

设存在以下列表:

	>>> l = [
	...     [1,2,3,4],
	...     [2,3,4,5],
	...     [3,4,5,6]
	... ]
	...
	>>> transpose(l)
	[[1,2,3],[2,3,4],[3,4,5],[4,5,6]]
	>>> l = [

请实现这样的函数.

ps: 为了方便,假设输入的列表都是规范的有值的列表,不会出现类似以下的列表形式:

	[[1,2],[3]] # 不存在这样的矩阵
	
**hint**: 可以采用列表生成式,也可以使用 for...in... 

### 实现 myTitle 函数

在字符串中,存在 title 函数,该函数的作用是大写字符串中每一个单词的首字母,小写字符串中每一个单词的非首字母.

	>>> "MSC IS GREAT".title()
	"Msc Is Great"

但内置的 title 函数,只是严格的切分开单词,然后再依次大写化首字符小写化其余字符,这不符合实际,因为实际生活中,介词,冠词,部分简单的动词是不会大写的.[论文英文标题等的写法](https://www.douban.com/note/180259961/)

	>>> "myb is a great person".title()
	"Myb Is A Great Person"
	# 正确的格式应该是 "Myb is a Great Person"
	
请你实现一个这样的 myTitle 函数,补充这一缺点.我们已经把不需要首字母大写化的单词单独放到了 words.py 中的 wordList 中,wordList 是一个列表,其元素都是不需要首字母大写的单词.

为了方便,我们规定英文标题大写的原则.优先级从前到后.

- 首单词的首字母必须大写.
- 存在于 wordList 中单词的首字母不大写.
- 其余单词则要求首字母大写.

示例如下:

	>>> myTitle("a giant tree stands on my face")
	"A Giant Tree Stands on my Face"
	>>> myTitle("Python is a simple programing language")
	"Python is a Simple Programing Language"
	>>> myTitle("asdfasdf a on ertert") # 我随手乱按的...
	"Asdfasdf a on Ertert" 
	
**hint:**

	>>> "this is a test".split()
	['this', 'is', 'a', 'test']

**hint:**
	
可以按照下面所述引入 wordList.

	>>> from word import wordList
	# 或者
	>>> import word
	>>> wordList = word.wordList
	
### 词频统计

假设存在词频统计函数 frequencies,其可以统计英文字符串中单词的词频,

	>>> words = "one apple two android one windows one apple"
	>>> print frequencies(words)
	{"one":3,"apple":2,"two":1...}
	
**hint**:Python 的字典有一个方法:

	>>> d = dict()
	>>> d['foo'] = 10
	>>> d.get("foo",1) # foo 存在时,返回 d['foo']
	10
	>>> d.get("unexistKey",1) # unexistKey 不存在时,返回默认值
	1

于是对于词列表(词向量)

	>>> d = ['this','is','a','test']
	>>> result = dict()

我们可以遍历这个列表
	
	>>> time = d.get(word,0)
	>>> time += 1
	>>> d[word] = time

**hint**:建议使用 reduce 函数,也可直接使用 for...in...
