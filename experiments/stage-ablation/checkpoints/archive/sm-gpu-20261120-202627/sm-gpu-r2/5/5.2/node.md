# N26: 工作点 B（数据中心基准/专业级）：1× NVIDIA A100 80GB 或 L40S 48GB。性能指标：BF16 下 Qwen3-27B 推理吞吐量约为 

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

工作点 B（数据中心基准/专业级）：1× NVIDIA A100 80GB 或 L40S 48GB。性能指标：BF16 下 Qwen3-27B 推理吞吐量约为 40-60 tokens/s [待核验]，显存充足支持 BF16 全精度推理，无需量化导致的精度损失论证。

## Corrected Claim

工作点 B（数据中心基准/专业级）：1× NVIDIA A100 80GB 或 L40S 48GB。显存充足支持 BF16 全精度推理，无需量化导致的精度损失论证。在典型推理框架（如 vLLM）及适中 Batch Size 下，Qwen3-27B 的 BF16 推理吞吐量通常在数十 tokens/s 量级（具体数值依配置而异）。

## Evidence

[质询]吞吐量数值（40-60 tokens/s）属于经验事实，且受具体推理框架（如 vLLM/TensorRT-LLM）、Batch Size、序列长度及硬件驱动版本影响极大，单一数值区间缺乏特定上下文支撑，存在口径混淆风险。 | source=knowledge，逻辑自洽（A100/L40S 显存足以承载 27B BF16 模型，无需量化），但吞吐量具体数值为经验事实，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

NVIDIA A100 L40S Qwen 27B inference benchmark tokens per second
