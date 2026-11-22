# N34: 性价比综合评分公式定义：Score = (Throughput_TPS * Quality_Score) / (TCO_5Year * Reliability_

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比综合评分公式定义：Score = (Throughput_TPS * Quality_Score) / (TCO_5Year * Reliability_Factor)，其中 Throughput_TPS 为单并发 tokens/sec，Quality_Score 为归一化后的精度损失惩罚因子，TCO_5Year 包含硬件折旧、电力成本（kWh * 电价 * 功耗）及运维人工成本，Reliability_Factor 为故障概率倒数，用于量化长期稳定性对性价比的影响。

## Corrected Claim

该公式为特定评估场景下的自定义性价比评分模型，非行业通用标准；其逻辑结构合理（吞吐量与质量正向，TCO与可靠性负向），但具体权重与形式需依据特定业务需求定义。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了父节点公式中 Reliability_Factor 的估算逻辑以及 TCO_5Year 中部分维护成本（硬件更换、人工）的计算，完全缺失了公式中核心的 Throughput_TPS（吞吐量）、Quality_Score（质量/精度）以及 TCO_5Year 中的主要成本项（硬件折旧、电力成本）。因此，子节点未能涵盖父节点定义的所有关键方面，不具备完备性。）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/337708438&rut=381ca795da54d17e718f8a76e4f9f79f13e8d815ed1c4b0bd8b536d3e8426c7b', 'type': 'ddg', 'title': '一文搞懂高并发性能指标：QPS、TPS、RT、并发数、吞吐量'}
