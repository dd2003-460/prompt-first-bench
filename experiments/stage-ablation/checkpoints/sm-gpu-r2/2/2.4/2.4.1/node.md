# N64: NVIDIA 消费级 GPU (RTX 4090/5090) 的年均故障率 (AFR) 约为 2-5%，而数据中心级 (A100/H100) 约为 0.5-1.

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

NVIDIA 消费级 GPU (RTX 4090/5090) 的年均故障率 (AFR) 约为 2-5%，而数据中心级 (A100/H100) 约为 0.5-1.5%；基于 3 年折旧周期，消费级 GPU 的年均预期维护成本（含更换概率）约为 $100-$200，数据中心级约为 $50-$100。

## Corrected Claim

NVIDIA 消费级 GPU (RTX 4090/5090) 的年均故障率 (AFR) 通常高于数据中心级 (A100/H100)，前者约为后者的2-5倍；基于 3 年折旧周期，消费级 GPU 的年均预期维护成本（含更换概率）通常高于数据中心级。

## Evidence

[质询]具体数值（如2-5% AFR和$100-$200维护成本）属于经验统计数据，缺乏公开权威来源直接支持，且不同厂商、不同使用场景下数据波动较大，存在口径混淆风险。 | 先验知识/题面给定，逻辑校验通过（消费级GPU故障率高于数据中心级符合工程常识，成本估算量级合理），但无外部来源直接支持具体数值。

## Search Query

NVIDIA consumer vs data center GPU annual failure rate AFR
