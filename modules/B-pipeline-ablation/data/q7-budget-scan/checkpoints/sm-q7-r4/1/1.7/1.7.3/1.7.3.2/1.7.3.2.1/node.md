# N418: QD=1 到 QD=32 的功耗跃升斜率：每增加 1 个队列深度，平均功耗增加 0.2-0.3W，主要源于控制器多通道并行激活导致的静态漏电增加；公式：P(QD

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N184

## Claim

QD=1 到 QD=32 的功耗跃升斜率：每增加 1 个队列深度，平均功耗增加 0.2-0.3W，主要源于控制器多通道并行激活导致的静态漏电增加；公式：P(QD) = P_base + α * log2(QD)，其中 α ≈ 1.5W

## Corrected Claim

QD=1 到 QD=32 的功耗随队列深度增加而上升，通常遵循对数增长趋势，具体斜率和系数取决于硬件实现细节。

## Evidence

[质询]该陈述包含具体的经验参数（斜率0.2-0.3W、系数α≈1.5W）和特定的物理归因（静态漏电为主），这些属于特定硬件架构下的经验事实，无法从第一性原理严格推导，且缺乏来源支持其具体数值和因果机制的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

NVMe SSD power consumption vs queue depth QD1 to QD32 logarithmic model
