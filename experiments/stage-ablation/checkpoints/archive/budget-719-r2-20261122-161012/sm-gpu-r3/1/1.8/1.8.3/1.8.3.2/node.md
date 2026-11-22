# N193: Qwen3-27B 在 INT4 (AWQ) 精度下的 MMLU 基准得分相比 BF16 基线下降幅度为 1.8% ± 0.5%，基于 AWQ 官方 GitHu

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N96

## Claim

Qwen3-27B 在 INT4 (AWQ) 精度下的 MMLU 基准得分相比 BF16 基线下降幅度为 1.8% ± 0.5%，基于 AWQ 官方 GitHub 仓库中 7B/13B 模型的平均退化率线性外推至 27B 规模，且 AWQ 算法通过保留 1% 显著权重为 FP16 以减小误差 [待核验: 需确认 Qwen3 官方 AWQ 量化模型的具体评测结果]

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ) 精度下的 MMLU 基准得分相比 BF16 基线存在一定程度的下降，具体幅度需参考官方评测报告，现有资料未提供确切的 1.8% ± 0.5% 实测数据。

## Evidence

[质询]该陈述中的具体数值（1.8% ± 0.5%）是基于7B/13B模型的线性外推，而非Qwen3-27B的实际实测数据。线性外推在模型规模变化时往往失效，且参考来源中并未提供该具体基准得分下降幅度的实证数据，属于缺乏直接证据支持的推测性结论。 | 参考来源[1][2][3]确认了Qwen3.6-27B-AWQ-INT4模型的存在及AWQ量化技术的应用，但未提供MMLU基准得分的具体下降幅度数据，无法直接支持'1.8% ± 0.5%'这一具体数值，仅能间接支持量化模型存在且性能保持较好的定性描述。

## Search Query

Qwen3-27B AWQ INT4 MMLU benchmark score degradation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00399/article/details/161864324&rut=e41dd7130426540450710d99dba426bbd4b95636ce279ab07451cbfa9a07eac5', 'type': 'ddg', 'title': 'Qwen3.6-27B-AWQ-INT4 模型部署与使用指南：高效量化模型实践手册-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00901/article/details/158275063&rut=621c2cedbba5698061b6c8cdc0fa46e8a85ede7d5975b35ed65e4b26c9ef5b8a', 'type': 'ddg', 'title': 'Qwen3.6-27B-AWQ-INT4：27B参数大语言模型实战部署与架构深度解析-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/158275063&rut=72d304f268e7e0fedc9935115e85aa859dbe5588f1e1c6a04788dcd361ad5b79', 'type': 'ddg', 'title': 'Qwen3.6-27B-AWQ-INT4：27B参数大语言模型实战部署与架构深度解析_霍璟尉-DeepSeek技术社区'}
