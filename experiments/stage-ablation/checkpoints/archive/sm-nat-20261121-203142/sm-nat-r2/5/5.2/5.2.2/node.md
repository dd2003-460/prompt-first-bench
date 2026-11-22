# N67: 在 ρ≈-0.3 负相关下，LFU 优先缓存热门小对象，但 LRU 因时间局部性已部分捕获该效应，实际增益 ΔH 衰减至理论上限的 30-50%，具体衰减系数 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N22

## Claim

在 ρ≈-0.3 负相关下，LFU 优先缓存热门小对象，但 LRU 因时间局部性已部分捕获该效应，实际增益 ΔH 衰减至理论上限的 30-50%，具体衰减系数 k ≈ 0.3-0.5 需通过 A/B 测试或仿真标定 [待核验：k 值无通用公式]

## Corrected Claim

在 ρ≈-0.3 负相关下，LFU 优先缓存热门小对象，但 LRU 因时间局部性已部分捕获该效应，实际增益 ΔH 通常低于理论上限；具体衰减系数 k 需通过 A/B 测试或仿真标定，无通用固定公式。

## Evidence

[质询]该陈述中的具体数值范围（30-50%）和衰减系数（k ≈ 0.3-0.5）属于经验性参数，缺乏通用理论公式支持，且未提供特定负载模型或实验条件，存在将特定场景下的观测值泛化为通用规律的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该数值非第一性原理可推导，属需实验标定的经验参数）

## Search Query

LFU vs LRU cache hit ratio improvement negative correlation object size popularity
