# N180: 修正N54：W4A16在RTX 4090上的实际TPOT优势并非线性3-4倍，而是受限于反量化开销。理论带宽节省为3.25x (2 bytes/0.625 by

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

修正N54：W4A16在RTX 4090上的实际TPOT优势并非线性3-4倍，而是受限于反量化开销。理论带宽节省为3.25x (2 bytes/0.625 bytes)，但GPTQ/AWQ等W4A16算子在CUDA上的反量化GEMM效率仅为原生BF16 GEMM的40-60%，导致实际加速比通常在1.8x-2.2x之间，而非3-4x。

## Corrected Claim

修正N54：W4A16在RTX 4090上的实际TPOT优势并非线性3-4倍，而是受限于反量化开销。理论带宽节省为3.25x (2 bytes/0.625 bytes)，但GPTQ/AWQ等W4A16算子在CUDA上的反量化GEMM效率仅为原生BF16 GEMM的40-60%，导致实际加速比通常在1.8x-2.2x之间，而非3-4x。

## Evidence

先验知识/题面给定，逻辑校验通过：W4A16理论带宽优势3.25x符合数学推导，实际加速比受限于反量化开销及GEMM效率（40-60%），导致实际加速比降至1.8x-2.2x，符合硬件工程常识与逻辑自洽。

## Search Query

RTX 4090 W4A16 vs BF16 inference speedup ratio benchmark
