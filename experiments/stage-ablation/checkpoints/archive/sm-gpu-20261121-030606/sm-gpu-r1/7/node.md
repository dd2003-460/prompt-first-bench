# N75: 在‘无硬性延迟’约束下，性价比核心指标定义为每美元生成的Token数（Tokens/$），计算公式为：(吞吐量 tokens/s * 86400 s/day) 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在‘无硬性延迟’约束下，性价比核心指标定义为每美元生成的Token数（Tokens/$），计算公式为：(吞吐量 tokens/s * 86400 s/day) / (硬件折旧成本/年 + 电力成本/年)，需对比单卡H100与双卡4090的该指标差异，预计双卡4090在纯吞吐/成本比上优于单卡H100，但受限于总显存和互联瓶颈。

## Corrected Claim

在‘无硬性延迟’约束下，性价比核心指标通常定义为每美元生成的Token数（Tokens/$），其逻辑为吞吐量与单位时间成本的比值。虽然理论上双卡4090可能在纯吞吐/成本比上具有优势，但具体是否优于单卡H100需依据实际硬件价格、功耗及模型适配情况计算，且受限于总显存和互联瓶颈。

## Evidence

[质询]该陈述包含具体的硬件性能对比结论（双卡4090优于单卡H100）及特定约束下的成本模型细节，属于经验事实。参考来源仅提供了通用的Tokens/$定义，未提供H100与4090的具体吞吐量、折旧及电力成本数据，无法从来源直接验证该特定对比结论的准确性。 | 来源[3]直接支持了Tokens/$作为性价比核心指标的定义及基本逻辑（吞吐量/成本），但所有来源均未覆盖H100与4090的具体对比数据，属于经验事实且缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://michaelygzhang.github.io/ai/2026/03/12/ai-daily-token-economics.html&rut=86bd3ca1826b93c474844818ae7e8dc145ddcd53bf35aaf490de7c010415453b', 'type': 'ddg', 'title': 'AI 应用中的 Token 经济学与成本优化 - ^_^ - 为学日益,为道日损.'}
- {'url': 'https://blog.csdn.net/shizheng_Li/article/details/167397179&rut=b9520798f5e1d961140f08918e70b5e54a93df7e245e232e527f988fb71ea535', 'type': 'ddg', 'title': '大模型推理必懂指标全解析：SLO、TBT、MFU、Goodput 到底是什么？_goodput slo-CSDN博客'}
- {'url': 'https://www.compassingai.com/concept/tokens-per-dollar/&rut=26f4454c677cb924bf39ac43c2117eed71925e75be1dbb69f00cea3939e40eca', 'type': 'ddg', 'title': 'Tokens per Dollar Tokens per Dollar | Compassing AI 概念库'}
