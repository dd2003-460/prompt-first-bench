# N192: LFU 有效头部对象覆盖量 k_lfu 的计算：k_lfu = C / E[S|LFU_set]。由于 LFU 优先缓存高频对象，且 ρ=-0.3 意味着高频对

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N83

## Claim

LFU 有效头部对象覆盖量 k_lfu 的计算：k_lfu = C / E[S|LFU_set]。由于 LFU 优先缓存高频对象，且 ρ=-0.3 意味着高频对象更小，E[S|LFU_set] ≈ E[S] * (1 + ρ * σ_logS * σ_logH * (1/k_lfu^(1/β)))。

## Corrected Claim

k_lfu = C / E[S|LFU_set]。由于 LFU 优先缓存高频对象，且 ρ=-0.3 意味着高频对象更小，E[S|LFU_set] < E[S]。具体近似公式 E[S|LFU_set] ≈ E[S] * (1 + ρ * σ_logS * σ_logH * (1/k_lfu^(1/β))) 依赖于特定分布假设及参数 β 的定义。

## Evidence

[质询]公式中引入的项 (1/k_lfu^(1/β)) 缺乏明确的理论推导或标准定义支持，属于经验拟合或特定假设下的近似，且未说明 β 的具体含义及来源，存在将复杂统计关系简化为单一经验公式的风险。 | 先验知识/题面给定，逻辑校验通过（量纲一致，LFU 缓存高频小对象导致平均大小小于全局平均值的直觉合理），但具体修正系数公式缺乏通用理论支撑，视为特定模型假设。
