# N16: LRU 稳态字节命中率下界的理论公式：H_byte = 1 - (C / S_total)^(α-1) * f(β, α)，其中 C=128GB 缓存容量，S_

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

LRU 稳态字节命中率下界的理论公式：H_byte = 1 - (C / S_total)^(α-1) * f(β, α)，其中 C=128GB 缓存容量，S_total 为对象总大小，f(β, α) 为热度-大小耦合修正因子；该公式源自 LRU 在 Zipf-like 负载下的渐近分析，属 knowledge 来源，但耦合因子 f 的具体形式需核验。

## Corrected Claim

LRU 稳态字节命中率下界的理论公式通常表示为 H_byte ≈ 1 - (C / S_total)^(α-1) * f(β, α)，其中 f(β, α) 为热度-大小耦合修正因子，具体形式取决于负载模型假设。

## Evidence

[质询]公式中耦合因子 f(β, α) 的具体形式未定义，且 LRU 在 Zipf 负载下的稳态命中率通常依赖于请求频率分布与对象大小的联合分布，简单的幂律形式 (C/S)^(α-1) 仅在特定假设（如大小与热度独立或特定耦合）下成立，缺乏通用性证明。 | 先验知识/题面给定，逻辑校验通过，但耦合因子 f 的具体形式需核验，且无外部来源支持该特定公式形式。

## Search Query

LRU steady-state byte hit rate Pareto distribution formula
