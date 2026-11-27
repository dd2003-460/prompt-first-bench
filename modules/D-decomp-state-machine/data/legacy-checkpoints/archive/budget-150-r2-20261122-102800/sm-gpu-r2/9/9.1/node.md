# N152: Qwen3-27B在4-bit量化（NVFP4）下GSM8K准确率约为68%，BF16基准准确率约为80%，绝对损失12个百分点。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N50

## Claim

Qwen3-27B在4-bit量化（NVFP4）下GSM8K准确率约为68%，BF16基准准确率约为80%，绝对损失12个百分点。

## Corrected Claim

Qwen3系列27B模型在4-bit量化（NVFP4）下GSM8K准确率相比BF16基准存在显著下降（约10-15个百分点），具体数值需参考对应版本（如Qwen3.6/3.8）的官方基准测试。

## Evidence

[质询]参考来源中的模型版本号（Qwen3.6-27B, Qwen3.8-27B）与陈述中的模型版本（Qwen3-27B）不一致，且来源摘要未提供具体的GSM8K准确率数值，无法直接证实68%和80%的具体数值。 | 来源[1]和[2]涉及Qwen3系列27B模型的NVFP4量化对比，主题相关但版本号不匹配且缺乏具体数值支持；逻辑上4-bit量化导致约12个百分点的精度损失符合一般经验规律，但具体数值缺乏直接证据。

## Search Query

Qwen3-27B 4-bit NVFP4 GSM8K accuracy benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00951/article/details/168656480&rut=71c6e1be65bbc23bfc7f503b60bfe1cc65244a06c54f645b59e12967ba2e801a', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 vs NVIDIA NVFP4 vs FP8 vs BF16：精度基准全对比，4-bit量化真的掉分吗'}
- {'url': 'https://blog.csdn.net/gitblog_01106/article/details/168111467&rut=4656c8b0bb90a8c61ac16354a3a742e3f4aeb46755b5b0c16d71beecf1c6a31b', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4完整指南：4位NVFP4量化如何玩转27B多模态大模型-CSDN博客'}
