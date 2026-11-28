# N303: 在 GSM8K 长逻辑链（>200 tokens）场景下，MTP×4 的验证回滚开销占比随 AR 降低而急剧上升，当 AR < 40% 时，验证开销占总推理时间

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

在 GSM8K 长逻辑链（>200 tokens）场景下，MTP×4 的验证回滚开销占比随 AR 降低而急剧上升，当 AR < 40% 时，验证开销占总推理时间的比例超过 25%，导致实际吞吐低于无投机解码基线，此时应禁用 MTP 以维持稳定性。

## Corrected Claim

在 GSM8K 长逻辑链场景下，MTP×4 的验证回滚开销占比随 AR 降低而上升；当 AR 较低时，验证开销可能显著增加并导致实际吞吐低于无投机解码基线，此时需根据具体系统配置评估是否禁用 MTP。

## Evidence

[质询]该陈述包含具体的经验阈值（AR<40%、开销>25%）和特定场景下的性能结论，属于经验事实。参考来源 [1] 仅涉及 GSM8K 基准测试中不同模型的准确率对比，完全未提及 MTP（Multi-Token Prediction）、投机解码、验证回滚开销或吞吐量等系统级性能指标，因此无法提供外部支持。此外，'AR<40% 时吞吐低于基线'这一结论高度依赖于具体的硬件配置、模型大小及 MTP 实现细节，缺乏通用性，存在将特定实验结果过度泛化的风险。 | 逻辑上自洽（低接受率导致高验证开销从而降低吞吐符合投机解码基本原理），但参考来源 [1] 与系统性能优化无关，无法提供直接支持；作为经验事实，缺乏多源一致或单一直接来源支持，故降级。

## Search Query

speculative decoding overhead rollback ratio low acceptance rate threshold

## Retrieval Sources

- {'url': 'https://arxiv.org/pdf/2312.17080&rut=2d6e935e4ef622d13e278faa67d96c7abf1fd1bbac17f1e91957b8f7af36ba42', 'type': 'ddg', 'title': 'MR-GSM8K: A Meta-Reasoning Benchmark for Large Language Model Evaluation'}
