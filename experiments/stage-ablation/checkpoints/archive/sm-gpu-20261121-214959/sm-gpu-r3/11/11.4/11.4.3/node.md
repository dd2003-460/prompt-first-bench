# N346: A100 (Ampere) 的 Tensor Core 不支持原生 FP8 数据格式，仅支持 BF16/TF32/INT8。若在 A100 上运行 FP8 权重

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

A100 (Ampere) 的 Tensor Core 不支持原生 FP8 数据格式，仅支持 BF16/TF32/INT8。若在 A100 上运行 FP8 权重，软件栈 (如 vLLM) 必须在加载时反量化为 BF16，导致显存占用从 27GB 增加至 54GB，且计算速度无增益，仅保留存储节省 (若磁盘空间受限)。

## Corrected Claim

A100 (Ampere) 的 Tensor Core 不支持原生 FP8 数据格式，仅支持 BF16/TF32/INT8。若在 A100 上运行 FP8 权重，软件栈 (如 vLLM) 必须在加载时反量化为 BF16，导致显存占用从 27GB 增加至 54GB，且计算速度无增益，仅保留存储节省 (若磁盘空间受限)。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 (Ampere架构) 确实不支持原生FP8 Tensor Core运算（FP8支持始于Hopper架构H100），因此FP8权重需反量化为BF16进行计算，显存占用翻倍（27GB->54GB）符合逻辑。
