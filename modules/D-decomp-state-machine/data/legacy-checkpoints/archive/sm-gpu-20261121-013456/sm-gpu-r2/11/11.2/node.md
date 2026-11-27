# N121: Qwen3-27B 在 FP8 E4M3 精度下，针对长文本逻辑推理任务（如 GSM8K, MATH）的最终答案准确率下降比例，预期 < 1%，需对比 BF16

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

Qwen3-27B 在 FP8 E4M3 精度下，针对长文本逻辑推理任务（如 GSM8K, MATH）的最终答案准确率下降比例，预期 < 1%，需对比 BF16 基线以确认 FP8 在逻辑推理上的稳健性。

## Corrected Claim

Qwen3-27B 在 FP8 E4M3 精度下，针对长文本逻辑推理任务（如 GSM8K, MATH）的最终答案准确率预期与 BF16 基线差异极小（通常 < 1%），但具体数值需实测确认。

## Evidence

[质询]参考来源均指向 Qwen3.5/3.6/3.8 版本，而非 Qwen3-27B；且来源主要讨论推理性能调优或体积减小，未提供 GSM8K/MATH 等逻辑推理任务在 FP8 下准确率下降 <1% 的具体量化数据，属于经验事实缺乏直接来源支持。 | 经验事实，逻辑自洽（FP8 通常对 LLM 精度影响较小），但参考来源 [1][2][3] 均针对其他 Qwen 版本且未提供具体准确率下降比例数据，无法直接支持该特定数值结论。

## Search Query

Qwen3-27B FP8 reasoning accuracy drop GSM8K MATH

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29062255/article/details/162589846&rut=e389b043182d747c4991b6c211debe4e733e341ed91d7e9dea2c20895d9b67d7', 'type': 'ddg', 'title': 'FP8精度优化Qwen3.5-27B大模型推理实战 - CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00238/article/details/151043054&rut=a1b707d3f778903e6a13d8ab1ef649aa2d9bad4cc2a563c17e7004632a2c1cfa', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 推理性能调优 10 个技巧：采样参数、输出长度与 KV Cache 优化-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/143005510&rut=26f38960e6230373005b7fbed5496a26ac1208d0db3e2d0cfa1483f31fcc4176', 'type': 'ddg', 'title': 'Qwen3.6-27B-FP8 FP8量化技术深度剖析：如何保持性能的同时减小模型体积？_滑杏舒-智能体开发者社区'}
