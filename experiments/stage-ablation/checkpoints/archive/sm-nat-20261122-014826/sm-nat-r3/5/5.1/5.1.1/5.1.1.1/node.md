# N135: 在 β=0.9 (Zipf) 和 C/S=0.14 条件下，LRU 字节命中率 H_LRU_base 的精确解析解为 H_LRU_base ≈ 1 - (1 -

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N50

## Claim

在 β=0.9 (Zipf) 和 C/S=0.14 条件下，LRU 字节命中率 H_LRU_base 的精确解析解为 H_LRU_base ≈ 1 - (1 - 0.14)^(1/0.9) ≈ 1 - 0.86^1.111 ≈ 1 - 0.846 = 0.154 (15.4%)，此为未考虑大小-热度相关性的基准值。

## Corrected Claim

在特定简化模型假设下（H = 1 - (1 - C/S)^(1/β)），当 β=0.9 和 C/S=0.14 时，计算得出的基准命中率约为 15.4%。

## Evidence

[质询]该公式 H = 1 - (1 - C/S)^(1/β) 并非 LRU 在 Zipf 分布下的标准解析解。标准 Zipf-LRU 模型通常涉及更复杂的积分或近似（如基于访问频率的累积分布），且 C/S (Cache-to-Server ratio) 与命中率的关系通常不是简单的幂律倒数关系。该公式看起来像是某种特定简化模型或经验拟合，而非通用的“精确解析解”。 | source=knowledge，逻辑自洽（数值计算 1-0.86^(1/0.9) ≈ 0.154 正确），但该公式作为“精确解析解”缺乏通用理论支持，属于特定模型假设下的推导，故降级为定性/特定模型表述。
