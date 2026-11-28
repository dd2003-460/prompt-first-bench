# N21: Qwen3-27B 从 BF16 到 INT8 的质量损失：在 MMLU 基准测试上下降约 1-3%，在长文本生成一致性上下降约 3-5% [待核验具体数值]，

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B 从 BF16 到 INT8 的质量损失：在 MMLU 基准测试上下降约 1-3%，在长文本生成一致性上下降约 3-5% [待核验具体数值]，主要源于非对称量化对激活值分布的偏差

## Corrected Claim

Qwen3系列模型从BF16量化至INT8通常会导致基准测试性能出现轻微下降（具体幅度视模型规模和量化方法而定），主要源于量化误差对模型精度的影响。

## Evidence

[质询]具体数值（MMLU下降1-3%，长文本一致性下降3-5%）及归因（非对称量化对激活值分布的偏差）缺乏来源支持，且Qwen3-27B并非标准发布型号（通常为235B-A22B或更小/更大整数倍），存在型号混淆或数据虚构风险。 | 参考来源[1]提及的是Qwen3.8-27B（多模态），来源[2]为Qwen3技术报告但未提供具体量化损失数值；该事实属于经验性量化评估数据，逻辑上INT8量化导致轻微性能下降是合理的，但具体百分比和归因机制无来源直接支持，符合经验事实排除条款。

## Search Query

Qwen3-27B INT8 quantization MMLU long-form generation quality degradation

## Retrieval Sources

- {'url': 'https://github.com/AlibabaCloud-Official/Qwen3.8-27B&rut=a332b0ce380d5c34328ba249051c409a073159eaa8056b4b8ce330676a0a4380', 'type': 'ddg', 'title': 'GitHub - AlibabaCloud-Official/Qwen3.8-27B: Native multimodal dense LLM ...'}
- {'url': 'https://arxiv.org/pdf/2505.09388&rut=9472ef158696388024a311921d5bf4d4fbac06b33151207dbaae5a50ba090d85', 'type': 'ddg', 'title': 'Qwen3 Technical Report - arXiv.org'}
