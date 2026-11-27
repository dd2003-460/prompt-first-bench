# N45: CUDA Overhead 显存占用量化：CUDA 上下文、内核加载、内存分配器等开销通常固定为 0.5-1.0 GB，与模型大小和序列长度无关。在 PyTor

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

CUDA Overhead 显存占用量化：CUDA 上下文、内核加载、内存分配器等开销通常固定为 0.5-1.0 GB，与模型大小和序列长度无关。在 PyTorch 中，可通过 torch.cuda.memory_summary() 获取精确值，通常 'reserved' 与 'allocated' 之间的差异即为碎片化开销，约 10-20% 的已分配内存。

## Corrected Claim

CUDA 上下文、内核加载等开销通常在数百 MB 至 1 GB 左右，具体数值随 GPU 型号、驱动及 CUDA 版本变化，并非严格固定。在 PyTorch 中，可通过 torch.cuda.memory_summary() 获取内存状态，'reserved' 与 'allocated' 之间的差异反映了内存碎片化及预分配未使用部分，其比例视分配模式而定，并非恒定为 10-20%。

## Evidence

[质询]CUDA 上下文及驱动开销并非严格固定为 0.5-1.0 GB，该数值高度依赖于 GPU 架构、驱动版本、CUDA 版本以及是否启用 MPS 等特性，不同环境下波动较大，将其描述为“通常固定”缺乏普适性且易误导。 | 经验事实，逻辑自洽但缺来源支持；CUDA 开销量级在常见数据中心 GPU 上大致合理，但具体数值非恒定，且无外部来源直接验证该固定区间。

## Search Query

PyTorch CUDA memory overhead reserved allocated difference fragmentation
