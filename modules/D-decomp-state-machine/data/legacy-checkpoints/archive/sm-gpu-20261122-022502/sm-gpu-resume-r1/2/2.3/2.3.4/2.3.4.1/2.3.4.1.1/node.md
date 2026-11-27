# N629: Mac Studio M2 Ultra 在运行 Qwen3-27B (INT8/FP8) 推理负载时，GPU 占用率平均为 85%-95%，导致整机功耗稳定在 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N194

## Claim

Mac Studio M2 Ultra 在运行 Qwen3-27B (INT8/FP8) 推理负载时，GPU 占用率平均为 85%-95%，导致整机功耗稳定在 165W-185W 区间，取 175W 为保守平均值。

## Corrected Claim

Mac Studio M2 Ultra 在运行 Qwen3-27B (INT8/FP8) 推理负载时，GPU 占用率通常较高，整机功耗可能在 150W-200W 区间波动，具体数值取决于负载强度和散热条件。

## Evidence

[质询]该陈述包含具体的硬件功耗数值（165W-185W）和GPU占用率（85%-95%），属于经验事实。在缺乏具体测试环境（如是否开启风扇、环境温度、具体推理框架、并发数）的情况下，直接断言“稳定”在该区间且取175W为保守平均值，存在将特定测试场景泛化为通用事实的风险，且无来源支持该具体数值。 | 经验事实，逻辑自洽但缺来源支持。M2 Ultra TDP约为120W-150W，整机功耗175W在物理上合理（含CPU、内存、风扇等开销），但具体数值无法从第一性原理推出，且检索无可用来源。

## Search Query

Mac Studio M2 Ultra LLM inference power consumption watts benchmark
