# N612: AVX-512 指令集在消费级 CPU (如 Ryzen 7000/9000) 上未启用，仅在数据中心 CPU (EPYC) 上可用，这一结论正确；但需注意，R

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N216

## Claim

AVX-512 指令集在消费级 CPU (如 Ryzen 7000/9000) 上未启用，仅在数据中心 CPU (EPYC) 上可用，这一结论正确；但需注意，Ryzen 7000/9000 支持 AVX2 和 AVX-VNNI (INT8)，但不支持 AVX-512 VNNI (INT8) 或 AVX-512 BF16 指令。

## Corrected Claim

AVX-512 指令集在消费级 CPU (如 Ryzen 7000/9000) 上未启用，仅在数据中心 CPU (EPYC) 上可用，这一结论正确；但需注意，Ryzen 7000/9000 支持 AVX2 和 AVX-VNNI (INT8)，但不支持 AVX-512 VNNI (INT8) 或 AVX-512 BF16 指令。

## Evidence

先验知识/题面给定，逻辑校验通过：AMD Zen 4/5 架构（Ryzen 7000/9000）确实支持 AVX2 和 AVX-VNNI，但不支持 AVX-512 指令集（包括 AVX-512 VNNI/BF16），AVX-512 在 AMD 平台主要见于 EPYC 系列。
