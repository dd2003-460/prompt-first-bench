# N14: Qwen3-27B 在 W4A8 或 W4A16 量化下的权重大小（约 13.5GB）及对应的质量退化基准测试分数（相对 BF16 的下降百分比）。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

Qwen3-27B 在 W4A8 或 W4A16 量化下的权重大小（约 13.5GB）及对应的质量退化基准测试分数（相对 BF16 的下降百分比）。

## Corrected Claim

Qwen3-27B（或 Qwen3.8-27B）在 W4A8/W4A16 量化下的权重大小约为 13.5GB，但具体的质量退化基准测试分数需参考更详细的评测报告，当前来源未提供确切数值。

## Evidence

[质询]来源标题提及的是 'Qwen3.8-27B' 而非 'Qwen3-27B'，且摘要内容主要讨论推理速度（t/s）和硬件配置，未提供 W4A8/W4A16 量化下的具体权重大小（13.5GB）或质量退化基准测试分数，存在版本混淆及数据缺失风险。 | 来源 [1] 主题相关（涉及 Qwen 系列 27B 模型本地部署），但未直接提供 W4A8/W4A16 量化下的具体权重数值和质量退化分数，仅能确认该量级模型在消费级显卡上的可行性，缺乏具体量化指标的直接支持。

## Search Query

Qwen3-27B 4bit quantization quality degradation benchmark score drop

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2079983038264513650&rut=8b3de12c2cfec63114cca3429910393b88bbe8f0eb0e725593197bae0fa02b4a', 'type': 'ddg', 'title': '别被 167 t/s 骗了：4080 魔改 32G 跑 Qwen3.8-27B 的完整实测与踩坑记录'}
