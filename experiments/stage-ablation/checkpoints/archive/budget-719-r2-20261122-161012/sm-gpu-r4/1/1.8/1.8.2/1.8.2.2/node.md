# N190: Qwen3-27B 在 FP8 量化下 GSM8K 准确率的具体下降幅度。数学推理任务对数值精度敏感，但 FP8 (E4M3) 动态范围较大，通常性能损失极小 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

Qwen3-27B 在 FP8 量化下 GSM8K 准确率的具体下降幅度。数学推理任务对数值精度敏感，但 FP8 (E4M3) 动态范围较大，通常性能损失极小 (< 0.5%)。假设 BF16 基线为 91%，FP8 预计为 90.5% - 91.0%。该损失通常可忽略，FP8 在数学任务上是安全选择。

## Corrected Claim

Qwen3-27B 在 FP8 量化下 GSM8K 准确率通常会有极小幅度下降（通常 < 0.5%），具体数值需参考官方技术报告或基准测试，但 FP8 在数学任务上通常被视为安全选择。

## Evidence

[质询]陈述中给出的具体数值（BF16基线91%，FP8预计90.5%-91.0%）属于经验事实，且参考来源中并未提供Qwen3-27B在GSM8K上的具体量化前后准确率对比数据，无法验证该具体数值区间。 | 逻辑上FP8量化对大模型性能影响极小符合常识，但具体数值缺乏来源支持；来源[1]仅定性描述'保持与原始模型几乎相同性能'，未提供GSM8K具体分数，属于间接支持。

## Search Query

Qwen3-27B FP8 quantization GSM8K accuracy impact

## Retrieval Sources

- {'url': 'https://devpress.csdn.net/v1/article/detail/143005510&rut=72058e48991a9bd76b310989e16d33361ef38e72269c86969e6851a507c25d86', 'type': 'ddg', 'title': 'Qwen3.6-27B-FP8 FP8量化技术深度剖析：如何保持性能的同时减小模型体积？_滑杏舒-智能体开发者社区'}
- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=acf49add5f46f2eaea65895c9fafae22a87eef3a627f68bc88459aef389fbcbb', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_32296621/article/details/166022305&rut=1988a9a0fa62f6e7373ed9a13fd2f678514c6d43e2c5cfe89a5a414396e58a6e', 'type': 'ddg', 'title': 'Qwen3.8-27B去审查FP8量化版：本地部署实战指南 - CSDN博客'}
