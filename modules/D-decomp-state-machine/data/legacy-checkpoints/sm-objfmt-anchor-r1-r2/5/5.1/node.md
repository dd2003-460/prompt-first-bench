# N99: FP8 E4M3 量化机理：FP8 E4M3 格式提供 3 位指数和 3 位尾数，动态范围约为 [-448, 448]，精度介于 FP16 和 INT8 之间。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

FP8 E4M3 量化机理：FP8 E4M3 格式提供 3 位指数和 3 位尾数，动态范围约为 [-448, 448]，精度介于 FP16 和 INT8 之间。对于权重分布偏态严重的 Transformer 模型，E4M3 能更好地保留小权重的高精度，因此 ΔPPL < 0.05 的‘近无损’结论主要源于其对权重长尾分布的适应性，而非单纯的位数优势。

## Corrected Claim

FP8 E4M3 量化机理：FP8 E4M3 格式提供 3 位指数和 3 位尾数，动态范围约为 [-448, 448]，精度介于 FP16 和 INT8 之间。对于权重分布偏态严重的 Transformer 模型，E4M3 能更好地保留小权重的高精度，因此 ΔPPL < 0.05 的‘近无损’结论主要源于其对权重长尾分布的适应性，而非单纯的位数优势。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 E4M3 格式定义（1+4+3位）及动态范围（±448）符合 IEEE 754 子集标准，其相比 INT8 在保持小数值精度上的优势符合浮点数表示原理，逻辑自洽。

## Search Query

FP8 E4M3 quantization perplexity impact transformer weights
