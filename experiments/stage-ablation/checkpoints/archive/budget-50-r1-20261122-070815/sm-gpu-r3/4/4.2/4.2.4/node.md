# N108: Apple Mac Studio M2 Ultra (192GB) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 300W (M2 Ultra TDP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

Apple Mac Studio M2 Ultra (192GB) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 300W (M2 Ultra TDP 250W + 系统开销 ~20%)，其统一内存架构下无独立显存功耗项

## Corrected Claim

Apple Mac Studio M2 Ultra (192GB) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 300W (M2 Ultra TDP 250W + 系统开销 ~20%)，其统一内存架构下无独立显存功耗项

## Evidence

[质询]M2 Ultra 的 TDP 通常指最大热设计功耗，实际 LLM 推理负载下的平均功耗可能低于 250W，且 300W 的整机功耗估算可能略高，但量级合理。 | 先验知识/题面给定，逻辑校验通过：M2 Ultra 芯片功耗在 200-250W 范围内，加上系统其他组件（风扇、SSD、主板等）开销，整机 300W 是合理的工程估算值；统一内存架构确实无独立显存功耗项。
