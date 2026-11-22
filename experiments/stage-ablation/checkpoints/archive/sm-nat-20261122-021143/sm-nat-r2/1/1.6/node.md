# N11: LRU 命中率偏差项：经典 LRU 假设时间局部性，但 Pareto(β=0.9) 的长尾导致 '扫描效应'（scan effect），即大量冷对象被频繁换入换

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

LRU 命中率偏差项：经典 LRU 假设时间局部性，但 Pareto(β=0.9) 的长尾导致 '扫描效应'（scan effect），即大量冷对象被频繁换入换出，实际命中率低于理想下界，偏差量 Δ ≈ (N - K) / N * (1 - H_ideal)，需通过 Belady 算法或仿真校正

## Corrected Claim

LRU 命中率偏差项：经典 LRU 假设时间局部性，但 Pareto(β=0.9) 的长尾导致 '扫描效应'（scan effect），即大量冷对象被频繁换入换出，实际命中率低于理想下界（如 Belady 算法）。偏差量 Δ 取决于访问序列的局部性结构，通常需通过 Belady 算法或仿真校正，而非简单的 (N - K) / N * (1 - H_ideal) 公式。

## Evidence

[质询]公式 Δ ≈ (N - K) / N * (1 - H_ideal) 缺乏严谨的理论推导支持，且量纲/逻辑存疑：(N-K)/N 是冷对象占比，(1-H_ideal) 是理想未命中率，两者相乘作为“偏差量”在数学上并不直接对应 LRU 与理想算法（如 Belady）之间的命中率差值（通常偏差取决于访问序列的具体局部性结构，而非简单的冷对象比例乘以理想未命中率）。此外，Pareto(β=0.9) 的长尾确实会导致扫描效应，但具体的偏差公式并非标准教科书结论，属于经验性或特定模型下的近似，缺乏通用性。 | 先验知识/题面给定，逻辑校验发现公式推导不严谨，偏差项的具体数学形式缺乏普遍成立的理论依据，属于特定场景下的近似或错误表述。

## Search Query

LRU scan effect long tail cache performance
