# N105: AMD Radeon PRO W7900 的显存带宽与算力规格：GDDR6 带宽 2560 GB/s (8x 256-bit @ 2.0 Gbps) 或 [待核

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

AMD Radeon PRO W7900 的显存带宽与算力规格：GDDR6 带宽 2560 GB/s (8x 256-bit @ 2.0 Gbps) 或 [待核验] 具体型号带宽，FP16 Tensor Core 算力需对比 NVIDIA 同级卡，若带宽低于 2000 GB/s，则 Decode 吞吐上限低于 RTX 5090，影响性价比排序。

## Corrected Claim

AMD Radeon PRO W7900 显存带宽约为 576 GB/s (256-bit GDDR6 @ 18 Gbps)，其 FP16 算力需对比 NVIDIA 同级卡（如 RTX 4090/5090 系列），由于带宽远低于 2000 GB/s，其 Decode 吞吐上限确实低于 RTX 5090。

## Evidence

[质询]数值量级与规格严重错误：AMD Radeon PRO W7900 基于 RDNA 3 架构，显存为 GDDR6，位宽 256-bit，频率通常为 18 Gbps（非 2.0 Gbps），带宽约为 576 GB/s（非 2560 GB/s）。2560 GB/s 是 HBM 或极高规格 GDDR6X 的量级，且 2.0 Gbps 的频率远低于 GDDR6 标准，导致计算出的带宽与标称值矛盾。此外，AMD GPU 没有 'Tensor Core' 这一专有名词（那是 NVIDIA 的术语），AMD 对应的是 Matrix Cores 或类似单元。 | 逻辑校验失败：GDDR6 带宽 2560 GB/s 需要极高的频率（如 20 Gbps 以上）或更宽的位宽，而 2.0 Gbps 的频率下 256-bit 带宽仅为 64 GB/s，陈述内部数值自相矛盾；且 AMD 无 Tensor Core 术语。来源不可用，但基于基本硬件规格知识，该陈述存在硬逻辑错误和事实错误。

## Search Query

AMD Radeon PRO W7900 memory bandwidth GB/s specs
