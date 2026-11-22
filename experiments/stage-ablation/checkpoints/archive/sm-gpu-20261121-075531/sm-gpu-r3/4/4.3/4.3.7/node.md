# N91: Qwen3-27B 在 NVFP4/W4 精度下，在通用基准 (MMLU-Pro) 上的得分，及相对 BF16 的得分下降百分比 (ΔScore%)。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N21, N22, N23

## Claim

Qwen3-27B 在 NVFP4/W4 精度下，在通用基准 (MMLU-Pro) 上的得分，及相对 BF16 的得分下降百分比 (ΔScore%)。

## Corrected Claim

Qwen3.6-27B 在 NVFP4 精度下 MMLU-Pro 得分为 86.3，与 FP8 版本差距在 ±0.5 以内；Qwen3-27B 在 BF16 下的具体得分及相对下降百分比需查阅官方技术报告或更精确的基准测试数据。

## Evidence

[质询]来源提供的数据是 Qwen3.6-27B 而非 Qwen3-27B，且未直接提供 BF16 的 MMLU-Pro 具体得分，仅说明与 FP8 差距在 ±0.5 内，无法精确计算相对 BF16 的下降百分比。 | 来源 [1] 和 [3] 提供了 Qwen3.6-27B-NVFP4 在 MMLU Pro 上的得分（86.3）及与 FP8 的对比，但未直接给出 Qwen3-27B 或 BF16 基准的具体数值，属于间接支持且存在版本/基准不匹配风险。

## Search Query

Qwen3-27B W4 MMLU-Pro score degradation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/chen695969/article/details/162604876&rut=a7a19bfa99b32b0ad40e38249eec2f5f14d2f6ed502248a8344e370364321565', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择-CSDN博客'}
- {'url': 'https://www.modelscope.cn/models/prithivMLmods/Qwen3.6-27B-NVFP4/summary&rut=95a6c33259a8ad60f008b69914c0705e2d879c286ce805d3de50a0ed6f01c6ab', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 · Models'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162604876&rut=ce986b437346723395d5fede77531458e5cfcc2fbcd05d48661b83dc8050cb57', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择'}
