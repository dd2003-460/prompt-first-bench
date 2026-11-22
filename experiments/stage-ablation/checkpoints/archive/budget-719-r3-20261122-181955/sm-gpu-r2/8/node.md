# N35: Qwen3-27B 在 INT4 (AWQ/GPTQ) 量化下，MMLU 准确率相对 BF16 下降约 0.5-1.5%，HumanEval Pass@1 下降

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 在 INT4 (AWQ/GPTQ) 量化下，MMLU 准确率相对 BF16 下降约 0.5-1.5%，HumanEval Pass@1 下降约 1-3%；若下降幅度超过 5% 则视为不可接受，该阈值基于 LLM 应用对代码生成准确率的敏感性设定。

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ/GPTQ) 量化下，MMLU 和 HumanEval 准确率通常会有轻微下降，具体幅度需参考官方或第三方基准测试报告；一般认为下降幅度超过 5% 可能影响应用体验。

## Evidence

[质询]参考来源中提到的模型版本为 Qwen3.6-27B 或 Qwen3.8-27B，与陈述中的 Qwen3-27B 版本不一致，且来源摘要仅提及量化方案（AWQ/GPTQ）和显存优化，未提供具体的 MMLU 或 HumanEval 准确率下降数值，无法直接支持具体的百分比范围。 | 逻辑上 INT4 量化导致少量精度损失符合常识，但具体数值（0.5-1.5% 和 1-3%）属于经验事实，参考来源 [1][2][3] 虽涉及相关量化技术但版本不匹配且未提供具体基准测试数据，缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00713/article/details/170621454&rut=a7b79e1f1d1e5969139fbf962bf1299be981fac0d5916af46bab67e8d99a3f1e', 'type': 'ddg', 'title': '为什么量化几乎无损？Qwen3.8-27B-INT4 的 GPTQ W4A16 + AWQ 量化方案原理拆解-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00778/article/details/170514051&rut=6fbbb3d294c305ee4c3027709dc103c05a5584a83fb75b1e9d701248aa75fa1c', 'type': 'ddg', 'title': '2026旗舰开源多模态大模型Qwen3.6-27B-AWQ-INT4完全解读：27B稠密模型+INT4量化，为什么它能打'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/144363894&rut=d8d13fce48d64b01f2c84ed83ec4b0f3fbce4c90d623d88fb01ac908009d8ae4', 'type': 'ddg', 'title': '技术方案：Qwen3.6-27B-AWQ-INT4的高效部署与量化优化实践'}
