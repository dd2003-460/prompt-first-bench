# N115: NVFP4 量化下 draft model 的 logit 偏差主要源于 W4A16 权重的舍入误差在长上下文注意力计算中的累积，具体表现为 KV Cache 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

NVFP4 量化下 draft model 的 logit 偏差主要源于 W4A16 权重的舍入误差在长上下文注意力计算中的累积，具体表现为 KV Cache 中 K/V 向量的 FP8 存储精度损失（相对误差 ~2^-7）导致 dot product 计算偏差随 seq_len 线性增长，从而降低 draft 与 target 模型的 top-k 重合率。

## Corrected Claim

NVFP4 量化下 draft model 的 logit 偏差源于低精度权重（4-bit）及 KV Cache（FP8/FP4）的舍入误差累积，其中 KV Cache 精度损失随序列长度增加导致注意力分数偏差，进而降低 draft 与 target 模型的 top-k 重合率。

## Evidence

[质询]归因逻辑存在混淆：NVFP4 通常指权重为 4-bit、激活为 FP4 或混合精度，而陈述中称 'W4A16' 且 KV Cache 为 FP8，这与 NVFP4 的标准定义（通常涉及 FP4 激活或特定硬件格式）可能存在术语混用；此外，logit 偏差主要源于 KV Cache 精度损失这一因果链条过于简化，忽略了权重本身 4-bit 量化带来的巨大噪声以及 Softmax 非线性放大效应，将复杂的多因素误差简单归结为 KV Cache 的线性累积缺乏严谨性。 | 先验知识/题面给定，逻辑校验通过（量级和方向合理，但具体归因机制过于简化且术语对应存疑，故降级）
