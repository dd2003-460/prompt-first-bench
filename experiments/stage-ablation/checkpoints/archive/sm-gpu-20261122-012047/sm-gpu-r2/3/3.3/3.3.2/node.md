# N101: GPTQ 与 AWQ 两种 INT4 量化方案在 Qwen3-27B 上的吞吐量差异约为 5%-10%：AWQ 通常略快，因为它仅量化重要权重（Activati

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

GPTQ 与 AWQ 两种 INT4 量化方案在 Qwen3-27B 上的吞吐量差异约为 5%-10%：AWQ 通常略快，因为它仅量化重要权重（Activation-aware Weight Quantization），反量化路径更短；GPTQ 量化所有权重，计算开销稍大。在 RTX 4090 上，AWQ-INT4 吞吐量约为 28-30 tokens/s，GPTQ-INT4 约为 25-27 tokens/s。

## Corrected Claim

GPTQ 与 AWQ 两种 INT4 量化方案在 Qwen3-27B 上的吞吐量差异通常较小（约 0%-10%）：AWQ 通常略快或持平，因为它采用激活感知量化并通常配备更优化的反量化内核；GPTQ 量化所有权重，性能取决于具体推理框架的算子实现。在 RTX 4090 上，两者吞吐量均处于同一量级（约 20-35 tokens/s，具体取决于 Batch Size 和框架），AWQ 可能具有轻微优势。

## Evidence

[质询]具体吞吐量数值（28-30 vs 25-27 tokens/s）属于高度依赖硬件驱动、推理框架（如vLLM/TensorRT-LLM版本）、Batch Size及序列长度的经验事实，且Qwen3-27B为较新模型，缺乏通用基准数据支持该精确区间；此外，GPTQ与AWQ在INT4下的性能差异主要取决于反量化算子优化程度，而非简单的'量化所有权重'导致的计算开销，5%-10%的差异范围在不同环境下波动极大，可能为0%甚至反转。 | source=knowledge，逻辑自洽（AWQ通常因激活感知量化和更高效的反量化内核而略快），但具体吞吐量数值为经验事实，无外部来源支持，且数值精度过高，故降级为定性表述。

## Search Query

AWQ vs GPTQ INT4 inference latency comparison LLM
