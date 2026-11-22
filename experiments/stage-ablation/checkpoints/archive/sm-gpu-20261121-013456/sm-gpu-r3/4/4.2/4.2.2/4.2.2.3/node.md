# N194: INT4(AWQ) 量化对 Qwen3-27B 质量损失的可接受性量化：在 MMLU 基准测试中，AWQ INT4 相比 BF16 的准确率下降通常为 1-3%

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

INT4(AWQ) 量化对 Qwen3-27B 质量损失的可接受性量化：在 MMLU 基准测试中，AWQ INT4 相比 BF16 的准确率下降通常为 1-3%，若下降 > 3% 则不可接受；需引用 Qwen 官方技术报告或第三方评测（如 LMSYS Chatbot Arena）中 Qwen3-27B-AWQ-INT4 的具体 MMLU 分数与 BF16 基线对比。

## Corrected Claim

AWQ INT4 量化通常能保持模型性能，具体质量损失需参考对应版本（如 Qwen3-27B 或 Qwen3.6-27B）的官方评测报告或第三方基准测试数据，一般经验表明下降幅度较小，但具体阈值（如 1-3%）需依据特定模型版本的实测结果确定。

## Evidence

[质询]参考来源均指向 'Qwen3.6-27B' 而非 'Qwen3-27B'，存在版本混淆风险；且来源摘要中未包含具体的 MMLU 分数对比数据，无法直接验证 '1-3% 下降' 这一具体数值区间。 | 来源 [1][2][3] 均讨论 Qwen3.6-27B-AWQ-INT4 的部署与架构，未提供 Qwen3-27B 的 MMLU 具体分数对比，属于间接相关但缺乏直接数据支持；逻辑上 AWQ INT4 通常损失较小，1-3% 符合一般经验，但具体数值需特定版本数据佐证。

## Search Query

Qwen3-27B AWQ INT4 MMLU accuracy drop compared to BF16

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00399/article/details/161864324&rut=267b4f5de28789ff3de8ee021404e86a5533b7952217d6a75c1db4d3c18a9327', 'type': 'ddg', 'title': 'Qwen3.6-27B-AWQ-INT4 模型部署与使用指南：高效量化模型实践手册-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00208/article/details/151567008&rut=d4a6e3dea625b2e9113f6a7f31e0ee5a1bd874e9a9ce1bdfd20561846fe4fe9a', 'type': 'ddg', 'title': '终极指南：Qwen3.6-27B-AWQ-INT4模型架构深度解析，从参数配置到量化技术-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/144363894&rut=8525ae31ca751ef0f01ceafe039f273ef7479d09c16985d65fa18b922268d5df', 'type': 'ddg', 'title': '技术方案：Qwen3.6-27B-AWQ-INT4的高效部署与量化优化实践'}
