# N8: 显存占用模型：总显存消耗 = (27B params × 4-bit quant size ≈ 13.5GB) + (KV Cache per seq × ma

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

显存占用模型：总显存消耗 = (27B params × 4-bit quant size ≈ 13.5GB) + (KV Cache per seq × max_num_seqs(8) × max_model_len(262144)) + (Activation memory for batch) + (TP communication buffers)，其中 KV Cache 在 fp8 下约为 [待核验] GB/seq@262k，导致有效并发数远低于 max_num_seqs=8。

## Corrected Claim

显存占用模型：总显存消耗 = (27B params × 4-bit quant size ≈ 13.5GB) + (KV Cache per seq × max_num_seqs(8) × max_model_len(262144)) + (Activation memory for batch) + (TP communication buffers)，其中 KV Cache 在 fp8 下取决于模型注意力头配置，通常占据显著比例，导致有效并发数受限于显存上限。

## Evidence

[质询]KV Cache 的具体数值缺失（标记为[待核验]），且不同模型架构（如 GQA vs MHA）和实现细节会导致该数值差异巨大，无法仅凭参数规模确定唯一值。 | 先验知识/题面给定，逻辑校验通过：显存组成公式符合大模型推理通用原理，4-bit量化13.5GB计算正确（27*0.5=13.5），但KV Cache具体值需依赖特定模型配置，故降级为定性描述。
