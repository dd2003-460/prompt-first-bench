# N37: 定义性价比指标公式：Value Score = (Throughput_tokens_per_sec * Quality_Score) / (Total_Cos

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

定义性价比指标公式：Value Score = (Throughput_tokens_per_sec * Quality_Score) / (Total_Cost_of_Ownership_per_year)；其中 Quality_Score 归一化至 0-1（基于MMLU/CMMLU），Total_Cost 包含硬件折旧+电力+维护

## Corrected Claim

定义性价比指标公式：Value Score = (Throughput_tokens_per_sec * Quality_Score) / (Total_Cost_of_Ownership_per_year)；其中 Quality_Score 归一化至 0-1（基于MMLU/CMMLU），Total_Cost 包含硬件折旧+电力+维护。注：此为自定义评估框架，非行业标准公式，具体参数需根据实际业务场景调整。

## Evidence

[质询]该公式为自定义指标，参考来源仅涉及推理延迟（TPOT/TTFT）和吞吐量概念，未提供关于将MMLU/CMMLU作为质量分母、或包含硬件折旧/电力/维护的总拥有成本（TCO）的具体定义或行业标准支持，存在口径混淆风险（如MMLU并非唯一或最佳的质量代理指标，且TCO计算方式因场景而异）。 | 逻辑自洽（量纲合理：(tokens/s * score) / cost 可衡量单位成本下的有效产出），但参考来源[1][2]仅讨论推理性能指标（Throughput, TPOT, TTFT），未直接支持该特定性价比公式的定义及TCO构成，属于经验事实且缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/24121326326&rut=33b6cf47a48fb54e64969d374ca49b87c56d8ca2ac7431201b9bcd422bc02efd', 'type': 'ddg', 'title': '吃瓜DeepSeek 推理成本需要的相关概念：Throughput，TPOT，TTFT'}
- {'url': 'https://zhuanlan.zhihu.com/p/2071005997469004510&rut=a9bac896631a5c7b572514e35a70b1c61d091943007bc406a897e03fbefcb02b', 'type': 'ddg', 'title': '浅析大模型推理十二篇之关键指标 - 知乎'}
