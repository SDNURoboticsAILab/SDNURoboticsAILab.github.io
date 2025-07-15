# 使用酒店评论进行情感分析 - 数据处理

在本节中，你将使用前面课程中介绍的技术，对一个大型数据集进行探索性数据分析。一旦你对各列数据的用途有了充分了解，你将学习：

- 如何删除不必要的列  
- 如何基于已有列计算出新数据  
- 如何保存处理后的数据集，以供最终挑战使用  

## [课前测验](https://gray-sand-07a10f403.1.azurestaticapps.net/quiz/37/)

### 简介

到目前为止，你已经了解到文本数据与数值型数据有很大不同。如果是人类书写或口述的文本，我们可以对其进行分析，找出模式、频率、情感和含义。本节课将带你接触一个真实的数据集和一个实际挑战：**[欧洲 515K 酒店评论数据](https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe)**，该数据集采用[CC0：公共领域许可](https://creativecommons.org/publicdomain/zero/1.0/)。数据来源于缤客网（[Booking.com](https://booking.com/)）的公开信息，由刘佳 Shen（Jiashen Liu）创建。

### 准备工作

* 你需要：

  * 能够使用 Python 3 运行 .ipynb 笔记本文件  
  * pandas 库  
  * NLTK（[你应在本地安装](https://www.nltk.org/install.html)）  
  * 数据集文件，可在 Kaggle 上获取：[515K Hotel Reviews Data in Europe](https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe)，解压后约为 230 MB。请下载并放置在本课程相关的 `/data` 根目录中。  

## 探索性数据分析

本挑战假设你正在构建一个结合情感分析和客人评论评分的酒店推荐机器人。你将使用的数据集包含 6 个城市的 1493 家不同酒店的评论。

借助 Python、酒店评论数据集和 NLTK 的情感分析功能，你可以找出：

* 评论中最常用的词语和短语是什么？
* 描述酒店的官方 “标签” 与评论分数是否相关（例如，某酒店的负面评论是否更多来自 “带小孩的家庭” 而非 “独自旅行者”，这可能表明该酒店更适合 “独自旅行者”）？
* NLTK 的情感评分与酒店评论者的数值评分是否 “一致”？

#### 数据集

让我们探索你已下载并保存到本地的数据集。用 VS Code 甚至 Excel 等编辑器打开文件。

数据集的标题如下：

*Hotel_Address（酒店地址）、Additional_Number_of_Scoring（额外评分数量）、Review_Date（评论日期）、Average_Score（平均评分）、Hotel_Name（酒店名称）、Reviewer_Nationality（评论者国籍）、Negative_Review（负面评论）、Review_Total_Negative_Word_Counts（评论负面词汇总数量）、Total_Number_of_Reviews（总评论数量）、Positive_Review（正面评论）、Review_Total_Positive_Word_Counts（评论正面词汇总数量）、Total_Number_of_Reviews_Reviewer_Has_Given（评论者给出的总评论数量）、Reviewer_Score（评论者评分）、Tags（标签）、days_since_review（距评论的天数）、lat（纬度）、lng（经度）*

以下是更便于查看的分组方式：
##### 酒店相关列

* `Hotel_Name`（酒店名称）、`Hotel_Address`（酒店地址）、`lat`（纬度）、`lng`（经度）
  * 可使用 *lat* 和 *lng* 绘制酒店分布图（可根据正面/负面评论进行颜色标注） 
  * `Hotel_Address` 暂时无用，之后可能替换为国家以便于排序和搜索  

##### **酒店元评论列**

* `Average_Score`（平均评分）
  
  * 根据数据集创建者的说明，该列是 “基于过去一年最新评论计算的酒店平均评分”。这种计算评分的方式似乎不太常见，但这是抓取到的数据，目前我们姑且按其表面意思理解。
  
  ✅ 根据数据中的其他列，你能想到另一种计算平均评分的方法吗？
  
* `Total_Number_of_Reviews`（总评论数量）
  
  * 该酒店收到的总评论数量 —— 目前尚不清楚（不编写代码的话）这是否指数据集中的评论数量。
* `Additional_Number_of_Scoring`（额外评分数量）
  
  * 这指的是有评论者给出了评分，但没有写下正面或负面评论。

##### **评论相关列**

- `Reviewer_Score`（评论者评分）
  - 这是一个最多保留 1 位小数的数值，范围在 2.5 到 10 之间
  - 目前不清楚为什么最低评分是 2.5
- `Negative_Review`（负面评论）
  - 如果评论者未写负面内容，该字段将显示 “**No Negative**（无负面内容）”
  - 注意，评论者可能在负面评论列中写正面内容（例如，“这家酒店没有任何不好的地方”）
- `Review_Total_Negative_Word_Counts`（评论负面词汇总数量）
  - 负面词汇数量越多，评分可能越低（不考虑情感倾向）
- `Positive_Review`（正面评论）
  - 如果评论者未写正面内容，该字段将显示 “**No Positive**（无正面内容）”
  - 注意，评论者可能在正面评论列中写负面内容（例如，“这家酒店根本没有任何好的地方”）
- `Review_Total_Positive_Word_Counts`（评论正面词汇总数量）
  - 正面词汇数量越多，评分可能越高（不考虑情感倾向）
- `Review_Date`（评论日期）和`days_since_review`（距评论的天数）
  - 可以对评论应用新鲜度或陈旧度衡量标准（旧评论可能不如新评论准确，因为酒店管理层可能已更换、进行过翻新或新增了泳池等设施）
- `Tags`（标签）
  - 这些是评论者可能选择的简短描述符，用于说明他们的客人类型（例如，独自旅行或家庭旅行）、房间类型、停留时间以及评论提交的设备类型。
  - 遗憾的是，使用这些标签存在问题，请查看下面讨论其有用性的部分

**评论者相关列**

- `Total_Number_of_Reviews_Reviewer_Has_Given`（评论者给出的总评论数量）
  - 这可能是推荐模型中的一个因素，例如，如果你能确定发表过数百条评论的高产评论者更可能给出负面而非正面评价。然而，任何特定评论的评论者都没有唯一代码标识，因此无法与一组评论关联。有 30 位评论者发表了 100 条或更多评论，但很难看出这对推荐模型有何帮助。
- `Reviewer_Nationality`（评论者国籍）
  - 有些人可能认为，某些国籍的人由于民族倾向更可能给出正面或负面评价。在模型中植入此类轶事观点时要谨慎。这些是国家（有时是种族）刻板印象，每位评论者都是独立的个体，其评论基于自身体验。这种体验可能经过多种视角过滤，例如他们之前的酒店住宿经历、旅行距离以及个人性格。认为他们的国籍是影响评论评分的原因，这一观点难以成立。

##### 示例

| 平均评分（Average Score） | 总评论数量（Total Number Reviews） | 评论者评分（Reviewer Score） | 负面评论（Negative<br/>Review） Review）                     | 正面评论（Positive Review）          | 标签（Tags）                       |
| ------------------------- | ---------------------------------- | ---------------------------- | :----------------------------------------------------------- | ------------------------------------ | ---------------------------------- |
| 7.8                       | 1945                               | 2.5                          | 这里目前不是酒店，而是一个建筑工地。我长途旅行后在房间休息和工作时，从清晨到全天都被令人无法接受的施工噪音困扰。我要求换房，但没有安静的房间了。更糟的是，我被多收费了。因为要赶早班飞机，我晚上就退房了，收到了合理的账单。但一天后，酒店在未经我同意的情况下又收取了一笔费用，超过了预订价格。这地方太糟糕了。别订这里折磨自己。 | 完全没有优点。糟糕的地方，远离这里。 | 商务旅行 情侣 标准双人间 住了 2 晚 |

如你所见，这位客人在这家酒店的住宿体验很不愉快。该酒店的平均评分为 7.8，有 1945 条评论，但这位评论者给了 2.5 分，并写了 115 个字描述其糟糕的住宿经历。如果他们在正面评论列中什么都没写，你可能会推测没有正面内容，但遗憾的是他们写了 7 个字的警告。如果我们只计算字数而不考虑词语的含义或情感，可能会误解评论者的意图。奇怪的是，他们给出 2.5 分让人困惑，因为如果住宿体验如此糟糕，为什么还要给分呢？仔细研究数据集会发现，最低可能评分是 2.5，而非 0。最高可能评分是 10。

##### 标签

如上所述，乍一看，使用`Tags`（标签）对数据进行分类是合理的。但遗憾的是，这些标签没有标准化，这意味着在某家酒店中，选项可能是 “单人间”“双床间” 和 “双人间”，而在下一家酒店中，可能是 “豪华单人间”“经典大床房” 和 “行政大床房”。这些可能指的是同一类房间，但变体太多，因此有两种选择：

1. 尝试将所有术语统一为单一标准，这非常困难，因为不清楚每种情况下的转换路径（例如，“经典单人间” 可对应 “单人间”，但 “带庭院花园或城市景观的高级大床房” 则很难对应）

1. 我们可以采用 NLP 方法，衡量某些术语（如 “独自旅行”“商务旅行者” 或 “带小孩的家庭”）在每家酒店中的出现频率，并将其纳入推荐因素


标签通常（但不总是）是一个单独的字段，包含 5 到 6 个逗号分隔的值，对应 “旅行类型”“客人类型”“房间类型”“住宿晚数” 和 “评论提交设备类型”。然而，由于有些评论者没有填写每个字段（可能留空一个），这些值的顺序并不总是一致的。

例如，以 “群体类型” 为例。`Tags`列中该字段有 1025 种独特的可能性，遗憾的是，其中只有部分涉及群体（有些是房间类型等）。如果只筛选提到 “家庭” 的标签，结果会包含很多 “家庭房” 类型的结果。如果包含 “with”（带）这个词，即统计 “Family with”（带…… 的家庭）的值，结果会更好，在 515,000 条结果中，有超过 80,000 条包含 “带小孩的家庭” 或 “带大孩子的家庭”。

这意味着标签列对我们并非完全无用，但需要一些处理才能使其有用。

##### 酒店平均评分

数据集中存在一些我无法解释的异常或不一致之处，但在此说明，以便你在构建模型时有所了解。如果你弄明白了，欢迎在讨论区告诉我们！

数据集中与平均评分和评论数量相关的列如下：

1. Hotel_Name（酒店名称）
2. Additional_Number_of_Scoring（额外评分数量）
3. Average_Score（平均评分）
4. Total_Number_of_Reviews（总评论数量）
5. Reviewer_Score（评论者评分）

数据集中评论数量最多的酒店是 “不列颠尼亚国际酒店金丝雀码头店（Britannia International Hotel Canary Wharf）”，在 515,000 条评论中占 4789 条。但查看该酒店的`Total_Number_of_Reviews`（总评论数量）值，是 9086。你可能会推测，还有很多评分没有对应的评论，因此或许应该加上`Additional_Number_of_Scoring`（额外评分数量）列的值。该值为 2682，与 4789 相加得到 7471，仍比`Total_Number_of_Reviews`（总评论数量）少 1615。

对于`Average_Score`（平均评分）列，你可能会推测它是数据集中评论的平均值，但 Kaggle 上的描述是 “基于过去一年最新评论计算的酒店平均评分”。这似乎没什么用，但我们可以根据数据集中的评论评分计算自己的平均值。以同一家酒店为例，给出的酒店平均评分为 7.1，但计算得出的分数（数据集中评论者评分的平均值）是 6.8。两者接近但不相同，我们只能猜测`Additional_Number_of_Scoring`（额外评分数量）中的评分将平均值提高到了 7.1。但由于无法测试或证明这一断言，因此很难使用或信任`Average_Score`（平均评分）、`Additional_Number_of_Scoring`（额外评分数量）和`Total_Number_of_Reviews`（总评论数量），因为它们基于或涉及我们没有的数据。

更复杂的是，评论数量第二多的酒店计算得出的平均评分为 8.12，而数据集中的`Average_Score`（平均评分）是 8.1。这个准确的分数是巧合还是第一家酒店的数据存在差异？ 

考虑到这些酒店可能是异常值，且大多数值可能一致（但有些由于某种原因不一致），接下来我们将编写一个简短的程序来探索数据集中的值，以确定这些值的正确用法（或不用法）。

> 🚨 注意事项
>
> 处理此数据集时，你会编写代码从文本中计算某些内容，而无需自己阅读或分析文本。这是 NLP 的核心，即无需人工干预即可解释含义或情感。然而，你可能会读到一些负面评论。我建议你不要读，因为没必要。有些负面酒店评论很愚蠢或无关紧要，例如 “天气不好”，这超出了酒店的控制范围，实际上也超出了任何人的控制范围。但有些评论也有阴暗面。有时负面评论带有种族主义、性别歧视或年龄歧视色彩。这很不幸，但在从公共网站抓取的数据集里是可以预料到的。有些评论者留下的评论可能会让你感到反感、不适或不安。最好让代码来衡量情感，而不是自己阅读这些评论。

## 练习 —— 数据探索

### 加载数据

现在对数据的可视化检查已经足够了，接下来你将编写一些代码并获得一些答案！本节将使用 `pandas` 库。你的第一个任务是确保你能够加载并读取 CSV 数据。`pandas` 库拥有快速的 CSV 加载器，加载的结果会被存储在一个 dataframe（数据框）中，就像前面的课程一样。我们要加载的这个 CSV 文件有超过 50 万行，但只有 17 列。`pandas` 为你提供了许多强大的方式来与 dataframe 交互，包括可以对每一行执行操作的能力

从本节开始，将会出现一些代码片段、对这些代码的解释，以及关于结果含义的讨论。请在附带的 *notebook.ipynb* 文件中编写你的代码。

让我们从加载你将要使用的数据文件开始：

```python
# Load the hotel reviews from CSV
import pandas as pd
import time
# importing time so the start and end time can be used to calculate file loading time
print("Loading data file now, this could take a while depending on file size")
start = time.time()
# df is 'DataFrame' - make sure you downloaded the file to the data folder
df = pd.read_csv('../../data/Hotel_Reviews.csv')
end = time.time()
print("Loading took " + str(round(end - start, 2)) + " seconds")
```

数据加载完成后，我们可以对其执行一些操作。将此代码保留在程序顶部，用于下一步操作。

## 探索数据

在这种情况下，数据已经是 “干净的”，这意味着它可以直接使用，没有其他语言的字符，不会干扰期望只处理英文字符的算法。

✅ 你可能需要处理一些初始数据，在应用 NLP 技术之前需要对其进行格式化，但这次不需要。如果需要，你会如何处理非英文字符？

花点时间确保数据加载后，你可以用代码探索它。很容易想专注于`Negative_Review`（负面评论）和`Positive_Review`（正面评论）列。这些列充满了自然文本，可供你的 NLP 算法处理。但先别急着进行 NLP 和情感分析！你应该按照下面的代码，确定数据集中给出的值是否与你用 pandas 计算的值一致。

## 数据框操作

本节课的第一个任务是通过编写代码检查数据框（不修改它），验证以下断言是否正确。

> 与许多编程任务一样，完成这项工作有多种方法，但好的建议是用最简单、最容易的方式去做，尤其是当你将来回顾这段代码时，更容易理解。对于数据框，有一个全面的 API，通常能高效地完成你想要做的事情。

将以下问题视为编码任务，尝试在不查看解决方案的情况下回答它们。

1. 打印出你刚刚加载的数据框的 “形状”（形状即行数和列数）
2. 计算评论者国籍的频率：
   1. `Reviewer_Nationality`（评论者国籍）列有多少个不同的值，分别是什么？
   2. 数据集中最常见的评论者国籍是什么（打印国家和评论数量）？
   3. 接下来最常见的 10 个国籍及其频率是多少？
3. 对于前 10 个最常见的评论者国籍，每个国籍评论最多的酒店是什么？
4. 数据集中每家酒店有多少条评论（酒店的频率计数）？
5. 虽然数据集中有每家酒店的`Average_Score`（平均评分）列，但你也可以计算平均评分（求数据集中每家酒店所有评论者评分的平均值）。向数据框中添加一个新列，列标题为`Calc_Average_Score`（计算得出的平均评分），其中包含计算出的平均值。
6. 是否有酒店的`Average_Score`（平均评分）和`Calc_Average_Score`（计算得出的平均评分）四舍五入到 1 位小数后相等？
   1. 尝试编写一个 Python 函数，该函数接受一个 Series（行）作为参数，比较这两个值，并在值不相等时打印一条消息。然后使用`.apply()`方法用该函数处理每一行。
7. 计算并打印出`Negative_Review`（负面评论）列值为 “No Negative”（无负面内容）的行数
8. 计算并打印出`Positive_Review`（正面评论）列值为 “No Positive”（无正面内容）的行数
9. 计算并打印出`Positive_Review`（正面评论）列值为 “No Positive”（无正面内容）**且**`Negative_Review`（负面评论）列值为 “No Negative”（无负面内容）的行数
### 代码答案

1. 打印出你刚刚加载的数据框的 “形状”（形状即行数和列数）

   ```python
   print("The shape of the data (rows, cols) is " + str(df.shape))
   > The shape of the data (rows, cols) is (515738, 17)
   ```

2. 计算评论者国籍的频率：

   1. `Reviewer_Nationality`（评论者国籍）列有多少个不同的值，分别是什么？
   2. 数据集中最常见的评论者国籍是什么（打印国家和评论数量）？

   ```python
   # value_counts() creates a Series object that has index and values in this case, the country and the frequency they occur in reviewer nationality
   nationality_freq = df["Reviewer_Nationality"].value_counts()
   print("There are " + str(nationality_freq.size) + " different nationalities")
   # print first and last rows of the Series. Change to nationality_freq.to_string() to print all of the data
   print(nationality_freq) 
   
   There are 227 different nationalities
    United Kingdom               245246
    United States of America      35437
    Australia                     21686
    Ireland                       14827
    United Arab Emirates          10235
                                  ...  
    Comoros                           1
    Palau                             1
    Northern Mariana Islands          1
    Cape Verde                        1
    Guinea                            1
   Name: Reviewer_Nationality, Length: 227, dtype: int64
   ```

   3. 接下来最常见的 10 个国籍及其频率是多少？

      ```python
      print("The highest frequency reviewer nationality is " + str(nationality_freq.index[0]).strip() + " with " + str(nationality_freq[0]) + " reviews.")
      # Notice there is a leading space on the values, strip() removes that for printing
      # What is the top 10 most common nationalities and their frequencies?
      print("The next 10 highest frequency reviewer nationalities are:")
      print(nationality_freq[1:11].to_string())
      
      The highest frequency reviewer nationality is United Kingdom with 245246 reviews.
      The next 10 highest frequency reviewer nationalities are:
       United States of America     35437
       Australia                    21686
       Ireland                      14827
       United Arab Emirates         10235
       Saudi Arabia                  8951
       Netherlands                   8772
       Switzerland                   8678
       Germany                       7941
       Canada                        7894
       France                        7296
      ```

3. 对于前 10 个最常见的评论者国籍，每个国籍评论最多的酒店是什么？

   ```python
   # What was the most frequently reviewed hotel for the top 10 nationalities
   # Normally with pandas you will avoid an explicit loop, but wanted to show creating a new dataframe using criteria (don't do this with large amounts of data because it could be very slow)
   for nat in nationality_freq[:10].index:
      # First, extract all the rows that match the criteria into a new dataframe
      nat_df = df[df["Reviewer_Nationality"] == nat]   
      # Now get the hotel freq
      freq = nat_df["Hotel_Name"].value_counts()
      print("The most reviewed hotel for " + str(nat).strip() + " was " + str(freq.index[0]) + " with " + str(freq[0]) + " reviews.") 
      
   The most reviewed hotel for United Kingdom was Britannia International Hotel Canary Wharf with 3833 reviews.
   The most reviewed hotel for United States of America was Hotel Esther a with 423 reviews.
   The most reviewed hotel for Australia was Park Plaza Westminster Bridge London with 167 reviews.
   The most reviewed hotel for Ireland was Copthorne Tara Hotel London Kensington with 239 reviews.
   The most reviewed hotel for United Arab Emirates was Millennium Hotel London Knightsbridge with 129 reviews.
   The most reviewed hotel for Saudi Arabia was The Cumberland A Guoman Hotel with 142 reviews.
   The most reviewed hotel for Netherlands was Jaz Amsterdam with 97 reviews.
   The most reviewed hotel for Switzerland was Hotel Da Vinci with 97 reviews.
   The most reviewed hotel for Germany was Hotel Da Vinci with 86 reviews.
   The most reviewed hotel for Canada was St James Court A Taj Hotel London with 61 reviews.
   ```

4. 数据集中每家酒店有多少条评论（酒店的频率计数）？

   ```python
   # First create a new dataframe based on the old one, removing the uneeded columns
   hotel_freq_df = df.drop(["Hotel_Address", "Additional_Number_of_Scoring", "Review_Date", "Average_Score", "Reviewer_Nationality", "Negative_Review", "Review_Total_Negative_Word_Counts", "Positive_Review", "Review_Total_Positive_Word_Counts", "Total_Number_of_Reviews_Reviewer_Has_Given", "Reviewer_Score", "Tags", "days_since_review", "lat", "lng"], axis = 1)
   
   # Group the rows by Hotel_Name, count them and put the result in a new column Total_Reviews_Found
   hotel_freq_df['Total_Reviews_Found'] = hotel_freq_df.groupby('Hotel_Name').transform('count')
   
   # Get rid of all the duplicated rows
   hotel_freq_df = hotel_freq_df.drop_duplicates(subset = ["Hotel_Name"])
   display(hotel_freq_df) 
   ```
   |                 Hotel_Name                 | Total_Number_of_Reviews | Total_Reviews_Found |
   | :----------------------------------------: | :---------------------: | :-----------------: |
   | Britannia International Hotel Canary Wharf |          9086           |        4789         |
   |    Park Plaza Westminster Bridge London    |          12158          |        4169         |
   |   Copthorne Tara Hotel London Kensington   |          7105           |        3578         |
   |                    ...                     |           ...           |         ...         |
   |       Mercure Paris Porte d Orleans        |           110           |         10          |
   |                Hotel Wagner                |           135           |         10          |
   |            Hotel Gallitzinberg             |           173           |          8          |

   你可能会注意到 “数据集中计数的结果” 与`Total_Number_of_Reviews`（总评论数量）中的值不匹配。目前不清楚数据集中的这个值是否代表酒店收到的总评论数量，但并非所有评论都被抓取，或者是其他计算方式。由于这种不确定性，模型中不使用`Total_Number_of_Reviews`（总评论数量）。

5. 虽然数据集中有每家酒店的`Average_Score`（平均评分）列，但你也可以计算平均评分（求数据集中每家酒店所有评论者评分的平均值）。向数据框中添加一个新列，列标题为`Calc_Average_Score`（计算得出的平均评分）。打印出`Hotel_Name`（酒店名称）、`Average_Score`（平均评分）和`Calc_Average_Score`（计算得出的平均评分）列。

   ```python
   # define a function that takes a row and performs some calculation with it
   def get_difference_review_avg(row):
     return row["Average_Score"] - row["Calc_Average_Score"]
   
   # 'mean' is mathematical word for 'average'
   df['Calc_Average_Score'] = round(df.groupby('Hotel_Name').Reviewer_Score.transform('mean'), 1)
   
   # Add a new column with the difference between the two average scores
   df["Average_Score_Difference"] = df.apply(get_difference_review_avg, axis = 1)
   
   # Create a df without all the duplicates of Hotel_Name (so only 1 row per hotel)
   review_scores_df = df.drop_duplicates(subset = ["Hotel_Name"])
   
   # Sort the dataframe to find the lowest and highest average score difference
   review_scores_df = review_scores_df.sort_values(by=["Average_Score_Difference"])
   
   display(review_scores_df[["Average_Score_Difference", "Average_Score", "Calc_Average_Score", "Hotel_Name"]])
   ```

   你可能还想知道`Average_Score`（平均评分）的值，以及为什么它有时与计算得出的平均评分不同。由于我们不知道为什么有些值匹配，而另一些值存在差异，在这种情况下，最安全的做法是使用我们拥有的评论评分自己计算平均值。也就是说，差异通常很小，以下是与数据集平均值和计算得出的平均值偏差最大的酒店：

   | Average_Score_Difference | Average_Score | Calc_Average_Score |                                  Hotel_Name |
   | :----------------------: | :-----------: | :----------------: | ------------------------------------------: |
   |           -0.8           |      7.7      |        8.5         |                  Best Western Hotel Astoria |
   |           -0.7           |      8.8      |        9.5         | Hotel Stendhal Place Vend me Paris MGallery |
   |           -0.7           |      7.5      |        8.2         |               Mercure Paris Porte d Orleans |
   |           -0.7           |      7.9      |        8.6         |             Renaissance Paris Vendome Hotel |
   |           -0.5           |      7.0      |        7.5         |                         Hotel Royal Elys es |
   |           ...            |      ...      |        ...         |                                         ... |
   |           0.7            |      7.5      |        6.8         |     Mercure Paris Op ra Faubourg Montmartre |
   |           0.8            |      7.1      |        6.3         |      Holiday Inn Paris Montparnasse Pasteur |
   |           0.9            |      6.8      |        5.9         |                               Villa Eugenie |
   |           0.9            |      8.6      |        7.7         |   MARQUIS Faubourg St Honor Relais Ch teaux |
   |           1.3            |      7.2      |        5.9         |                          Kube Hotel Ice Bar |

   只有 1 家酒店的评分差值大于 1，这意味着我们可能可以忽略这种差异，使用计算得出的平均评分。

6. 计算并打印出`Negative_Review`（负面评论）列值为 “No Negative”（无负面内容）的行数

7. 计算并打印出`Positive_Review`（正面评论）列值为 “No Positive”（无正面内容）的行数

8. 计算并打印出`Positive_Review`（正面评论）列值为 “No Positive”（无正面内容）**且**`Negative_Review`（负面评论）列值为 “No Negative”（无负面内容）的行数

   ```python
   # with lambdas:
   start = time.time()
   no_negative_reviews = df.apply(lambda x: True if x['Negative_Review'] == "No Negative" else False , axis=1)
   print("Number of No Negative reviews: " + str(len(no_negative_reviews[no_negative_reviews == True].index)))
   
   no_positive_reviews = df.apply(lambda x: True if x['Positive_Review'] == "No Positive" else False , axis=1)
   print("Number of No Positive reviews: " + str(len(no_positive_reviews[no_positive_reviews == True].index)))
   
   both_no_reviews = df.apply(lambda x: True if x['Negative_Review'] == "No Negative" and x['Positive_Review'] == "No Positive" else False , axis=1)
   print("Number of both No Negative and No Positive reviews: " + str(len(both_no_reviews[both_no_reviews == True].index)))
   end = time.time()
   print("Lambdas took " + str(round(end - start, 2)) + " seconds")
   
   Number of No Negative reviews: 127890
   Number of No Positive reviews: 35946
   Number of both No Negative and No Positive reviews: 127
   Lambdas took 9.64 seconds
   ```

## 另一种方法

不使用 lambda 函数，使用 sum 来计数行的另一种方法：

   ```python
   # without lambdas (using a mixture of notations to show you can use both)
   start = time.time()
   no_negative_reviews = sum(df.Negative_Review == "No Negative")
   print("Number of No Negative reviews: " + str(no_negative_reviews))
   
   no_positive_reviews = sum(df["Positive_Review"] == "No Positive")
   print("Number of No Positive reviews: " + str(no_positive_reviews))
   
   both_no_reviews = sum((df.Negative_Review == "No Negative") & (df.Positive_Review == "No Positive"))
   print("Number of both No Negative and No Positive reviews: " + str(both_no_reviews))
   
   end = time.time()
   print("Sum took " + str(round(end - start, 2)) + " seconds")
   
   Number of No Negative reviews: 127890
   Number of No Positive reviews: 35946
   Number of both No Negative and No Positive reviews: 127
   Sum took 0.19 seconds
   ```

你可能已经注意到，有 127 行的`Negative_Review`（负面评论）列值为 “No Negative”（无负面内容），且`Positive_Review`（正面评论）列值为 “No Positive”（无正面内容）。这意味着评论者给了酒店一个数值评分，但没有写任何正面或负面评论。幸运的是，这样的行数量很少（515738 行中的 127 行，即 0.02%），因此可能不会使我们的模型或结果产生偏差，但值得探索数据以发现这样的行。

现在你已经探索了数据集，下一节课你将过滤数据并添加一些情感分析。

---
## 🚀挑战

本节课展示了，正如我们在之前的课程中看到的，在对数据执行操作之前，了解你的数据及其缺陷是至关重要的。特别是基于文本的数据，需要仔细检查。深入研究各种文本密集型数据集，看看你能否发现可能给模型带来偏差或情感倾斜的地方。

## [课后测验](https://gray-sand-07a10f403.1.azurestaticapps.net/quiz/38/)

## 复习与自学

学习[这个 NLP 学习路径](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77952-leestott)，了解构建语音和文本密集型模型时可以尝试的工具。

## 作业

[NLTK](assignment.md)
