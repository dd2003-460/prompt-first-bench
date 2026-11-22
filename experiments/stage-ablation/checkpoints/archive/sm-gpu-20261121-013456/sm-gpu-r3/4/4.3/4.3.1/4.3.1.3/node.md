# N197: FP8 E4M3 量化对 Qwen3-27B 质量损失的可接受性量化：在 C4 数据集上的 Perplexity (PPL) 相比 BF16 增加通常 < 0.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

FP8 E4M3 量化对 Qwen3-27B 质量损失的可接受性量化：在 C4 数据集上的 Perplexity (PPL) 相比 BF16 增加通常 < 0.1，在 GSM8K/MATH 等推理任务上的准确率下降 < 1%；若 PPL 增加 > 0.5 或准确率下降 > 2%，则 FP8 方案不可接受，需回退至 INT8 或 BF16。

## Corrected Claim

FP8 E4M3 量化（特别是采用细粒度块量化时）通常能显著降低 Qwen3-27B 的质量损失，在多数基准测试中表现接近 BF16；具体可接受性需根据实际业务场景的 PPL 和任务准确率下降幅度进行评估，一般认为 PPL 增加 < 0.5 且关键任务准确率下降 < 2% 为可接受范围。

## Evidence

[质询]陈述中引用的具体量化阈值（PPL增加<0.1，准确率下降<1%）属于经验性工程指标，且参考来源中未提供针对Qwen3-27B在C4/GSM8K/MATH数据集上的具体基准测试数据来直接支持这些精确数值，存在将通用经验值或特定实验结果泛化为绝对标准的风险。 | 来源[1]和[2]证实了Qwen3-27B存在FP8 E4M3量化版本且采用细粒度量化以保持精度，但均未提供C4 PPL或GSM8K/MATH准确率的具体对比数值，无法直接验证'<0.1'和'<1%'的具体阈值，属于经验事实缺来源直接支持。

## Search Query

Qwen3-27B FP8 E4M3 perplexity increase accuracy drop GSM8K MATH

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00439/article/details/155257784&rut=0e8f0dfa7b87216743b85a5d74bfff004ee7d8a8930cbb0be7f745f60a0470f2', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 量化原理深度解析：块大小 128 的细粒度 FP8 如何保持精度无损？-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=90c2b8874e00fe7c65b297d67da0c9b8864d2183e939c714938b3ce2952db9f2', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://www.modelscope.cn/models/Qwen/Qwen3.8-27B-FP8&rut=43d567f4cd5ae17b64f550f22ab64273ba3818e9461481b384c818a76dbe04f0', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 · Models'}
