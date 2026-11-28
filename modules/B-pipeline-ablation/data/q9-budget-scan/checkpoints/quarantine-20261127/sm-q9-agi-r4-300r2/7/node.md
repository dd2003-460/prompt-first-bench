# N25: 在长上下文（>128k tokens）场景下，Transformer模型的'Lost in the Middle'效应导致关键信息召回率从短上下文的95%骤降至

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在长上下文（>128k tokens）场景下，Transformer模型的'Lost in the Middle'效应导致关键信息召回率从短上下文的95%骤降至70-80%。对于262k max_model_len，若未采用分段检索（Chunking）或滑动窗口注意力机制，模型在整合全篇文献证据时的遗漏率将高于20%，直接影响研究结论的全面性。

## Corrected Claim

在长上下文场景下，Transformer模型常出现'Lost in the Middle'效应，导致中间位置信息的召回率显著低于首尾位置，具体下降幅度依模型和任务而异。

## Evidence

[质询]具体数值（95%降至70-80%）缺乏通用性，不同模型和任务表现差异巨大，且参考来源完全未涉及此性能衰减数据，属于无来源支持的特定经验断言。 | 逻辑上符合长上下文注意力稀释的已知现象，但参考来源[1]仅讨论上下文长度历史，未提供召回率数据，属经验事实且缺直接来源支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1928837435808282488&rut=752f94c949f2eaa368a525b007c0de4f84547547b51cc1d9bbb4db1c9ec32ce4', 'type': 'ddg', 'title': '为什么主流大模型的上下文窗口都是128k？| 深度 - 知乎'}
