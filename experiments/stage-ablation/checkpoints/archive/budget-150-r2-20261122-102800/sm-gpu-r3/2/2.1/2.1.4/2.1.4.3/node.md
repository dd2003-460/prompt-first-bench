# N219: W4 量化下 Embedding 层保持 BF16 的原因不仅是精度，还因为 Embedding 查表操作 (Gather) 在 INT4/W4 格式下缺乏高效

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

W4 量化下 Embedding 层保持 BF16 的原因不仅是精度，还因为 Embedding 查表操作 (Gather) 在 INT4/W4 格式下缺乏高效的 GPU Kernel 支持，导致 Embedding 层计算延迟可能比 BF16 增加 20-30%，抵消了显存节省带来的部分吞吐提升。

## Corrected Claim

W4 量化下 Embedding 层保持 BF16 的原因不仅是精度，还因为 Embedding 查表操作 (Gather) 在 INT4/W4 格式下缺乏高效的 GPU Kernel 支持，可能导致计算延迟增加，从而抵消部分显存节省带来的吞吐提升。

## Evidence

[质询]具体数值（20-30%延迟增加）缺乏通用性，高度依赖硬件架构（如H100 vs A100）和具体Kernel实现（如是否使用CUDA Graph或特定优化库），将其作为普遍事实陈述存在以偏概全的风险。 | 经验事实，逻辑自洽（Embedding Gather操作在低精度下确实存在Kernel支持不足的问题，导致计算开销增加），但缺来源支持具体数值。

## Search Query

LLM quantization embedding layer gather kernel overhead W4 vs BF16
