# N101: 高吞吐边界条件验证：当预算上限为 $30,000 且要求 BF16 精度（Quality_Score = 1.0）时，1x H200 (141GB) 与 2x 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

高吞吐边界条件验证：当预算上限为 $30,000 且要求 BF16 精度（Quality_Score = 1.0）时，1x H200 (141GB) 与 2x H100 (160GB, NVLink) 的 T_decode 延迟对比。H200 带宽优势 (4.8TB/s vs 3.35TB/s) 在 32K 上下文下的具体加速倍数计算

## Corrected Claim

当预算上限为 $30,000 且要求 BF16 精度时，1x H200 (141GB, 4.8TB/s) 与 2x H100 (160GB, 聚合带宽约 6.7TB/s) 的 T_decode 延迟对比。由于 2x H100 的聚合带宽高于单卡 H200，在纯带宽受限的 Decode 阶段，2x H100 可能具有优势或持平，具体取决于 NVLink 通信开销和软件栈优化，而非简单的单卡带宽倍数关系。

## Evidence

[质询]陈述中关于 2x H100 的总带宽（160GB, 3.35TB/s）存在严重的物理/架构逻辑错误。H100 SXM5 单卡显存为 80GB，2 卡应为 160GB，但单卡 HBM3 带宽约为 3.35TB/s，2 卡并行总带宽应约为 6.7TB/s，而非 3.35TB/s。若指单卡带宽，则与 H200 的 4.8TB/s 对比时，忽略了 2 卡并行带来的聚合带宽优势，导致加速倍数计算基础错误。 | 来源 [2] 确认 H200 带宽为 4.8TB/s，但未提供 2x H100 的聚合带宽数据；逻辑校验发现 2x H100 的带宽描述（3.35TB/s）与单卡规格（~3.35TB/s）混淆，导致对比基准错误，属于硬逻辑错误。

## Search Query

H200 vs 2x H100 inference latency BF16 32K context bandwidth advantage

## Retrieval Sources

- {'url': 'https://tokcalc.vercel.app/compare/h100-vs-h200&rut=28a4e8855e9337634aea88b6732431435046e36304926be1181298e4640eca13', 'type': 'ddg', 'title': 'H100 vs H200 for LLM Inference: Throughput, Latency, VRAM & Cost'}
- {'url': 'https://www.spheron.network/blog/nvidia-h100-vs-h200/&rut=093f80be9fac4c56c7e4d6a3563dae3a25ef607c176fd2d0e64d9feafeba15eb', 'type': 'ddg', 'title': 'H100 vs H200: Specs, FP8 Throughput & Cloud Pricing Compared (2026 ...'}
- {'url': 'https://www.spheron.network/blog/flashattention-2-vs-flashattention-3-h100-h200-guide/&rut=58ea0f0fdcb70c4cef6f90b61b426495b9d638d6e7f953499f186bd60fda8ead', 'type': 'ddg', 'title': 'FlashAttention 2 vs FlashAttention 3: H100 and H200 Speedups, FP8 ...'}
