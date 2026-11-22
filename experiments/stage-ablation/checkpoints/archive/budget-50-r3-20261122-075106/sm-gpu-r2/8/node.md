# N39: FP8 (E4M3/E5M2) 精度在H100/H200上的推理吞吐量相比BF16提升约1.5-2倍，且由于保留较高动态范围，其质量损失（Perplexity增

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

FP8 (E4M3/E5M2) 精度在H100/H200上的推理吞吐量相比BF16提升约1.5-2倍，且由于保留较高动态范围，其质量损失（Perplexity增加）通常小于1%，被视为当前数据中心级硬件的最佳性价比精度选择。

## Corrected Claim

FP8 (E4M3/E5M2) 在H100/H200等支持硬件上通常能带来显著的推理吞吐量提升（具体倍数依模型和实现而异），且由于保留较高动态范围，其质量损失通常较小，被视为当前数据中心级硬件的高性价比精度选择。

## Evidence

[质询]数值量级与具体性能指标缺乏来源支持：来源仅定义了FP8格式，未提供H100/H200上的具体吞吐量提升倍数（1.5-2x）或Perplexity损失（<1%）的实验数据，且不同模型和硬件配置下性能增益差异较大，直接断言固定区间存在过度概括风险。 | 来源[1]仅确认FP8包含E4M3/E5M2格式，未覆盖吞吐量提升倍数及质量损失的具体数值，属于经验事实且缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/574825662&rut=9755e3806f401d6877b27ee5d536112421e1e47c1359299fa5e0267ef1bcddf5', 'type': 'ddg', 'title': 'Fp8 量化-原理、实现与误差分析 - 知乎'}
