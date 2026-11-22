# N165: γ_base 的构成：γ_base = λ_impression * (1 - bounce_rate)，其中 λ_impression 为平台算法给予该商品的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N50

## Claim

γ_base 的构成：γ_base = λ_impression * (1 - bounce_rate)，其中 λ_impression 为平台算法给予该商品的日均自然曝光次数，bounce_rate 为曝光后未点击的比率；需通过平台日志统计特定品类（如手机）的日均自然曝光均值以实例化 λ_impression。

## Corrected Claim

γ_base 的构成：γ_base = λ_impression * (1 - bounce_rate)，其中 λ_impression 为平台算法给予该商品的日均自然曝光次数，bounce_rate 为曝光后未点击的比率；需通过平台日志统计特定品类（如手机）的日均自然曝光均值以实例化 λ_impression。（注：此为特定模型定义，缺乏通用外部来源支持）

## Evidence

[质询]该陈述属于特定业务场景下的经验性模型定义，并非通用物理或数学定律。参考来源[1]讨论的是计算机科学中的λ演算（Lambda Calculus），与电商曝光率无关；来源[2]讨论的是图像处理的Gamma校正，与电商指标无关。两个来源均与该事实主题完全无关，无法提供外部支持。此外，'γ_base'这一符号在通用电商领域并非标准术语，其具体构成公式依赖于特定内部模型或论文定义，缺乏通用性验证。 | 逻辑上，曝光次数乘以点击率（1-跳出率）得到有效点击/转化基数，量纲和逻辑自洽。但参考来源[1]和[2]均与该电商业务事实无关，属于经验事实且缺乏直接来源支持，故降级。

## Search Query

second hand marketplace daily average organic impressions product category

## Retrieval Sources

- {'url': 'https://blog.csdn.net/ChuanfangChen/article/details/138157389&rut=7c560c534c993587488ac46b18bc92043422ab3998197f7abc57fe91b84fbac5', 'type': 'ddg', 'title': '全量知识系统 程序详细设计 定稿之 1"λ演算"及其三个基本转换规则+2计算模型-情态模型中的λ演算图灵机微感机：计算分'}
- {'url': 'https://blog.csdn.net/u013185349/article/details/85103473&rut=29cd1142f6d9eccd31fabc4926078db808bdf9a43126701aa37c70b081beb9ec', 'type': 'ddg', 'title': '图像Gamma校正原理与实践-CSDN博客'}
