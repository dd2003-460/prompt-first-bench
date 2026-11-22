# N34: 性价比综合评分公式定义：Score = (Throughput_TPS * Quality_Score) / (TCO_5Year * Reliability_

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比综合评分公式定义：Score = (Throughput_TPS * Quality_Score) / (TCO_5Year * Reliability_Factor)，其中 Throughput_TPS 为单并发 tokens/sec，Quality_Score 为归一化后的精度损失惩罚因子，TCO_5Year 包含硬件折旧、电力成本（kWh * 电价 * 功耗）及运维人工成本，Reliability_Factor 为故障概率倒数，用于量化长期稳定性对性价比的影响。

## Corrected Claim

该公式为特定评估场景下的自定义性价比评分模型，非行业通用标准；其逻辑结构合理（吞吐量与质量正向，TCO与可靠性负向），但具体权重与形式需依据特定业务需求定义。

## Evidence

[质询]该公式为特定场景下的自定义经验公式，并非行业通用标准或第一性原理可推导的数学恒等式；参考来源仅涉及通用性能指标定义，未提供该特定性价比评分公式的支持，属于缺乏外部证据支持的经验性定义。 | 逻辑自洽（量纲与业务逻辑合理），但参考来源[1]仅讨论QPS/TPS等基础指标，与该特定综合评分公式无关，无直接支持证据，且该公式属经验事实，无法从第一性原理严格推出。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/337708438&rut=381ca795da54d17e718f8a76e4f9f79f13e8d815ed1c4b0bd8b536d3e8426c7b', 'type': 'ddg', 'title': '一文搞懂高并发性能指标：QPS、TPS、RT、并发数、吞吐量'}
