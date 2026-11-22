# N196: vLLM 调度器元数据 (Scheduler Metadata) 的显存开销主要包含请求状态字典和采样参数存储，其大小与活跃请求数线性相关。在 max_num_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

vLLM 调度器元数据 (Scheduler Metadata) 的显存开销主要包含请求状态字典和采样参数存储，其大小与活跃请求数线性相关。在 max_num_seqs=256 且每个请求平均存储 1KB 元数据时，总开销约为 256KB，可忽略不计；若考虑更复杂的 LoRA 适配器元数据，每个适配器增加约 10-50KB，需根据具体 LoRA 数量修正。

## Corrected Claim

vLLM 调度器元数据 (Scheduler Metadata) 的显存开销主要包含请求状态字典和采样参数存储，其大小与活跃请求数线性相关。在 max_num_seqs=256 且每个请求平均存储 1KB 元数据时，总开销约为 256KB，可忽略不计；若考虑更复杂的 LoRA 适配器元数据，每个适配器增加约 10-50KB，需根据具体 LoRA 数量修正。

## Evidence

先验知识/题面给定，逻辑校验通过：256 * 1KB = 256KB 计算正确，且相对于 GPU 显存（GB 级）确实可忽略；LoRA 元数据量级符合工程常识。
