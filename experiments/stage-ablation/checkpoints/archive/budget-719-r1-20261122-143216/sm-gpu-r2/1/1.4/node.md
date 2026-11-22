# N9: FP8/INT8 量化下 Qwen3-27B 的权重存储降至 27 GB，但需验证在 32K 长上下文场景下的困惑度（Perplexity）增量是否小于 5%，

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

FP8/INT8 量化下 Qwen3-27B 的权重存储降至 27 GB，但需验证在 32K 长上下文场景下的困惑度（Perplexity）增量是否小于 5%，若超过则判定质量损失不可接受

## Corrected Claim

FP8/INT8 量化下 Qwen3-27B 的权重存储约为 27 GB；在 32K 长上下文场景下的困惑度增量需通过具体基准测试验证，通常 FP8 量化对质量影响较小，但“小于 5%”的具体阈值需依据实际评测结果判定。

## Evidence

[质询]陈述中关于“32K长上下文下困惑度增量是否小于5%”的具体阈值及验证结论属于经验性工程指标，无法从第一性原理推导，且参考来源主要关注部署显存和速度，未提供该特定场景下的困惑度对比数据。 | 来源[1][2][3]证实了Qwen3-27B支持FP8量化且能显著降低显存占用（逻辑上27B参数FP8约为27GB，量级合理），但均未提供32K上下文下困惑度增量<5%的具体实证数据，属于经验事实缺来源支持。

## Search Query

Qwen3-27B FP8 INT8 quantization perplexity degradation long context 32k

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=acf49add5f46f2eaea65895c9fafae22a87eef3a627f68bc88459aef389fbcbb', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_32296621/article/details/166022305&rut=1988a9a0fa62f6e7373ed9a13fd2f678514c6d43e2c5cfe89a5a414396e58a6e', 'type': 'ddg', 'title': 'Qwen3.8-27B去审查FP8量化版：本地部署实战指南 - CSDN博客'}
- {'url': 'https://www.datalearner.com/blog/qwen3-8-27b-local-deployment-quantization-guide&rut=5665e872f90ea316a774a152d65358b2ab3193d74e04fe006cbd6b2fee9166a5', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地部署完全指南：量化版本怎么选，效果差多少，速度有多快？ | DataLearnerAI'}
