# N250: Qwen3-27B 在 2×RTX 4090 (48GB) 下，不同量化精度（INT4/INT8/FP8）权重占用显存的具体数值（GB），用于确定剩余显存用于 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98

## Claim

Qwen3-27B 在 2×RTX 4090 (48GB) 下，不同量化精度（INT4/INT8/FP8）权重占用显存的具体数值（GB），用于确定剩余显存用于 KV Cache 的上限。

## Corrected Claim

Qwen3-27B 在 2×RTX 4090 (48GB) 下，不同量化精度（INT4/INT8/FP8）权重占用显存的具体数值需根据实际部署框架（如 vLLM, llama.cpp）及具体模型版本（Qwen3 或 Qwen3.8）实测确定，通常 INT4 约 14-16GB，INT8 约 27-29GB，FP8 约 27-29GB（单卡权重部分），双卡部署需考虑通信开销及框架额外内存。

## Evidence

[质询]来源标题提及的是 'Qwen3.8-27B' 且仅涉及单张 4090，与事实节点中的 'Qwen3-27B' 及 '2×RTX 4090' 配置存在版本和硬件规模上的不匹配，无法直接提供双卡环境下不同量化精度的具体显存占用数值。 | 经验事实，逻辑自洽但缺来源支持（来源[1]主题相关但硬件配置和模型版本不完全匹配，未提供双卡具体数值）

## Search Query

Qwen3-27B model size GB INT4 INT8 FP8 quantization memory footprint

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073510788808041813&rut=a77d5a5fecdef8d6bdc7fd7a08bc24438eb2f3091be79164857be09419f0126a', 'type': 'ddg', 'title': '超强端侧大模型!一张 4090，把 Qwen3.8-27B 跑到真能干活：能力实测、快速部署与最佳参数分享 - 知乎'}
