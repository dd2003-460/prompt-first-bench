# N36: NVFP4/W4 权重占用空间计算：27.8B * 0.5 bytes = 13.9 GB，需确认 NVFP4 是否包含 block-wise scale 因子

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

NVFP4/W4 权重占用空间计算：27.8B * 0.5 bytes = 13.9 GB，需确认 NVFP4 是否包含 block-wise scale 因子（如每 128 元素一个 scale，额外开销约 1-2%）

## Corrected Claim

NVFP4 权重基础占用约为 27.8B * 0.5 bytes = 13.9 GB，但需额外计入 block-wise scale 因子（如每 128 元素一个 scale）带来的约 1-2% 额外开销，实际占用略高于 13.9 GB。

## Evidence

[质询]NVFP4 并非简单的 4-bit 整数存储，其核心特性是包含 block-wise scale 因子（通常每 128 或 256 个元素一个 FP8/FP16 scale），因此实际字节占用会略高于纯 0.5 bytes/element 的理论值，直接计算 27.8B * 0.5 忽略了这部分元数据开销，导致数值偏低。 | 来源 [1] 和 [2] 确认了 NVFP4 格式的存在及其在 Blackwell 架构上的应用，但未提供具体的 scale 因子开销比例或精确的每元素字节数；该事实属于经验性硬件/格式规格，逻辑上 0.5 bytes 是 4-bit 的基础值，但缺乏来源直接支持包含 scale 后的精确总占用，故降级。

## Search Query

NVFP4 quantization overhead scale factors storage

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1944504541950248086&rut=7c0984fec9ccc397e773776c6f1d777c9a29f0f4e3ca3f64035752532416768f', 'type': 'ddg', 'title': 'Nvfp4量化技术深度解析：4位精度下实现2.3倍推理加速 - 知乎'}
- {'url': 'https://arxiv.org/pdf/2509.25149v1&rut=03182edf92f725599267994c933f2ae2fccace1b1037fb1712b410202f143ddc', 'type': 'ddg', 'title': 'Pretraining Large Language Models with NVFP4 - arXiv.org'}
