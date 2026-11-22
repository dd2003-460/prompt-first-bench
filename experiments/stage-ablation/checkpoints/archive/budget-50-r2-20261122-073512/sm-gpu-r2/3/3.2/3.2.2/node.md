# N116: Qwen3-27B 在 FP8 (E5M2) 量化下，困惑度增加 1.5%-3.0%，MMLU 准确率下降 0.8%-1.5%，基于 AWQ 算法，需具体模型验

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

Qwen3-27B 在 FP8 (E5M2) 量化下，困惑度增加 1.5%-3.0%，MMLU 准确率下降 0.8%-1.5%，基于 AWQ 算法，需具体模型验证。

## Corrected Claim

Qwen3-27B 在 FP8 (E5M2) 量化下，通常会导致轻微的精度损失（如困惑度增加、MMLU 准确率下降），具体数值需基于 AWQ 等算法及特定模型版本进行实测验证。

## Evidence

[质询]参考来源均指向 Qwen3.5-27B 或 Qwen3.8-27B，而非 Qwen3-27B，存在模型版本不匹配；且来源主要关注部署与显存优化，未提供具体的困惑度（PPL）和 MMLU 准确率下降数值，无法直接支持具体的性能损失范围。 | 来源 [1][2][3] 涉及 Qwen3.5/3.8-27B 的 FP8 量化部署，与 Qwen3-27B 版本不符，且未包含具体的 PPL/MMLU 性能下降数据，属于间接相关但缺乏直接数值支持。

## Search Query

Qwen3-27B FP8 E5M2 quantization perplexity MMLU accuracy drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_28223453/article/details/162589847&rut=b722533d659afc93220bc111a3be7d0ff55ae51842a854653cb3d4c28115931b', 'type': 'ddg', 'title': 'Qwen3.5-27B大模型FP8量化部署实战：显存减半+推理加速-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=7c73d43c2d312385e48aa0ad557ba2e8eff51baaeb38951c62af550fd88281bf', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162589847&rut=ca5dfd6fd7ae8cfe3f75f2fb42d72edc28df73664a8d4eef60eb7c5197bd9858', 'type': 'ddg', 'title': 'Qwen3.5-27B大模型FP8量化部署实战：显存减半+推理加速'}
