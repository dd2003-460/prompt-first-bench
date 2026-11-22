# N260: Qwen3-27B在BF16精度下的HumanEval Pass@1基准得分需从官方评测数据中核实（当前假设为68.0%，标记为[待核验]），该数值是判断FP8

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113

## Claim

Qwen3-27B在BF16精度下的HumanEval Pass@1基准得分需从官方评测数据中核实（当前假设为68.0%，标记为[待核验]），该数值是判断FP8（67.8%）是否满足代码生成业务阈值的基准。

## Corrected Claim

Qwen3-27B在BF16精度下的HumanEval Pass@1基准得分需从官方评测数据中核实（当前假设为68.0%，标记为[待核验]），该数值是判断FP8（67.8%）是否满足代码生成业务阈值的基准。

## Evidence

[质询]参考来源均指向 Qwen3.6 或 Qwen3.8 版本，而非 Qwen3-27B，存在版本混淆风险；且 68.0% 的具体数值在提供的摘要中未直接出现，属于缺乏直接证据支持的假设值。 | 来源 [1] 和 [2] 涉及 Qwen 3.6 27B 的 HumanEval 评测，与 Qwen3-27B 主题高度相关但版本不完全匹配，且摘要未提供具体 68.0% 的数值，仅能间接支持该量级合理性，无法直接验证具体数值。

## Search Query

Qwen3-27B HumanEval Pass@1 benchmark score BF16

## Retrieval Sources

- {'url': 'https://www.heyneo.com/blog/evaluating-qwen-3-6-27b-benchmarking-case-study&rut=6ac8f79df6c54461759623add2d7e1fe7c9e0657a40e7be8b00a708ce3c3feda', 'type': 'ddg', 'title': 'Evaluating Qwen 3.6 27B: A Complete Benchmarking Case Study'}
- {'url': 'https://qevos.ai/blog/cn/2026-05-06-qwen36-27b-verilog-lora-finetuning.html&rut=fea8a13556df97dc5fb5b255f3465f7a840eb32587165d8f624516f18806ae79', 'type': 'ddg', 'title': 'Qwen3.6-27B Verilog微调全流程：训练、评估与HumanEval验证'}
- {'url': 'https://blog.csdn.net/liangjinhu/article/details/164183862&rut=a6a509f8e74bff9b487998cd33b34a6a6d8d0784c2d7f4310f4e98041b75497e', 'type': 'ddg', 'title': 'Qwen3.8-27B GSQ-RCO 量化部署实测：9.3GB 跑出超 BF16 精度，消费级显卡落地 27B 多模态'}
