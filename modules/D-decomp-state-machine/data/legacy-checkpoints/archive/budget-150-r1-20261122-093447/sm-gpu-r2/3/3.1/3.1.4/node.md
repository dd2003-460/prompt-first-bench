# N80: Qwen3-27B 在 NVFP4 精度下的 MATH 数学推理基准测试准确率及相对于 BF16 基线的绝对下降值（ΔMATH）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

Qwen3-27B 在 NVFP4 精度下的 MATH 数学推理基准测试准确率及相对于 BF16 基线的绝对下降值（ΔMATH）

## Corrected Claim

Qwen3.6-27B（注意版本差异）在 NVFP4 精度下进行了 MATH 等基准测试，具体准确率及相对于 BF16 的绝对下降值需查阅完整报告，现有摘要未提供确切数值。

## Evidence

[质询]参考来源均指向 'Qwen3.6-27B' 而非 'Qwen3-27B'，存在模型版本混淆风险；且摘要中未直接提供 MATH 基准的具体数值及 ΔMATH 绝对下降值，仅提及 MMLU Pro 等指标，无法直接验证具体数值。 | 来源 [1][2][3] 主题相关（NVFP4 精度对比），但均针对 Qwen3.6-27B 且摘要未包含 MATH 具体数值，属于间接支持/证据不足，符合经验事实缺直接来源支持的降级条件。

## Search Query

Qwen3-27B NVFP4 MATH benchmark accuracy

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00951/article/details/168656480&rut=71c6e1be65bbc23bfc7f503b60bfe1cc65244a06c54f645b59e12967ba2e801a', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 vs NVIDIA NVFP4 vs FP8 vs BF16：精度基准全对比，4-b'}
- {'url': 'https://blog.csdn.net/chen695969/article/details/162604876&rut=cea0366098e2c98d92cd2d1d7e767e93d35d42e4c829eb85b5926f23410c838c', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/153300295&rut=59e5aebe53f3402514f50654c940aab377ec3b93c43eb9ef3228233225ec85c9', 'type': 'ddg', 'title': '实测对比：NVIDIA Qwen3.6-27B-NVFP4与FP8版本9大基准测试数据深度分析'}
