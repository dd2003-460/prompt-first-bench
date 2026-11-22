# N65: NVFP4 (FP4 E2M1) 格式在 Qwen3-27B 上的具体量化算法（如 SmoothQuant, GPTQ, AWQ, 或原生 FP4 训练后量化）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15, N16, N17

## Claim

NVFP4 (FP4 E2M1) 格式在 Qwen3-27B 上的具体量化算法（如 SmoothQuant, GPTQ, AWQ, 或原生 FP4 训练后量化）及其对应的校准数据集大小（如 128-512 样本），因为不同算法对长尾分布权重的处理差异直接决定 4-bit 下的精度上限

## Corrected Claim

NVFP4 (FP4 E2M1) 格式在 Qwen3-27B 上的具体量化算法及校准数据集大小需查阅特定技术报告或论文，不同算法对长尾分布权重的处理差异确实会影响 4-bit 下的精度上限。

## Evidence

[质询]该陈述包含具体的经验事实（特定模型 Qwen3-27B 的量化算法选择及校准集大小），参考来源仅讨论了 NVFP4 格式的一般特性，未提供针对 Qwen3-27B 的具体算法细节或校准数据规模，无法验证具体数值和算法归属。 | 来源 [1] 确认了 NVFP4 格式的存在及其优于原生 FP4 的特性，间接支持了量化精度的讨论背景，但未提供 Qwen3-27B 的具体量化算法（如 SmoothQuant/GPTQ 等）及校准集大小（128-512 样本）的直接证据，属于经验事实缺来源支持。

## Search Query

Qwen3-27B NVFP4 quantization method SmoothQuant GPTQ AWQ calibration dataset size

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2049244381027292133&rut=30ea8626e1f6abdc1ae33572b84eaf1111e96f0deca06d87e99d49868ff156c8', 'type': 'ddg', 'title': 'Nvfp4、Fp8、Bf16 大模型量化格式详解 - 知乎'}
