# N8: 数据中心级硬件候选集：NVIDIA L4 (24GB VRAM, ~300 GB/s bandwidth, ~$2000), NVIDIA A10 (24GB 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

数据中心级硬件候选集：NVIDIA L4 (24GB VRAM, ~300 GB/s bandwidth, ~$2000), NVIDIA A10 (24GB VRAM, ~600 GB/s bandwidth, ~$3500), NVIDIA H100/H800 (80GB HBM3, ~2.0-3.35 TB/s bandwidth, ~$25k-$30k), NVIDIA A100 (80GB HBM2e, ~1.55 TB/s bandwidth, ~$15k)。

## Corrected Claim

数据中心级硬件候选集包含 NVIDIA L4、A10、H100/H800、A100 等型号，其具体 VRAM、带宽及价格需查阅最新官方数据表或市场报价以获取准确数值。

## Evidence

[质询]参考来源仅覆盖 NVIDIA L4 的规格，完全缺失 A10、H100/H800、A100 的数据及所有 GPU 的价格信息，导致大部分陈述缺乏外部证据支持。 | 来源 [1][2][3] 确认了 L4 的存在及部分特性，但未提供具体 VRAM/Bandwidth 数值或价格；其余 GPU 数据无来源支持，属经验事实且缺来源，故降级。

## Search Query

NVIDIA data center GPU L4 A10 H100 A100 specs VRAM bandwidth price

## Retrieval Sources

- {'url': 'https://resources.nvidia.com/en-us-gpu-resources/l4-tensor-datasheet?ncid=no-ncid&rut=949b510d477ae84b7adae014777ef8b764ede5cb550391150852fc8aa8c7fb95', 'type': 'ddg', 'title': 'NVIDIA L4 GPU Datasheet'}
- {'url': 'https://www.nvidia.com/en-us/data-center/l4/&rut=b999f99c78c09f51ca616c668d4351c99ee8414536bbb0cb293fb9cf18f0b4ea', 'type': 'ddg', 'title': 'L4 Tensor Core GPU for AI & Graphics | NVIDIA'}
- {'url': 'https://www.nvidia.com/zh-tw/data-center/l4/&rut=57e48cdbef53ef7aba06ec8212ab5c3fca3e465f68fe3c8f020f87c75e6cf997', 'type': 'ddg', 'title': '用於 AI 和 圖像的 L4 Tensor Core GPU | NVIDIA'}
