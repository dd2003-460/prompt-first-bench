# N362: Apple M3 Ultra 整机在 LLM 推理负载下的平均功耗 P_avg 约为 100-120W（峰值 145W，依据 Apple 官方 Mac Stud

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N122

## Claim

Apple M3 Ultra 整机在 LLM 推理负载下的平均功耗 P_avg 约为 100-120W（峰值 145W，依据 Apple 官方 Mac Studio 功耗曲线及第三方实测，推理负载下 CPU/GPU 协同效率高于峰值），而 RTX 4090 在同等推理负载下 P_avg 约为 315-360W（TDP 450W * 0.7-0.8）。

## Corrected Claim

Apple M3 Ultra 整机在 LLM 推理负载下的平均功耗估计在 100-120W 区间，而 RTX 4090 在同等负载下平均功耗估计在 315-360W 区间，具体数值需依据实际测试环境确定。

## Evidence

[质询]RTX 4090 在 LLM 推理负载下的平均功耗估算（315-360W）缺乏具体实测数据支持，且 0.7-0.8 的负载系数为经验性假设，不同模型和批次大小下波动较大；Apple M3 Ultra 的功耗数据同样缺乏本轮检索的直接来源佐证。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Mac Studio M3 Ultra power consumption LLM inference average watts vs RTX 4090
