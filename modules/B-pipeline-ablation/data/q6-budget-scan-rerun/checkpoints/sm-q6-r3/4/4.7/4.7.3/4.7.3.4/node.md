# N318: 故障窗口内加权P99劣化幅度计算公式：ΔP99_Worst = (Effective_Downtime / Total_Duration) * (Origin_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N123

## Claim

故障窗口内加权P99劣化幅度计算公式：ΔP99_Worst = (Effective_Downtime / Total_Duration) * (Origin_Latency_P99 - Normal_P99)。若Effective_Downtime=300s（自建），Total_Duration=86400s（日），Origin_Latency_P99=500ms，Normal_P99=50ms，则ΔP99_Worst ≈ (300/86400) * 450ms ≈ 1.56ms（日均影响），但瞬时P99在故障期间为500ms。

## Corrected Claim

故障窗口内加权P99劣化幅度计算公式：ΔP99_Worst = (Effective_Downtime / Total_Duration) * (Origin_Latency_P99 - Normal_P99)。若Effective_Downtime=300s（自建），Total_Duration=86400s（日），Origin_Latency_P99=500ms，Normal_P99=50ms，则ΔP99_Worst ≈ (300/86400) * 450ms ≈ 1.56ms（日均影响），但瞬时P99在故障期间为500ms。

## Evidence

先验知识/题面给定，逻辑校验通过：公式为加权平均劣化的标准定义，数值计算 (300/86400)*450 ≈ 1.5625 正确，量纲一致。
