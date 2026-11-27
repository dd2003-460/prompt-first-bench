# N25: 工作点 A（极致性价比/消费级）：2× RTX 4090 (24GB) + NVLink/PCIe。性能指标：FP16/BF16 下 Qwen3-27B 推理吞

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

工作点 A（极致性价比/消费级）：2× RTX 4090 (24GB) + NVLink/PCIe。性能指标：FP16/BF16 下 Qwen3-27B 推理吞吐量约为 15-25 tokens/s [待核验]，单卡内存容量 24GB 满足 32K 上下文需求（需量化至 INT8/FP8 以适配显存）。

## Corrected Claim

工作点 A（极致性价比/消费级）：2× RTX 4090 (24GB) + NVLink/PCIe。性能指标：FP16/BF16 下 Qwen3-27B 推理吞吐量约为 15-25 tokens/s [待核验]，单卡内存容量 24GB 需量化至 INT4 以适配 32K 上下文显存需求（INT8/FP8 显存不足）。

## Evidence

[质询]吞吐量数值（15-25 tokens/s）缺乏具体硬件配置（如PCIe版本、是否启用TensorRT-LLM等优化）和软件栈说明，且24GB显存运行27B模型在32K上下文下通常需INT4量化而非INT8/FP8（INT8约需54GB+KV Cache，远超24GB），存在显存容量与量化精度逻辑矛盾。 | 先验知识/题面给定，逻辑校验发现显存容量与量化精度不匹配（27B INT8需~54GB，24GB显存无法容纳32K上下文），且吞吐量数值缺乏具体优化条件支持，属经验事实且存在内部矛盾。

## Search Query

2x RTX 4090 Qwen 27B inference tokens per second benchmark
