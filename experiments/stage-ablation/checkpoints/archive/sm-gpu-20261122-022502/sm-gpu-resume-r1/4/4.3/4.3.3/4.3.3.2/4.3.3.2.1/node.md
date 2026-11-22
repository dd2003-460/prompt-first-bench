# N832: H200 SXM 的实际 TDP 功耗为 700W，但在高负载推理（Qwen3-27B BF16）下的平均功耗约为 550W-600W（基于 NVIDIA 官方

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N260

## Claim

H200 SXM 的实际 TDP 功耗为 700W，但在高负载推理（Qwen3-27B BF16）下的平均功耗约为 550W-600W（基于 NVIDIA 官方 H200 datasheet 及第三方实测基准测试 [search]），导致年 OpEx 从 $6,132 降至约 $4,885-$5,622。

## Corrected Claim

H200 SXM 的 TDP 功耗为 700W，在高负载推理场景下平均功耗通常低于 TDP（具体数值需依据实测数据，此处暂估为 550W-600W），相应地年 OpEx 预计从 $6,132 降至约 $4,885-$5,622（基于特定电价和负载假设）。

## Evidence

[质询]H200 SXM 的 TDP 700W 是硬件规格（经验事实），且特定模型（Qwen3-27B）在特定精度（BF16）下的平均功耗 550W-600W 属于高度依赖具体部署环境、并发量和硬件配置的实测数据，无法从第一性原理推导，且当前无可用来源支持该具体数值区间。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体功耗数值及对应的 OpEx 计算细节）。

## Search Query

H200 SXM average power consumption inference benchmark watts
