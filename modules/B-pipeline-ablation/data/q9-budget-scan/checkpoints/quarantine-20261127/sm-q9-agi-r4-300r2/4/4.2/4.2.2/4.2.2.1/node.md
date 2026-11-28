# N170: 科研长文本场景 MTP 接受率 η_research 的实测基准值：在 Qwen3-27B NVFP4 部署下，针对 10k-50k token 长度的文献综述

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

科研长文本场景 MTP 接受率 η_research 的实测基准值：在 Qwen3-27B NVFP4 部署下，针对 10k-50k token 长度的文献综述/假设生成任务，η_research 的均值及置信区间（需通过 vLLM 监控日志中 spec_decode_accept_rate 指标获取，预期范围 0.60-0.75）

## Corrected Claim

在 Qwen3-27B NVFP4 部署下，针对 10k-50k token 长度的文献综述/假设生成任务，MTP 接受率 η_research 的具体均值及置信区间需通过 vLLM 监控日志中 spec_decode_accept_rate 指标实测获取，目前缺乏公开的实测基准数据支持 0.60-0.75 这一预期范围。

## Evidence

[质询]该陈述声称拥有“实测基准值”并给出了具体的均值及置信区间预期范围（0.60-0.75），但这属于特定硬件（NVFP4）、特定模型（Qwen3-27B）和特定任务（10k-50k token科研长文本）下的经验性统计数据。此类数据无法从第一性原理推导，且当前无任何参考来源支持该具体数值范围，存在将推测或未经证实的经验值当作既定事实的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值范围0.60-0.75的真实性）

## Search Query

vLLM speculative decoding acceptance rate scientific text generation benchmark Qwen3
