# N9: 数据中心级GPU候选集包含H100 SXM (80GB) 和 A100 SXM (80GB)，因为H100提供900GB/s HBM3带宽和NVLink互联，A

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

数据中心级GPU候选集包含H100 SXM (80GB) 和 A100 SXM (80GB)，因为H100提供900GB/s HBM3带宽和NVLink互联，A100提供800GB/s HBM2e带宽，两者均支持FP8/INT8加速，是单卡部署27B模型的标准选择；H800/A800因出口限制不纳入主流性价比比较。

## Corrected Claim

数据中心级GPU候选集包含H100 SXM (80GB) 和 A100 SXM (80GB)，因为H100提供约3.35TB/s HBM3带宽、NVLink互联及FP8/INT8加速，A100提供约2TB/s HBM2e带宽及INT8/FP16加速，两者是单卡部署27B模型的标准选择；H800/A800因出口限制不纳入主流性价比比较。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 763)

## Search Query

H100 vs A100 LLM inference cost per token
