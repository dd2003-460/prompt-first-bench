# N60: NVIDIA L40S (48GB) 推理性能基准：Qwen3-27B INT8 单卡吞吐 35 tokens/s (batch=1)，显存 48GB 可容纳 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

NVIDIA L40S (48GB) 推理性能基准：Qwen3-27B INT8 单卡吞吐 35 tokens/s (batch=1)，显存 48GB 可容纳 INT8 权重 (27GB) + 32K KV cache (1.6GB) + 框架开销 (5GB) 余量 14.4GB；无 FP8 硬件加速，FP8 性能回退到 INT8 水平

## Corrected Claim

NVIDIA L40S (48GB) 推理性能基准：Qwen3-27B INT8 单卡吞吐约 30-40 tokens/s (batch=1)，显存 48GB 可容纳 INT8 权重 (27GB) + 32K KV cache (1.6GB) + 框架开销 (5GB) 余量约 14.4GB；无 FP8 硬件加速，FP8 性能回退到 INT8 水平

## Evidence

[质询]具体吞吐数值（35 tokens/s）和显存余量计算（14.4GB）属于经验事实，缺乏来源支持，且不同框架/驱动版本下性能波动较大，单一数值可能不准确。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

L40S Qwen3-27B INT8 inference 48GB memory benchmark
