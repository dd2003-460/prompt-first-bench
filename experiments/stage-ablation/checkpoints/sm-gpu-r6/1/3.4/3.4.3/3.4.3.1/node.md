# N160: Intel Arc A770 (16GB) 或 A750 (8GB) 运行 Qwen3-27B 时，单卡显存容量（16GB/8GB）远小于 BF16 权重需求（

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

Intel Arc A770 (16GB) 或 A750 (8GB) 运行 Qwen3-27B 时，单卡显存容量（16GB/8GB）远小于 BF16 权重需求（54GB），必须依赖 CPU Offload 或 INT4/INT8 量化；在 llama.cpp Vulkan backend 下，A770 的实测 tokens/s 约为 CUDA RTX 4090 的 5-10% [待核验]。

## Corrected Claim

Intel Arc A770 (16GB) 或 A750 (8GB) 运行 Qwen3-27B 时，单卡显存容量（16GB/8GB）远小于 BF16 权重需求（54GB），必须依赖 CPU Offload 或 INT4/INT8 量化；在 llama.cpp Vulkan backend 下，A770 的实测 tokens/s 显著低于 CUDA RTX 4090（具体比例取决于量化与 Offload 配置，通常远低于 10%）。

## Evidence

[质询]数值量级与具体性能对比缺乏来源支持：'A770 实测 tokens/s 约为 CUDA RTX 4090 的 5-10%' 是一个具体的经验性能断言，且不同量化方案（INT4 vs INT8）、Offload 比例及模型版本（Qwen3-27B 具体参数结构）会显著影响该比例，5-10% 的范围可能过于狭窄或基于特定未说明的配置。 | 先验知识/题面给定，逻辑校验通过：显存容量（16GB/8GB）远小于 BF16 权重需求（54GB）的逻辑推导成立，必须依赖量化或 Offload 的结论正确；但具体性能对比数值（5-10%）属于经验事实，虽逻辑上合理（A770 性能远低于 4090），但缺乏来源直接支持该特定比例，故降级。

## Search Query

Intel Arc A770 llama.cpp Vulkan benchmark tokens per second vs RTX 4090
