# N311: AMD Radeon PRO W7900 在 LLM 推理负载下的平均功耗 P_avg_W7900 并非恒定 TDP，而是随显存带宽利用率波动；基于 576 G

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N106

## Claim

AMD Radeon PRO W7900 在 LLM 推理负载下的平均功耗 P_avg_W7900 并非恒定 TDP，而是随显存带宽利用率波动；基于 576 GB/s 带宽瓶颈，Decode 阶段功耗预计为 250-300W，保守取 280W 用于 TCO 计算，修正原 N106 中 350W 的高估。

## Corrected Claim

AMD Radeon PRO W7900 在 LLM 推理负载下的平均功耗随显存带宽利用率波动，Decode 阶段功耗预计低于 TDP，具体数值需依据实测数据确定，原 350W 估值可能偏高。

## Evidence

[质询]该陈述包含具体的硬件功耗数值（250-300W, 280W）和带宽参数（576 GB/s），属于经验事实。虽然逻辑上功耗随负载波动是合理的，但具体的数值区间和“修正原N106”的对比缺乏外部来源支持，且576 GB/s并非W7900的标准公开标称带宽（通常为HBM2e，带宽更高，如1.6TB/s+，此处576GB/s可能指有效带宽或特定瓶颈下的数值，存在口径混淆风险）。 | 经验事实，逻辑自洽但缺来源支持；source=knowledge节点，但具体数值缺乏直接证据，且带宽数值存疑，故降级。
