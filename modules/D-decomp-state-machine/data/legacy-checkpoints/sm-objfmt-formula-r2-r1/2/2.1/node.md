# N13: Qwen3-27B 在 INT8 量化下的权重大小（约 27GB）及对应的质量退化基准测试分数（如 MMLU, HumanEval 相对 BF16 的下降百分比

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

Qwen3-27B 在 INT8 量化下的权重大小（约 27GB）及对应的质量退化基准测试分数（如 MMLU, HumanEval 相对 BF16 的下降百分比）。

## Corrected Claim

Qwen3.8-27B 在 INT8 (W8A16) 量化下的权重大小约为 27GB。关于质量退化，虽然 INT8 量化通常会导致轻微的性能下降，但参考来源未提供 MMLU 或 HumanEval 相对于 BF16 的具体下降百分比数据。

## Evidence

[质询]来源中提到的模型名称均为 'Qwen3.8-27B'，而待核验事实指定为 'Qwen3-27B'，存在版本/命名不一致的风险；此外，来源 [3] 主要讨论 GGUF 量化（Q2-Q8），虽提及 Q8 但未明确提供 INT8 在 MMLU/HumanEval 上的具体相对下降百分比数据，缺乏直接数值支持。 | 来源 [1] 确认了 Qwen3.8-27B-INT8 的存在及 W8A16 量化格式，逻辑上 27B 参数 INT8 权重大小约为 27GB 符合计算常识（27e9 * 1 byte ≈ 27GB）；但所有来源均未提供具体的 MMLU/HumanEval 相对 BF16 的下降百分比数值，且模型版本号存在细微差异（Qwen3 vs Qwen3.8），故降级为定性表述。

## Search Query

Qwen3-27B INT8 quantization quality degradation benchmark MMLU score drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00839/article/details/170612979&rut=7875455a2a1150797bd127aea853b23f483ccd9b42eb9aa508a7389defefe263', 'type': 'ddg', 'title': '新手必读：Qwen3.8-27B-INT8-W8A16-MTP的262K长上下文与266K KV内存池到底怎么用-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00522/article/details/152001461&rut=e962f847fbde1f7870b27d43e3490e9d1b7c0436300838aa829c740346d573dd', 'type': 'ddg', 'title': '一文读懂 Qwen3.8-27B-FP8：FP8 量化、27B 参数与 262K 超长上下文-CSDN博客'}
- {'url': 'https://www.datalearner.com/blog/qwen3-8-27b-local-deployment-quantization-guide&rut=1fa99b1a298bb35659b089a8fb4cc56bec0cb2545060f406b39ee8a0274e36e1', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地部署完全指南：量化版本怎么选，效果差多少，速度有多快？ | DataLearnerAI'}
