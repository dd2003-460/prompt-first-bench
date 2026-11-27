# N107: ROCm 生态在 2024 年对 Qwen3 系列模型的支持存在已知兼容性缺陷，包括 KV Cache 量化支持不全及 Attention 算子性能回退约 15

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42, N43, N44

## Claim

ROCm 生态在 2024 年对 Qwen3 系列模型的支持存在已知兼容性缺陷，包括 KV Cache 量化支持不全及 Attention 算子性能回退约 15-20%，这导致其实际有效吞吐量需从理论值打折计算。

## Corrected Claim

ROCm 生态在 2024 年对 Qwen3 系列模型的支持存在已知兼容性缺陷，导致其实际有效吞吐量可能低于理论值，具体性能损失需视硬件和模型版本而定。

## Evidence

[质询]具体数值（15-20%性能回退）和特定技术细节（KV Cache量化支持不全）缺乏来源直接支持，且来源[1]主要讨论的是特定硬件（Ryzen AI MAX+ 395）和特定模型版本（Qwen3.8-Flash-Next）的构建兼容性，而非整个Qwen3系列在2024年的通用生态缺陷。 | 来源[1]证实了ROCm在特定场景下存在兼容性问题（'ROCm全败'），间接支持了'存在已知兼容性缺陷'的定性描述，但未提供'15-20%性能回退'或'KV Cache量化支持不全'的具体证据，属于间接支持。

## Search Query

ROCm Qwen3 compatibility issues performance penalty 2024

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2080025658277863444&rut=de496448c0fb76f59b4ca373087615e5a8a0ef6922bd3e99515bf95843fd1fd0', 'type': 'ddg', 'title': '从 ROCm 翻车到双后端可用：Qwen3.8-Flash-Next 在 Ryzen AI MAX+ 395 上的显存 / 后端 / 系统完整 ...'}
