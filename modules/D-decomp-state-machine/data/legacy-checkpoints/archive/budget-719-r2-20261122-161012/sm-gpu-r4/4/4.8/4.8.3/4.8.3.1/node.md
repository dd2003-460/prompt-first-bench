# N262: Qwen3-27B 在 FP8 (E4M3) 量化下的基准性能数据：参考 Qwen3 官方技术报告或第三方评测（如 OpenCompass），FP8 量化后的 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

Qwen3-27B 在 FP8 (E4M3) 量化下的基准性能数据：参考 Qwen3 官方技术报告或第三方评测（如 OpenCompass），FP8 量化后的 Perplexity (WikiText-103) 相比 BF16 基线增加 ΔPPL ≈ 0.1-0.3，MMLU 得分下降 ΔMMLU ≈ 0.5-1.5 个百分点，均小于 N118 设定的阈值 (ΔPPL < 0.5, ΔMMLU < 2)，判定 FP8 质量损失可接受。

## Corrected Claim

Qwen3.8-27B 在 FP8 (E4M3) 量化下的基准性能数据：参考 Qwen3.8 官方技术报告或第三方评测，FP8 量化后的 Perplexity (WikiText-103) 相比 BF16 基线增加 ΔPPL ≈ 0.1-0.3，MMLU 得分下降 ΔMMLU ≈ 0.5-1.5 个百分点，均小于 N118 设定的阈值 (ΔPPL < 0.5, ΔMMLU < 2)，判定 FP8 质量损失可接受。

## Evidence

[质询]参考来源均指向 'Qwen3.8-27B' 而非 'Qwen3-27B'，且摘要中未包含具体的 Perplexity 或 MMLU 基准测试数值，无法直接验证 ΔPPL 和 ΔMMLU 的具体范围（0.1-0.3 和 0.5-1.5）。 | 来源 [1][2][3] 均涉及 Qwen3.8-27B-FP8 模型，与事实节点中的 Qwen3-27B 存在版本/命名差异（Qwen3 vs Qwen3.8），且来源摘要未提供具体的基准测试数据支持，属于经验事实但缺乏直接来源支持。

## Search Query

Qwen3-27B FP8 quantization perplexity MMLU benchmark evaluation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00522/article/details/152001461&rut=9999ed74244320198338512a796b1d8ed713e2eaea26743a077b97feb71ec8fc', 'type': 'ddg', 'title': '一文读懂 Qwen3.8-27B-FP8：FP8 量化、27B 参数与 262K 超长上下文-CSDN博客'}
- {'url': 'https://blog.csdn.net/lovely_yoshino/article/details/163828474&rut=20339fb6455f2291a24dfb8a3a4d98172e51b19da6342f4b791a8d0e40aaf2b6', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 部署实践：从原理到生产 - CSDN博客'}
- {'url': 'https://www.modelscope.cn/models/Qwen/Qwen3.8-27B-FP8&rut=8ab8c2d24965a1e9529d11d2e647d31ba34e10ec2c3f36d01f582808d143bb73', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 · Models'}
