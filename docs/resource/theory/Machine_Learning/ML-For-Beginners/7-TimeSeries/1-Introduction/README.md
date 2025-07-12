# 时间序列预测简介

![时间序列概述草图](../../sketchnotes/ml-timeseries.png)

> 草图作者：[Tomomi Imura](https://www.twitter.com/girlie_mac)

在本节课和下一节课中，你将了解一些关于时间序列预测的知识，这是机器学习科学家技能库中一个有趣且有价值的部分，相比其他主题知名度稍低。时间序列预测有点像“水晶球”：基于价格等变量的过去表现，你可以预测其未来的潜在价值。

[![时间序列预测简介](https://img.youtube.com/vi/cBojo1hsHiI/0.jpg)](https://youtu.be/cBojo1hsHiI "时间序列预测简介")

> ? 点击上方图片观看关于时间序列预测的视频

## [课前小测](https://gray-sand-07a10f403.1.azurestaticapps.net/quiz/41/)

这是一个实用且有趣的领域，对业务具有实际价值，因为它直接应用于定价、库存和供应链问题等场景。虽然深度学习技术已开始用于获取更多见解以更好地预测未来表现，但时间序列预测仍然是一个深受经典机器学习技术影响的领域。

> 宾夕法尼亚州立大学有用的时间序列课程可在[此处](https://online.stat.psu.edu/stat510/lesson/1)找到

## 引言

假设你维护着一组智能停车计时器，它们提供了关于不同时段使用频率和时长的数据。

> 要是能基于计时器过去的使用情况，根据供需规律预测其未来价值，会怎么样呢？

准确预测何时采取行动以实现目标，是一个可以通过时间序列预测解决的挑战。在繁忙时段，当人们正在寻找停车位时提高收费可能会让大家不高兴，但这肯定是一种筹集街道清洁资金的方式！

让我们探索一些时间序列算法的类型，并开始使用笔记本清理和准备一些数据。你将分析的数据来自GEFCom2014预测竞赛，包含2012至2014年间3年的每小时电力负荷和温度值。基于电力负荷和温度的历史模式，你可以预测未来的电力负荷值。

在这个例子中，你将学习如何仅使用历史负荷数据预测未来一个时间步长的值。不过，在开始之前，了解其背后的原理是很有用的。

## 一些定义

当遇到“时间序列”这个术语时，你需要理解它在不同语境中的用法。

? **时间序列**

在数学中，“时间序列是按时间顺序索引（或列出或绘制）的一系列数据点。最常见的是，时间序列是在连续的等时间间隔点上获取的序列。”时间序列的一个例子是[道琼斯工业平均指数](https://wikipedia.org/wiki/Time_series)的每日收盘价。时间序列图和统计建模的应用在信号处理、天气预报、地震预测以及其他事件发生且数据点可随时间绘制的领域中经常遇到。

? **时间序列分析**

时间序列分析是对上述时间序列数据的分析。时间序列数据可以有不同的形式，包括“中断时间序列”，它用于检测时间序列在中断事件前后的演变模式。所需的时间序列分析类型取决于数据的性质。时间序列数据本身可以是数字或字符序列的形式。

分析可以使用多种方法，包括频域和时域方法、线性和非线性方法等。[了解更多](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm)关于分析这类数据的多种方式。

? **时间序列预测**

时间序列预测是使用模型基于先前收集的数据所呈现的模式来预测未来值。虽然可以使用回归模型探索时间序列数据（将时间索引作为图上的x变量），但这类数据最好使用特殊类型的模型进行分析。

时间序列数据是有序观测的列表，不同于可以通过线性回归分析的数据。最常见的模型是ARIMA，它是“自回归积分移动平均”的缩写。

[ARIMA模型](https://online.stat.psu.edu/stat510/lesson/1/1.1)“将序列的当前值与过去值和过去的预测误差相关联”。它们最适合分析时域数据，即数据按时间顺序排列的数据。

> ARIMA模型有几种类型，你可以在[此处](https://people.duke.edu/~rnau/411arim.htm)了解更多，并且在下一节课中会涉及到。

在下一节课中，你将使用[单变量时间序列](https://itl.nist.gov/div898/handbook/pmc/section4/pmc44.htm)构建ARIMA模型，单变量时间序列专注于随时间变化的一个变量。这类数据的一个例子是[这个数据集](https://itl.nist.gov/div898/handbook/pmc/section4/pmc4411.htm)，它记录了莫纳罗亚天文台的每月二氧化碳浓度：

| 二氧化碳 | 年月    | 年份 | 月份 |
| :------- | :------ | :--- | :--- |
| 330.62   | 1975.04 | 1975 | 1    |
| 331.40   | 1975.13 | 1975 | 2    |
| 331.87   | 1975.21 | 1975 | 3    |
| 333.18   | 1975.29 | 1975 | 4    |
| 333.92   | 1975.38 | 1975 | 5    |
| 333.43   | 1975.46 | 1975 | 6    |
| 331.85   | 1975.54 | 1975 | 7    |
| 330.01   | 1975.63 | 1975 | 8    |
| 328.51   | 1975.71 | 1975 | 9    |
| 328.41   | 1975.79 | 1975 | 10   |
| 329.25   | 1975.88 | 1975 | 11   |
| 330.97   | 1975.96 | 1975 | 12   |

? 找出这个数据集中随时间变化的变量

## 需要考虑的时间序列数据特征

查看时间序列数据时，你可能会注意到它具有[某些特征](https://online.stat.psu.edu/stat510/lesson/1/1.1)，为了更好地理解其模式，你需要考虑这些特征并进行缓解。如果你将时间序列数据视为可能提供你想要分析的“信号”，那么这些特征可以被视为“噪声”。你通常需要通过使用一些统计技术来抵消其中一些特征，以减少这种“噪声”。

以下是处理时间序列时需要了解的一些概念：

? **趋势（Trends）**

趋势被定义为随时间的可测量增减。[了解更多](https://machinelearningmastery.com/time-series-trends-in-python)。在时间序列的背景下，是关于如何使用趋势以及在必要时从时间序列中去除趋势。

? **[季节性（Seasonality）](https://machinelearningmastery.com/time-series-seasonality-with-python/)**

季节性被定义为周期性波动，例如可能影响销售的假日旺季。[看看](https://itl.nist.gov/div898/handbook/pmc/section4/pmc443.htm)不同类型的图如何显示数据中的季节性。

? **异常值（Outliers）**

异常值是远离标准数据方差的数据点。

? **长期周期（Long-run cycle）**

与季节性无关，数据可能显示长期周期，例如持续一年以上的经济衰退。

? **恒定方差（Constant variance）**

随着时间的推移，一些数据表现出恒定的波动，例如每天和每晚的能源使用量。

? **突变（Abrupt changes）**

数据可能会出现需要进一步分析的突变。例如，由于COVID导致的企业突然关闭，引起了数据变化。

? 这里有一个[时间序列样本图](https://www.kaggle.com/kashnitsky/topic-9-part-1-time-series-analysis-in-python)，显示了几年内每日的游戏内货币支出。你能在这个数据中识别出上面列出的任何特征吗？

![游戏内货币支出](./images/currency.png)

## 练习 - 开始处理电力使用数据

让我们开始创建一个时间序列模型，根据过去的电力使用情况预测未来的电力使用量。

> 本示例中的数据来自GEFCom2014预测竞赛，包含2012至2014年间3年的每小时电力负荷和温度值。
>
> Tao Hong, Pierre Pinson, Shu Fan, Hamidreza Zareipour, Alberto Troccoli and Rob J. Hyndman, "Probabilistic energy forecasting: Global Energy Forecasting Competition 2014 and beyond", International Journal of Forecasting, vol.32, no.3, pp 896-913, July-September, 2016.

1. 在本节课的`working`文件夹中，打开_notebook.ipynb_文件。首先添加帮助你加载和可视化数据的库：

    ```python
    import os
    import matplotlib.pyplot as plt
    from common.utils import load_data
    %matplotlib inline
    ```

    注意，你正在使用包含的`common`文件夹中的文件，这些文件用于设置环境和处理数据下载。

2. 接下来，通过调用`load_data()`和`head()`查看数据框：

    ```python
    data_dir = './data'
    energy = load_data(data_dir)[['load']]
    energy.head()
    ```

    你可以看到有两列，分别表示日期和负荷：

    |                     |  负荷  |
    | :-----------------: | :----: |
    | 2012-01-01 00:00:00 | 2698.0 |
    | 2012-01-01 01:00:00 | 2558.0 |
    | 2012-01-01 02:00:00 | 2444.0 |
    | 2012-01-01 03:00:00 | 2402.0 |
    | 2012-01-01 04:00:00 | 2403.0 |

3. 现在，调用`plot()`绘制数据：

    ```python
    energy.plot(y='load', subplots=True, figsize=(15, 8), fontsize=12)
    plt.xlabel('时间戳', fontsize=12)
    plt.ylabel('负荷', fontsize=12)
    plt.show()
    ```

    ![能源图](images/energy-plot.png)

4. 现在，通过以`[起始日期]:[结束日期]`的格式向`energy`提供输入，绘制2014年7月的第一周数据：

    ```python
    energy['2014-07-01':'2014-07-07'].plot(y='load', subplots=True, figsize=(15, 8), fontsize=12)
    plt.xlabel('时间戳', fontsize=12)
    plt.ylabel('负荷', fontsize=12)
    plt.show()
    ```

    ![七月](images/july-2014.png)

    一个很棒的图！看看这些图，看看你能否确定上面列出的任何特征。通过可视化数据，我们能得出什么结论？

在下一节课中，你将创建一个ARIMA模型来进行一些预测。

---

## ?挑战

列出你能想到的所有可以从时间序列预测中受益的行业和研究领域。你能想到这些技术在艺术、计量经济学、生态学、零售业、工业、金融业等领域的应用吗？还有其他领域吗？

## [课后小测](https://gray-sand-07a10f403.1.azurestaticapps.net/quiz/42/)

## 复习与自学

尽管我们这里不会涉及，但神经网络有时被用于增强经典的时间序列预测方法。在[这篇文章](https://medium.com/microsoftazure/neural-networks-for-forecasting-financial-and-economic-time-series-6aca370ff412)中了解更多相关内容。

## 作业

[可视化更多时间序列](assignment.md)
