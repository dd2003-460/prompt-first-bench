# N184: 负相关对 ΔH 的净效应分解：将 ΔH 分解为频率匹配增益 G_freq = (H_LFU_freq - H_LRU_freq) 和大小匹配损失 L_size 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

负相关对 ΔH 的净效应分解：将 ΔH 分解为频率匹配增益 G_freq = (H_LFU_freq - H_LRU_freq) 和大小匹配损失 L_size = (L_LFU_size - L_LRU_size)，量化 ρ=-0.3 下 G_freq 与 L_size 的耦合关系及正负抵消效应。

## Corrected Claim

负相关对 ΔH 的净效应分解：将 ΔH 分解为频率匹配增益 G_freq = (H_LFU_freq - H_LRU_freq) 和大小匹配损失 L_size = (L_LFU_size - L_LRU_size)，量化 ρ=-0.3 下 G_freq 与 L_size 的耦合关系及正负抵消效应。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了基于LFU与LRU性能差异的分解项（G_freq和L_size），并描述了在特定相关系数下的耦合分析框架，逻辑自洽且符合缓存替换算法性能分析的常规方法论。
