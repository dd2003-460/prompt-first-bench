# N370: Qwen3-27B 在 2× RTX 4090 (PCIe 4.0) 上运行 BF16 推理时的实测平均功耗 P_avg 约为 380-420W (每卡)，需通

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117

## Claim

Qwen3-27B 在 2× RTX 4090 (PCIe 4.0) 上运行 BF16 推理时的实测平均功耗 P_avg 约为 380-420W (每卡)，需通过 nvidia-smi 或功耗监控工具在持续解码负载下采样 10 分钟以上取均值，以替换 TDP 450W 进行更精确的 OpEx 计算。

## Corrected Claim

Qwen3-27B 在 2× RTX 4090 (PCIe 4.0) 上运行 BF16 推理时的实测平均功耗 P_avg 需通过 nvidia-smi 或功耗监控工具在持续解码负载下采样 10 分钟以上取均值，以替换 TDP 450W 进行更精确的 OpEx 计算。

## Evidence

[质询]该陈述包含具体的经验性数值（380-420W），属于硬件功耗实测数据，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 average power consumption LLM inference 27B benchmark watts
