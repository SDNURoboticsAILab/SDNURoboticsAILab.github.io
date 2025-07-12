# 酒店评论的情感分析

既然你已经详细探索了数据集，现在是时候筛选列，然后在数据集上使用 NLP 技术来获取关于酒店的新见解了。
## [课前测验](https://gray-sand-07a10f403.1.azurestaticapps.net/quiz/39/)

### 筛选与情感分析操作

你可能已经注意到，这个数据集存在一些问题。有些列充斥着无用信息，有些列的数据似乎不正确。即使数据是正确的，其计算方式也不明确，而且无法通过自己的计算独立验证结果。

## 练习：更多的数据处理

对数据再做一些清理。添加后续会用到的列，修改其他列的值，彻底删除某些列。

1. 初始列处理

   1. 删除`lat`和`lng`列

   2. 将`Hotel_Address`（酒店地址）的值替换为以下值（如果地址包含城市和国家名称，将其简化为仅包含城市和国家）。

      数据集中只包含这些城市和国家：

      阿姆斯特丹，荷兰

      巴塞罗那，西班牙

      伦敦，英国

      米兰，意大利

      巴黎，法国

      维也纳，奥地利

   ```python
   def replace_address(row):
       if "Netherlands" in row["Hotel_Address"]:
           return "Amsterdam, Netherlands"
       elif "Barcelona" in row["Hotel_Address"]:
           return "Barcelona, Spain"
       elif "United Kingdom" in row["Hotel_Address"]:
           return "London, United Kingdom"
       elif "Milan" in row["Hotel_Address"]:        
           return "Milan, Italy"
       elif "France" in row["Hotel_Address"]:
           return "Paris, France"
       elif "Vienna" in row["Hotel_Address"]:
           return "Vienna, Austria" 
   
   # 将所有地址替换为更简短、更有用的形式
   df["Hotel_Address"] = df.apply(replace_address, axis = 1)
   #  value_counts()的总和应等于评论的总数
   print(df["Hotel_Address"].value_counts())
   ```

   现在你可以查询国家层面的数据：

   ```python
   display(df.groupby("Hotel_Address").agg({"Hotel_Name": "nunique"}))
   ```

   | 酒店地址         | 酒店数量 |
   | :--------------- | :------: |
   | 阿姆斯特丹，荷兰 |   105    |
   | 巴塞罗那，西班牙 |   211    |
   | 伦敦，英国       |   400    |
   | 米兰，意大利     |   162    |
   | 巴黎，法国       |   458    |
   | 维也纳，奥地利   |   158    |

2. 处理酒店元评论列

  3. 删除`Additional_Number_of_Scoring`（额外评分数量）

  4. 将`Total_Number_of_Reviews`（评论总数）替换为数据集中该酒店实际的评论总数

  5. 用我们自己计算的分数替换`Average_Score`（平均分数）


  ```python
  # Drop `Additional_Number_of_Scoring`
  df.drop(["Additional_Number_of_Scoring"], axis = 1, inplace=True)
  # Replace `Total_Number_of_Reviews` and `Average_Score` with our own calculated values
  df.Total_Number_of_Reviews = df.groupby('Hotel_Name').transform('count')
  df.Average_Score = round(df.groupby('Hotel_Name').Reviewer_Score.transform('mean'), 1)
  ```

3. 处理评论列

   1. 删除`Review_Total_Negative_Word_Counts`（评论负面词汇总数）、`Review_Total_Positive_Word_Counts`（评论正面词汇总数）、`Review_Date`（评论日期）和`days_since_review`（距评论天数）

   2. 保留`Reviewer_Score`（评论者评分）、`Negative_Review`（负面评论）和`Positive_Review`（正面评论）不变
   3. 暂时保留`Tags`（标签）

     - 下一节将对标签进行额外筛选操作，之后会删除标签列

4. 处理评论者列

  5. 删除`Total_Number_of_Reviews_Reviewer_Has_Given`（评论者给出的评论总数）

  6. 保留`Reviewer_Nationality`（评论者国籍）


### 标签列

`Tag`列存在问题，因为它是以文本形式存储在列中的列表。不幸的是，该列中子部分的顺序和数量并不固定。由于数据集中有 515,000 行记录、1427 家酒店，且每家酒店的评论者可选择的选项略有不同，人类很难识别出值得关注的正确短语。这正是自然语言处理（NLP）的优势所在 —— 可以扫描文本、找出最常见的短语并进行计数。

遗憾的是，我们感兴趣的不是单个词语，而是多词短语（例如 “商务旅行”）。在如此大量的数据（6,762,646 个词）上运行多词频率分布算法可能会耗费大量时间，但在未查看数据的情况下，这似乎是必要的步骤。而探索性数据分析在此处就发挥了作用：通过查看标签样本（如`[' 商务旅行 ', ' 独自旅行者 ', ' 单人间 ', ' 住了5晚 ', ' 从移动设备提交 ']`），你可以思考是否有可能大幅减少必须进行的处理工作。幸运的是，答案是肯定的 —— 但首先需要按步骤确定关注的标签。

### 筛选标签

请记住，该数据集的目标是添加情感信息和有助于选择最佳酒店的列（无论是为自己选择，还是为客户开发酒店推荐机器人）。你需要判断标签在最终数据集中是否有用。以下是一种分析视角（若数据集用于其他目的，筛选出的标签可能会不同）：

1. 旅行类型具有相关性，应保留
2. 客人群体类型很重要，应保留
3. 客人入住的房间、套房或公寓类型无关紧要（所有酒店的房间类型基本相同）
4. 提交评论的设备无关紧要
5. 评论者的入住天数*可能*相关（若认为入住时间越长表明客人越喜欢该酒店），但这种关联较为牵强，很可能无关紧要

总之，**保留两类标签，移除其他标签**。

首先，在标签格式优化前，我们不会对其进行计数，这意味着需要移除方括号和引号。有多种实现方式，但由于处理大量数据可能耗时较长，我们会选择最快的方式。幸运的是，pandas 提供了简便的方法来完成这些步骤。

```Python
# 移除开头和结尾的括号
df.Tags = df.Tags.str.strip("[']")
# 同时移除所有引号
df.Tags = df.Tags.str.replace(" ', '", ",", regex = False)
```

处理后，每个标签会变成类似这样的形式：`Business trip, Solo traveler, Single Room, Stayed 5 nights, Submitted from a mobile device`. 

接下来我们发现一个问题：部分评论（即行）有 5 个标签，有些有 3 个，还有些有 6 个。这是数据集创建方式导致的，难以修复。我们希望统计每个短语的出现频率，但由于它们在各评论中的顺序不同，计数可能不准确，且酒店可能会遗漏应有的标签。

不过，我们可以利用这种顺序差异 —— 因为每个标签都是多词短语，且用逗号分隔！最简单的方法是创建 6 个临时列，每个标签按其在原标签中的顺序对应存入列中。然后将这 6 个列合并为一个大列，并对结果列运行`value_counts()`方法。运行后会发现有 2428 个独特标签，以下是部分样本：

| 标签             | 计数   |
| ---------------- | ------ |
| 休闲旅行         | 417778 |
| 从移动设备提交   | 307640 |
| 情侣             | 252294 |
| 住了 1 晚        | 193645 |
| 住了 2 晚        | 133937 |
| 独自旅行者       | 108545 |
| 住了 3 晚        | 95821  |
| 商务旅行         | 82939  |
| 团体             | 65392  |
| 带幼儿的家庭     | 61015  |
| 住了 4 晚        | 47817  |
| 双人间           | 35207  |
| 标准双人间       | 32248  |
| 高级双人间       | 31393  |
| 带大孩子的家庭   | 26349  |
| 豪华双人间       | 24823  |
| 双人或双床间     | 22393  |
| 住了 5 晚        | 20845  |
| 标准双人或双床间 | 17483  |
| 经典双人间       | 16989  |
| 高级双人或双床间 | 13570  |
| 2 间房           | 12393  |

一些常见标签（如`从移动设备提交`）对我们无用，因此在统计短语出现次数前移除它们是明智的，但由于操作速度很快，也可以保留它们之后再忽略。

### 移除入住时长标签

第一步是移除这些标签，这会略微减少需考虑的标签总数。注意：并非从数据集中删除它们，只是在评论数据集中不将其作为计数 / 保留的值。

| 入住时长  | 计数   |
| --------- | ------ |
| 住了 1 晚 | 193645 |
| 住了 2 晚 | 133937 |
| 住了 3 晚 | 95821  |
| 住了 4 晚 | 47817  |
| 住了 5 晚 | 20845  |
| 住了 6 晚 | 9776   |
| 住了 7 晚 | 7399   |
| 住了 8 晚 | 2502   |
| 住了 9 晚 | 1293   |
| ...       | ...    |

数据集中有各种各样的房间、套房、公寓等类型，它们的含义大致相同且与我们的目标无关，因此也将其从考虑范围中移除。

| 房间类型         | 计数  |
| ---------------- | ----- |
| 双人间           | 35207 |
| 标准双人间       | 32248 |
| 高级双人间       | 31393 |
| 豪华双人间       | 24823 |
| 双人或双床间     | 22393 |
| 标准双人或双床间 | 17483 |
| 经典双人间       | 16989 |
| 高级双人或双床间 | 13570 |

最终，令人欣喜的是（因为几乎无需额外处理），我们会得到以下*有用的*标签：

| 标签                             | 计数   |
| -------------------------------- | ------ |
| 休闲旅行                         | 417778 |
| 情侣                             | 252294 |
| 独自旅行者                       | 108545 |
| 商务旅行                         | 82939  |
| 团体（与和朋友一起旅行的人合并） | 67535  |
| 带幼儿的家庭                     | 61015  |
| 带大孩子的家庭                   | 26349  |
| 带宠物                           | 1405   |

可以认为 “和朋友一起旅行的人” 与 “团体” 大致相同，因此将两者合并是合理的。识别正确标签的代码可参考[标签笔记本](https://github.com/microsoft/ML-For-Beginners/blob/main/6-NLP/5-Hotel-Reviews-2/solution/1-notebook.ipynb)。

最后一步是为每个有用标签创建新列。对于每条评论行，若`Tag`列包含某个新列对应的标签，则在该新列中填 1，否则填 0。最终结果将呈现出有多少评论者选择该酒店的原因（总体而言），例如商务出行还是休闲旅行，或是否带宠物等，这对酒店推荐非常有用。

```python
# 将标签处理为新列
# 文件Hotel_Reviews_Tags.py识别了最重要的标签
# 休闲旅行、情侣、独自旅行者、商务旅行、与朋友一起旅行的人合并后的团体、
# 带幼儿的家庭、带大孩子的家庭、带宠物
df["Leisure_trip"] = df.Tags.apply(lambda tag: 1 if "Leisure trip" in tag else 0)
df["Couple"] = df.Tags.apply(lambda tag: 1 if "Couple" in tag else 0)
df["Solo_traveler"] = df.Tags.apply(lambda tag: 1 if "Solo traveler" in tag else 0)
df["Business_trip"] = df.Tags.apply(lambda tag: 1 if "Business trip" in tag else 0)
df["Group"] = df.Tags.apply(lambda tag: 1 if "Group" in tag or "Travelers with friends" in tag else 0)
df["Family_with_young_children"] = df.Tags.apply(lambda tag: 1 if "Family with young children" in tag else 0)
df["Family_with_older_children"] = df.Tags.apply(lambda tag: 1 if "Family with older children" in tag else 0)
df["With_a_pet"] = df.Tags.apply(lambda tag: 1 if "With a pet" in tag else 0)

```

### 保存文件

最后，将当前数据集以新名称保存。

```python
df.drop(["Review_Total_Negative_Word_Counts", "Review_Total_Positive_Word_Counts", "days_since_review", "Total_Number_of_Reviews_Reviewer_Has_Given"], axis = 1, inplace=True)

# 保存包含计算列的新数据文件
print("Saving results to Hotel_Reviews_Filtered.csv")
df.to_csv(r'../data/Hotel_Reviews_Filtered.csv', index = False)
```

## 情感分析操作

在最后一节中，我们将对评论列应用情感分析，并将结果保存到数据集中。

## 练习：加载并保存筛选后的数据

注意：现在加载的是上一节保存的筛选后数据集，**而非**原始数据集。

```python
import time
import pandas as pd
import nltk as nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# 从CSV加载筛选后的酒店评论
df = pd.read_csv('../../data/Hotel_Reviews_Filtered.csv')

# 在此处添加你的代码


# 最后记得保存添加了新NLP数据的酒店评论
print("Saving results to Hotel_Reviews_NLP.csv")
df.to_csv(r'../data/Hotel_Reviews_NLP.csv', index = False)
```

### 移除停用词

若直接对负面和正面评论列进行情感分析，可能会耗时较长。在配备快速 CPU 的高性能测试笔记本上，根据使用的情感分析库不同，耗时约 12-14 分钟。这（相对而言）是较长时间，因此值得研究如何提速。

第一步是移除停用词（即不影响句子情感的常见英语单词）。移除停用词后，情感分析的速度会加快，且准确性不会降低（因为停用词不影响情感，但会拖慢分析速度）。

最长的负面评论有 395 个词，移除停用词后仅剩 195 个词。

移除停用词的操作本身很快：在测试设备上，对 515,000 行数据的 2 个评论列移除停用词仅需 3.3 秒。具体耗时可能因设备的 CPU 速度、内存、是否使用固态硬盘等因素略有差异。由于该操作耗时较短，若能缩短情感分析时间，则值得执行。

```python
from nltk.corpus import stopwords

# 从CSV加载酒店评论
df = pd.read_csv("../../data/Hotel_Reviews_Filtered.csv")

# 移除停用词——处理大量文本时可能较慢！
# Ryan Han（Kaggle上的ryanxjhan）发布了一篇很棒的帖子，对比了不同停用词移除方法的性能
# https://www.kaggle.com/ryanxjhan/fast-stop-words-removal # 采用Ryan推荐的方法
start = time.time()
cache = set(stopwords.words("english"))
def remove_stopwords(review):
    text = " ".join([word for word in review.split() if word not in cache])
    return text

# 从两个列中移除停用词
df.Negative_Review = df.Negative_Review.apply(remove_stopwords)   
df.Positive_Review = df.Positive_Review.apply(remove_stopwords)
```

### 执行情感分析

现在需要计算负面和正面评论列的情感得分，并将结果存储在 2 个新列中。情感分析的有效性可通过与同一条评论的评论者评分对比来检验。例如，若情感分析认为负面评论的情感得分为 1（极度正面）且正面评论的情感得分为 1，但评论者给酒店打了最低分，则可能是评论文本与评分不匹配，或情感分析器未能正确识别情感。需注意，部分情感得分可能完全错误，这通常是有原因的，例如评论可能带有强烈讽刺意味（如 “我当然*喜欢*睡在没有暖气的房间里”），情感分析器会认为这是正面情感，而人类读者能识别出其中的讽刺。

NLTK 提供了多种情感分析器供学习使用，你可以替换分析器以观察情感分析准确性的变化。此处使用 VADER 情感分析器。

> Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

```python
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# 创建vader情感分析器（NLTK中还有其他分析器可供尝试）
vader_sentiment = SentimentIntensityAnalyzer()
# Hutto, C.J. & Gilbert, E.E. (2014). VADER: 一种用于社交媒体文本情感分析的简洁规则模型。第八届网络日志和社交媒体国际会议（ICWSM-14）。美国密歇根州安阿伯，2014年6月。

# 评论的输入有3种可能：
# 可能是"No Negative"（无负面内容），此时返回0
# 可能是"No Positive"（无正面内容），此时返回0
# 可能是一条评论，此时计算其情感得分
def calc_sentiment(review):    
    if review == "No Negative" or review == "No Positive":
        return 0
    return vader_sentiment.polarity_scores(review)["compound"]    
```

在程序中准备好计算情感得分后，可按如下方式将其应用于每条评论：

```python
# 添加负面情感和正面情感列
print("计算正面和负面评论的情感列")
start = time.time()
df["Negative_Sentiment"] = df.Negative_Review.apply(calc_sentiment)
df["Positive_Sentiment"] = df.Positive_Review.apply(calc_sentiment)
end = time.time()
print("计算情感耗时" + str(round(end - start, 2)) + "秒")
```

在我的计算机上，该操作约需 120 秒，具体耗时因设备而异。若想打印结果并查看情感得分与评论是否匹配，可执行以下代码：

```python
df = df.sort_values(by=["Negative_Sentiment"], ascending=True)
print(df[["Negative_Review", "Negative_Sentiment"]])
df = df.sort_values(by=["Positive_Sentiment"], ascending=True)
print(df[["Positive_Review", "Positive_Sentiment"]])
```

在将文件用于挑战前，最后一步是保存它！你还可以考虑重新排列新列的顺序，以便于后续处理（对人类而言，这是一种美化操作）。

```python
# 重新排列列（仅为美化，方便后续探索数据）
df = df.reindex(["Hotel_Name", "Hotel_Address", "Total_Number_of_Reviews", "Average_Score", "Reviewer_Score", "Negative_Sentiment", "Positive_Sentiment", "Reviewer_Nationality", "Leisure_trip", "Couple", "Solo_traveler", "Business_trip", "Group", "Family_with_young_children", "Family_with_older_children", "With_a_pet", "Negative_Review", "Positive_Review"], axis=1)

print("将结果保存到Hotel_Reviews_NLP.csv")
df.to_csv(r"../data/Hotel_Reviews_NLP.csv", index = False)
```

在挑战中使用该文件前，需运行[分析笔记本](https://github.com/microsoft/ML-For-Beginners/blob/main/6-NLP/5-Hotel-Reviews-2/solution/3-notebook.ipynb)的完整代码（需先运行[筛选笔记本](https://github.com/microsoft/ML-For-Beginners/blob/main/6-NLP/5-Hotel-Reviews-2/solution/1-notebook.ipynb)生成 Hotel_Reviews_Filtered.csv 文件）。

回顾步骤如下：

1. 原始数据集文件**Hotel_Reviews.csv**在之前的课程中通过[探索器笔记本](https://github.com/microsoft/ML-For-Beginners/blob/main/6-NLP/4-Hotel-Reviews-1/solution/notebook.ipynb)进行了探索
2. Hotel_Reviews.csv 经[筛选笔记本](https://github.com/microsoft/ML-For-Beginners/blob/main/6-NLP/5-Hotel-Reviews-2/solution/1-notebook.ipynb)筛选后生成**Hotel_Reviews_Filtered.csv**
3. Hotel_Reviews_Filtered.csv 经[情感分析笔记本](https://github.com/microsoft/ML-For-Beginners/blob/main/6-NLP/5-Hotel-Reviews-2/solution/3-notebook.ipynb)处理后生成**Hotel_Reviews_NLP.csv**
4. 在下方的 NLP 挑战中使用 Hotel_Reviews_NLP.csv

### 结论

起初，你拿到的数据集包含一些无法验证或无用的列和数据。通过探索数据、筛选无用信息、将标签转换为有用形式、计算自定义平均值、添加情感列等操作，希望你能学到处理自然文本的有趣知识。

## [课后测验](https://gray-sand-07a10f403.1.azurestaticapps.net/quiz/40/)

## 挑战

既然你已对数据集进行了情感分析，尝试运用本课程所学的策略（如聚类）来找出情感相关的模式 

学习[此 Learn 模块](https://docs.microsoft.com/en-us/learn/modules/classify-user-feedback-with-the-text-analytics-api/?WT.mc_id=academic-77952-leestott)，了解更多内容并使用不同工具探索文本中的情感。
## 作业

[尝试不同的数据集](assignment.md)
