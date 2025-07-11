好的，这是您要求的完整、准确、保留 Markdown 格式的中文翻译。

# 常见的自然语言处理任务和技术

对于大多数*自然语言处理*任务，必须对要处理的文本进行分解、检查，并将结果存储起来或与规则和数据集进行交叉引用。这些任务使得程序员能够推断出文本中术语和单词的_含义_、_意图_，或者仅仅是它们的_频率_。

## [课前测验](https://gray-sand-07a10f403.1.azurestaticapps.net/quiz/33/)

让我们来探索处理文本时使用的常用技术。将这些技术与机器学习相结合，可以帮助你高效地分析大量文本。然而，在将机器学习应用于这些任务之前，让我们先了解一下自然语言处理（NLP）专家会遇到的问题。

## NLP 的常见任务

分析你正在处理的文本有多种不同的方法。你可以执行一些任务，通过这些任务，你能够对文本获得理解并得出结论。你通常会按顺序执行这些任务。

### 分词 (Tokenization)

可能大多数 NLP 算法要做的第一件事就是将文本分割成词元（token）或单词。虽然这听起来很简单，但考虑到标点符号以及不同语言的单词和句子分隔符，这项任务可能会变得棘手。你可能需要使用各种方法来确定分界。

![分词](images/tokenization.png)
> 对《傲慢与偏见》中的一个句子进行分词。信息图由 [Jen Looper](https://twitter.com/jenlooper) 制作。

### 词嵌入 (Embeddings)

[词嵌入](https://zh.wikipedia.org/wiki/词嵌入) 是一种将文本数据数值化的方法。词嵌入的实现方式使得含义相似或经常一起使用的词语会聚集在一起。

![词嵌入](images/embedding.png)
> “我非常敬重你的神经，它们是我的老朋友了。”——《傲慢与偏见》中一个句子的词嵌入。信息图由 [Jen Looper](https://twitter.com/jenlooper) 制作。

✅ 试试[这个有趣的工具](https://projector.tensorflow.org/)来体验词嵌入。点击一个词会显示出相似词的聚类：“toy”（玩具）与“disney”（迪士尼）、“lego”（乐高）、“playstation”（游戏机）和“console”（游戏机）聚集在一起。

### 解析与词性标注 (Parsing & Part-of-speech Tagging)

每个被分词的单词都可以被标注词性——名词、动词或形容词。句子 `the quick red fox jumped over the lazy brown dog`（敏捷的红狐狸跳过了懒惰的棕狗）可能会被进行如下词性标注（POS tagging）：fox = 名词，jumped = 动词。

![解析](images/parse.png)

> 对《傲慢与偏见》中的一个句子进行解析。信息图由 [Jen Looper](https://twitter.com/jenlooper) 制作。

解析（Parsing）是识别句子中哪些词相互关联——例如，`the quick red fox jumped` 是一个形容词-名词-动词序列，与 `lazy brown dog` 序列是分开的。

### 词和短语频率 (Word and Phrase Frequencies)

在分析大量文本时，一个有用的程序是构建一个包含所有感兴趣的词或短语及其出现频率的字典。短语 `the quick red fox jumped over the lazy brown dog` 中单词 `the` 的词频为 2。

让我们看一个计算词频的示例文本。Rudyard Kipling 的诗歌《The Winners》包含以下诗节：

```output
What the moral? Who rides may read.
When the night is thick and the tracks are blind
A friend at a pinch is a friend, indeed,
But a fool to wait for the laggard behind.
Down to Gehenna or up to the Throne,
He travels the fastest who travels alone.
```

由于短语频率可以根据需要区分或不区分大小写，短语 `a friend` 的频率为 2，`the` 的频率为 6，`travels` 的频率为 2。

### N-gram

文本可以被分割成设定长度的单词序列，单个词（unigram，一元语法）、两个词（bigram，二元语法）、三个词（trigram，三元语法）或任意数量的词（n-gram）。

例如，对于句子 `the quick red fox jumped over the lazy brown dog`，使用 n-gram 值为 2 会产生以下 n-gram：

1. the quick
2. quick red
3. red fox
4. fox jumped
5. jumped over
6. over the
7. the lazy
8. lazy brown
9. brown dog

将其想象成一个在句子上滑动的窗口可能更容易理解。以下是 n-gram 值为 3 的情况，n-gram 在每个句子中以粗体显示：

1.  <u>**the quick red**</u> fox jumped over the lazy brown dog
2.  the <u>**quick red fox**</u> jumped over the lazy brown dog
3.  the quick <u>**red fox jumped**</u> over the lazy brown dog
4.  the quick red <u>**fox jumped over**</u> the lazy brown dog
5.  the quick red fox <u>**jumped over the**</u> lazy brown dog
6.  the quick red fox jumped <u>**over the lazy**</u> brown dog
7.  the quick red fox jumped over <u>**the lazy brown**</u> dog
8.  the quick red fox jumped over the <u>**lazy brown dog**</u>

![n-gram 滑动窗口](images/n-grams.gif)

> N-gram 值为 3：信息图由 [Jen Looper](https://twitter.com/jenlooper) 制作。

### 名词短语提取 (Noun phrase Extraction)

在大多数句子中，都有一个作为主语或宾语的名词。在英语中，它通常可以通过前面有 'a'、'an' 或 'the' 来识别。在尝试理解句子含义时，通过“提取名词短语”来识别句子的主语或宾语是 NLP 中的一项常见任务。

✅ 在句子 "I cannot fix on the hour, or the spot, or the look or the words, which laid the foundation. It is too long ago. I was in the middle before I knew that I had begun."（我无法确定是哪个时辰，在哪个地点，是哪种容貌，是哪些言语，才奠定了基础。那太久远了。我竟是在不知不觉中陷入其中的。）中，你能找出名词短语吗？

在句子 `the quick red fox jumped over the lazy brown dog` 中，有两个名词短语：**quick red fox** 和 **lazy brown dog**。

### 情感分析 (Sentiment analysis)

可以对一个句子或文本进行情感分析，即分析它是多么*积极*或*消极*。情感通过*极性*（polarity）和*客观性/主观性*（objectivity/subjectivity）来衡量。极性的衡量范围是从 -1.0 到 1.0（消极到积极），客观性/主观性的衡量范围是从 0.0 到 1.0（最客观到最主观）。

✅ 稍后你将学习到，有多种使用机器学习来确定情感的方法，但其中一种方法是，拥有一个由人类专家分类为积极或消极的单词和短语列表，然后将该模型应用于文本以计算极性得分。你能看出为什么这种方法在某些情况下有效，而在其他情况下效果不佳吗？

### 词形变化 (Inflection)

词形变化（Inflection）使你能够根据一个词得到其单数或复数形式。

### 词形还原 (Lemmatization)

*词元*（lemma）是一组词的词根或中心词，例如，*flew*、*flies*、*flying* 的词元是动词 *fly*。

对于 NLP 研究者来说，还有一些有用的数据库可用，特别是：

### WordNet

[WordNet](https://wordnet.princeton.edu/) 是一个包含多种语言中每个词的词语、同义词、反义词和许多其他细节的数据库。在尝试构建翻译器、拼写检查器或任何类型的语言工具时，它都非常有用。

## NLP 库

幸运的是，你不必自己构建所有这些技术，因为有优秀的 Python 库可用，这使得非自然语言处理或机器学习专业的开发人员也更容易上手。接下来的课程将包含更多相关示例，但这里你将学习一些有用的例子来帮助你完成下一个任务。

### 练习 - 使用 `TextBlob` 库

让我们使用一个名为 TextBlob 的库，因为它包含了用于处理这类任务的实用 API。TextBlob “站在 [NLTK](https://nltk.org) 和 [pattern](https://github.com/clips/pattern) 这两个巨人的肩膀上，并且与两者都能很好地配合。” 它在其 API 中嵌入了大量的机器学习功能。

> 注意：对于有经验的 Python 开发者，推荐阅读 TextBlob 的 [快速入门](https://textblob.readthedocs.io/en/dev/quickstart.html#quickstart) 指南。

在尝试识别*名词短语*时，TextBlob 提供了多种提取器选项来查找名词短语。

1. 看一下 `ConllExtractor`。

    ```python
    from textblob import TextBlob
    from textblob.np_extractors import ConllExtractor
    # 导入并创建一个 Conll 提取器以备后用
    extractor = ConllExtractor()
    
    # 稍后当你需要一个名词短语提取器时：
    user_input = input("> ")
    user_input_blob = TextBlob(user_input, np_extractor=extractor)  # 注意指定了非默认的提取器
    np = user_input_blob.noun_phrases                                    
    ```

    > 这是怎么回事？[ConllExtractor](https://textblob.readthedocs.io/en/dev/api_reference.html?highlight=Conll#textblob.en.np_extractors.ConllExtractor) 是“一个使用 ConLL-2000 训练语料库训练的语块分析（chunk parsing）来进行名词短语提取的提取器。” ConLL-2000 指的是 2000 年的计算自然语言学习会议（Conference on Computational Natural Language Learning）。每年该会议都会举办一个研讨会来解决一个棘手的 NLP 问题，2000 年的主题是名词短语切分（noun chunking）。一个模型在《华尔街日报》语料上进行了训练，使用“第 15-18 节作为训练数据（211727 个词元），第 20 节作为测试数据（47377 个词元）”。你可以在[这里](https://www.clips.uantwerpen.be/conll2000/chunking/)查看所使用的程序，并在[这里](https://ifarm.nl/erikt/research/np-chunking.html)查看结果。

### 挑战 - 用 NLP 改进你的机器人

在上一课中，你构建了一个非常简单的问答机器人。现在，你将通过分析你的输入情感并打印出匹配情感的响应，让马文（Marvin）变得更有同情心一点。你还需要识别一个`名词短语`（noun_phrase）并就此提问。

构建一个更好的对话机器人的步骤：

1. 打印说明，告知用户如何与机器人互动
2. 开始循环
   1. 接受用户输入
   2. 如果用户要求退出，则退出
   3. 处理用户输入并确定适当的情感响应
   4. 如果在情感分析的文本中检测到名词短语，将其变为复数形式，并就该主题请求更多输入
   5. 打印响应
3. 回到第 2 步

以下是使用 TextBlob 确定情感的代码片段。请注意，这里只有四种情感响应的*梯度*（如果你愿意，可以有更多）：

```python
if user_input_blob.polarity <= -0.5:
  response = "天哪，这听起来很糟糕。"
elif user_input_blob.polarity <= 0:
  response = "嗯，那不太好。"
elif user_input_blob.polarity <= 0.5:
  response = "嗯，听起来很积极。"
elif user_input_blob.polarity <= 1:
  response = "哇，听起来太棒了。"```

这里有一些示例输出来指导你（用户输入位于以 > 开头的行）：

```output
你好，我是友好的机器人马文。
你可以随时输入'bye'来结束这次对话。
每次输入回答后，请按'enter'键。
你今天怎么样？
> 我还行
嗯，听起来很积极。能多告诉我一些吗？
> 我去散步了，看到了一只可爱的猫
嗯，听起来很积极。能多告诉我一些关于可爱的猫们(lovely cats)的事吗？
> 猫是最棒的。但我也有一只很酷的狗
哇，听起来太棒了。能多告诉我一些关于很酷的狗们(cool dogs)的事吗？
> 我有一只老猎犬，但它生病了
嗯，那不太好。能多告诉我一些关于老猎犬们(old hounddogs)的事吗？
> bye
很高兴和你聊天，再见！
```

该任务的一个可能解决方案在[这里](https://github.com/microsoft/ML-For-Beginners/blob/main/6-NLP/2-Tasks/solution/bot.py)。

✅ 知识检验

1. 你认为这种富有同情心的回应会“欺骗”某人，让他们以为机器人真的理解他们吗？
2. 识别名词短语是否让机器人更“可信”？
3. 为什么从句子中提取“名词短语”是一件有用的事？

---

实现上一个知识检验中的机器人，并在朋友身上测试它。它能骗过他们吗？你能让你的机器人更“可信”吗？

## 🚀挑战

选择上一个知识检验中的一个任务并尝试实现它。在朋友身上测试这个机器人。它能骗过他们吗？你能让你的机器人更“可信”吗？

## [课后测验](https://gray-sand-07a10f403.1.azurestaticapps.net/quiz/34/)

## 复习与自学

在接下来的几节课中，你将学习更多关于情感分析的知识。通过阅读 [KDNuggets](https://www.kdnuggets.com/tag/nlp) 等网站上的文章来研究这项有趣的技术。

## 作业

[让机器人回话](assignment.md)