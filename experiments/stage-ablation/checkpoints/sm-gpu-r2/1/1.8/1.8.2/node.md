# N57: BF16 精度下，Qwen3-27B 在 H100 80GB 上的实测吞吐量（batch=1）通常在 50-80 tokens/s 之间，基于 vLLM 或 T

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

BF16 精度下，Qwen3-27B 在 H100 80GB 上的实测吞吐量（batch=1）通常在 50-80 tokens/s 之间，基于 vLLM 或 TensorRT-LLM 官方基准测试数据，与理论极限偏差 <10%。

## Corrected Claim

BF16 精度下，Qwen3-27B 在 H100 80GB 上的实测吞吐量（batch=1）通常在数十 tokens/s 量级，具体数值取决于序列长度及推理引擎配置。

## Evidence

[质询]具体吞吐量数值（50-80 tokens/s）及偏差比例（<10%）属于经验事实，且不同序列长度、硬件驱动版本及具体配置下波动较大，缺乏统一官方基准直接支持该精确区间。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B H100 BF16 inference throughput tokens per second
