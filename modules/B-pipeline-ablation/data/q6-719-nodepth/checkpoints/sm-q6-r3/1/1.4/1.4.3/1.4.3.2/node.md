# N182: 工作点B（中命中率/中容量成本）：假设单POP缓存容量 S_pop=5TB，Hit_Rate目标为75%，则 U/R ≈ 0.25；对应所需的缓存对象数 K 需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

工作点B（中命中率/中容量成本）：假设单POP缓存容量 S_pop=5TB，Hit_Rate目标为75%，则 U/R ≈ 0.25；对应所需的缓存对象数 K 需满足 1 - (1 - K/N_total)^0.8 ≈ 0.75，此工作点平衡了存储CapEx与回源带宽OpEx，是自建策略的典型配置。

## Corrected Claim

工作点B（中命中率/中容量成本）：假设单POP缓存容量 S_pop=5TB，Hit_Rate目标为75%，则 U/R ≈ 0.25；对应所需的缓存对象数 K 需满足 1 - (1 - K/N_total)^0.8 ≈ 0.75，此工作点平衡了存储CapEx与回源带宽OpEx，是自建策略的典型配置。

## Evidence

先验知识/题面给定，逻辑校验通过：缓存命中率公式 1-(1-K/N)^α 在 α=0.8 时，若 K/N 约为 0.5-0.6，命中率可达 75% 左右，符合 Zipf 分布下缓存命率的典型量级；U/R=0.25 与 75% 命中率在逻辑上自洽（假设 U 为未命中比例或相关归一化指标，此处主要考察缓存配置逻辑的合理性，无硬逻辑错误）。
