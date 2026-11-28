# N22: Qwen3-27B 从 BF16 到 NVFP4 的质量损失：在 MMLU 基准测试上下降约 5-10%，在复杂推理任务上下降约 8-15% [待核验具体数值]

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B 从 BF16 到 NVFP4 的质量损失：在 MMLU 基准测试上下降约 5-10%，在复杂推理任务上下降约 8-15% [待核验具体数值]，主要源于 4-bit 表示对权重分布的过度压缩和块级缩放的粒度限制

## Corrected Claim

Qwen3-27B 从 BF16 到 NVFP4 的质量损失极小，在 MMLU 等基准测试上通常下降不超过 1%，主要得益于 NVFP4 高效的块级缩放机制，而非陈述中所述的显著性能衰退。

## Evidence

[质询]数值量级严重错误：参考来源明确指出 NVFP4 量化带来的精度损失极小（<1% 或与 FP8 差距在 1 分以内），而陈述中声称 MMLU 下降 5-10%、复杂推理下降 8-15%，这与实际数据相差一个数量级，属于严重的夸大失真。 | 来源 [1] 指出精度损失低于 1%，来源 [3] 指出与 FP8 基准差距在 1 分以内，均直接矛盾于陈述中 5-15% 的大幅下降说法。

## Search Query

Qwen3-27B NVFP4 4-bit quantization MMLU complex reasoning accuracy loss

## Retrieval Sources

- {'url': 'https://flowtivity.ai/blog/qwen3-6-27b-nvfp4-blackwell-quantization/&rut=8f0cee2a3a3bc24232c1cc0a7b895afdddd3882f5dca090ff37f6aa06b49472f', 'type': 'ddg', 'title': "Nvidia's Qwen3.6-27B-NVFP4: 27B Parameter AI Now Runs on Consumer ..."}
- {'url': 'https://kie.ai/blog/qwen-3-6-27b-deep-dive-benchmarks-quantization&rut=11a3679303835513266e39c3516a9bfd0b0ce098dbd07655c82935b825c3a217', 'type': 'ddg', 'title': 'Qwen 3.6 27B Benchmark Deep Dive: The Measured Numbers'}
- {'url': 'https://thakicloud.com/tech-blog/en/owm/qwen3-6-27b-nvfp4-onprem-serving/&rut=9bbf7e0f54b583e77a9c90ae685f162b5e8e9303bf41589eba388e3166ee1272', 'type': 'ddg', 'title': 'Qwen3.6-27B at 4-bit: Why NVFP4 Quantization Came Down to Hopper'}
