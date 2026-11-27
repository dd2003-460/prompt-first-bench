# N187: A100 80GB 在 27B BF16 推理下的显存占用为 54GB (27GB 权重 + 1.93GB KV + 1GB 激活 + 冗余缓冲)，剩余 26G

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

A100 80GB 在 27B BF16 推理下的显存占用为 54GB (27GB 权重 + 1.93GB KV + 1GB 激活 + 冗余缓冲)，剩余 26GB 可用于扩展上下文至 64K 或支持 Batch Size=2，其单 Token 能耗约为 0.5-0.8 J/token，相比消费级卡 (1.5-2.0 J/token) 能效高 2-3 倍。

## Corrected Claim

A100 80GB 在 27B BF16 推理下的显存占用约为 54GB 权重加上 KV Cache 及激活值开销，剩余显存可用于扩展上下文或支持小批量推理；其能效通常优于消费级显卡，但具体单 Token 能耗需视负载条件而定。

## Evidence

[质询]单Token能耗数值（0.5-0.8 J/token）缺乏具体负载条件（如序列长度、Batch Size、利用率）支撑，且与消费级卡对比的能效倍数属于经验性估算，不同测试场景下波动较大，易产生误导。 | 显存占用计算逻辑自洽（27B BF16权重约54GB，加上KV Cache和激活值后接近80GB上限，剩余空间估算合理），但能耗数据为经验事实，检索无可用来源支持，依据经验事实排除条款降级。

## Search Query

NVIDIA A100 80GB energy efficiency tokens per watt LLM inference
