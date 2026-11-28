# N104: Qwen3-27B FP8 (E4M3/E5M2) 推理最低要求 CUDA 12.2 及以上版本，且需搭配支持 FP8 Tensor Core 的硬件（如 Ad

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

Qwen3-27B FP8 (E4M3/E5M2) 推理最低要求 CUDA 12.2 及以上版本，且需搭配支持 FP8 Tensor Core 的硬件（如 Ada Lovelace 或 Blackwell 架构）；CUDA 12.1 仅支持 FP8 存储但不保证全链路 FP8 计算加速。

## Corrected Claim

Qwen3-27B（或相关版本如 Qwen3.8-27B）FP8 推理需搭配支持 FP8 Tensor Core 的硬件（如 Ada Lovelace 或 Blackwell 架构）以实现全链路加速；在 Ampere 等不支持 FP8 Tensor Core 的硬件上，框架通常回退至 W8A16 模式（权重 FP8，计算 BF16）。CUDA 版本的具体最低要求需参考官方文档，但通常 FP8 支持始于 CUDA 12.x 系列。

## Evidence

[质询]来源中提到的模型名称为 'Qwen3.8-27B'，与陈述中的 'Qwen3-27B' 存在细微差异（可能是笔误或不同版本），且来源主要讨论的是 SGLang/vLLM 在 Ampere 架构上的回退机制，并未直接提供 CUDA 12.2 作为 Qwen3-27B FP8 推理的‘最低硬性要求’这一具体版本约束的官方文档证据。 | 来源 [2] 间接支持了 FP8 计算需要特定硬件（Ampere 无 FP8 Tensor Core 导致回退到 W8A16），符合陈述中关于硬件要求的逻辑；但来源未直接证实 CUDA 12.2 是最低版本要求，且模型名称存在不一致，故降级。

## Search Query

NVIDIA CUDA 12.2 release notes FP8 support Qwen

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=703955979b9fa5473f892e9cc833e8a83c17da81ae43d0b61ec72f10a13a0f3e', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://blog.mitsea.com/3c1779ab6468800eac67f555a5301e82/&rut=8f1f38ebba9621d7274a4d4490ec7dfc3c6000aec03ec88e2a4c88896199ebd9', 'type': 'ddg', 'title': 'Qwen3.8-27B 部署技术报告'}
