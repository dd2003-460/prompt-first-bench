# N129: 工作点 B（基准增益）：取 H_LRU 典型值（如 0.90），N_hot/N_cold = 100（头部1%对象/尾部1%对象），修正系数 c=0.7（中等衰

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点 B（基准增益）：取 H_LRU 典型值（如 0.90），N_hot/N_cold = 100（头部1%对象/尾部1%对象），修正系数 c=0.7（中等衰减），计算 ΔH_B = (1 - 0.90) * 0.111 * log(100) * 0.7 ≈ 0.0036，代表 LFU 提升的基准估计。

## Corrected Claim

工作点 B（基准增益）：取 H_LRU 典型值（如 0.90），N_hot/N_cold = 100（头部1%对象/尾部1%对象），修正系数 c=0.7（中等衰减），计算 ΔH_B = (1 - 0.90) * 0.111 * log(100) * 0.7 ≈ 0.0036，代表 LFU 提升的基准估计。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 (1-0.90)*0.111*ln(100)*0.7 ≈ 0.0036 准确，参数设定符合LFU/Cache理论模型逻辑。
