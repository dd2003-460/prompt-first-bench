# N176: 在 TensorRT-LLM 中，Batch=1, seq_len=32K 场景下的 Activation Buffer 开销约为 1.2-1.5 GB，比 v

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

在 TensorRT-LLM 中，Batch=1, seq_len=32K 场景下的 Activation Buffer 开销约为 1.2-1.5 GB，比 vLLM 低约 30-40%，这是因为 TensorRT-LLM 对中间激活值进行了更激进的内存复用（In-place operation）和精度降级（部分中间层使用 FP16 而非 BF16/FP32）。

## Corrected Claim

在 TensorRT-LLM 中，Batch=1, seq_len=32K 场景下的 Activation Buffer 开销通常低于 vLLM，这是因为 TensorRT-LLM 对中间激活值进行了更激进的内存复用（In-place operation）和精度优化。具体开销数值（如 1.2-1.5 GB）及性能提升比例（30-40%）高度依赖于具体的模型架构（如隐藏层维度、层数）和硬件配置，并非通用固定值。

## Evidence

[质询]数值量级存疑：在 Batch=1, seq_len=32K 场景下，若模型为常见规模（如 7B-70B），仅 Attention 的 KV Cache 或中间激活值（取决于具体层数和隐藏维度）往往远超 1.2-1.5 GB。例如，对于 7B 模型，32K 序列的 KV Cache 通常就在 1-2 GB 左右（取决于 GQA 头数），而 Activation Buffer 通常指前向传播中的临时激活，其大小与 Batch 和 Seq Len 成正比，但具体数值高度依赖模型架构（Hidden Size, Num Layers）。1.2-1.5 GB 这个具体数值缺乏通用性，且“比 vLLM 低 30-40%”这一对比结论缺乏特定模型和硬件配置的前提，属于高度依赖具体实现的经验性断言，极易因模型不同而失效。 | 先验知识/题面给定，逻辑校验通过（机制描述合理，但具体数值缺乏通用性，降级为定性表述）
