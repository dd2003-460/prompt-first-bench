# N238: ONNX Runtime + NPU 方案中，模型导出至 ONNX 格式的适配工时下限 10 人天包含：Qwen3-27B 模型结构解析 (2 天)、RoPE 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91

## Claim

ONNX Runtime + NPU 方案中，模型导出至 ONNX 格式的适配工时下限 10 人天包含：Qwen3-27B 模型结构解析 (2 天)、RoPE 位置编码算子的手动 ONNX 节点实现 (3 天)、特定 Attention 变体（如 FlashAttention）的算子拆分与重写 (5 天)。

## Corrected Claim

ONNX Runtime + NPU 方案中，模型导出至 ONNX 格式的适配工时通常包含：Qwen3-27B 模型结构解析、RoPE 位置编码算子的手动 ONNX 节点实现、特定 Attention 变体（如 FlashAttention）的算子拆分与重写等关键步骤，具体人天需根据团队熟练度与工具链支持情况评估。

## Evidence

[质询]具体的人天估算（2+3+5=10）属于高度依赖团队经验、工具链成熟度及具体模型变体细节的经验性工程评估，而非客观固定的物理或数学常数。不同团队或不同版本的ONNX Runtime支持程度可能导致工时显著波动，该数值缺乏普适性。 | source=knowledge，逻辑自洽（各分项工时之和等于总工时，且任务分解符合ONNX适配常见难点），但具体数值为经验估计，无外部来源直接支持，依据经验事实排除条款降级。
