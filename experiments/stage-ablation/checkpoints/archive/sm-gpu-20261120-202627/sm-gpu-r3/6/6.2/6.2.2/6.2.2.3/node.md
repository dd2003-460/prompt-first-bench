# N403: LLM 推理负载下的平均功耗修正系数 (Alpha) 定义：Alpha = P_avg / TDP，对于 A100 和 L40S 在 BF16 推理场景下，Al

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

LLM 推理负载下的平均功耗修正系数 (Alpha) 定义：Alpha = P_avg / TDP，对于 A100 和 L40S 在 BF16 推理场景下，Alpha 通常取值 0.6-0.8，该系数用于从 TDP 估算 OpEx_energy，需根据具体 GPU 利用率曲线验证。

## Corrected Claim

LLM 推理负载下的平均功耗修正系数 (Alpha) 定义：Alpha = P_avg / TDP，对于 A100 和 L40S 在 BF16 推理场景下，Alpha 通常取值 0.6-0.8，该系数用于从 TDP 估算 OpEx_energy，需根据具体 GPU 利用率曲线验证。

## Evidence

先验知识/题面给定，逻辑校验通过
