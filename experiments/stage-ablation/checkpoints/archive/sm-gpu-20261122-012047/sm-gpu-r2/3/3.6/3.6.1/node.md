# N108: 在 MMLU 复杂推理子集（如 GSM8K, MATH）上，Qwen3-27B INT4 (AWQ) 量化相比 BF16 的准确率下降幅度约为 3-5 个百分点

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

在 MMLU 复杂推理子集（如 GSM8K, MATH）上，Qwen3-27B INT4 (AWQ) 量化相比 BF16 的准确率下降幅度约为 3-5 个百分点，低于早期 GPTQ 方案的 8-10% 下降，得益于 AWQ 的激活感知量化策略。

## Corrected Claim

在 MMLU 复杂推理子集上，Qwen3-27B INT4 (AWQ) 量化相比 BF16 的准确率下降幅度通常低于早期 GPTQ 方案，得益于 AWQ 的激活感知量化策略，但具体下降幅度（如 3-5%）需特定基准测试数据支持。

## Evidence

[质询]参考来源均针对 'Qwen3.8' 系列模型（且为 GGUF 格式或 9B 蒸馏版），与陈述中的 'Qwen3-27B' 及 'AWQ INT4' 量化方案不匹配，无法提供直接证据支持具体的 3-5% 下降幅度及与 GPTQ 的对比数据。 | 逻辑上 AWQ 优于 GPTQ 符合量化领域共识，但具体数值（3-5% vs 8-10%）属于经验事实，且参考来源 [1][2] 主题（Qwen3.8/GGUF/9B）与事实节点（Qwen3-27B/AWQ）不相关，无可用外部证据支持具体数值。

## Search Query

Qwen3-27B INT4 AWQ quantization MMLU GSM8K accuracy drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00688/article/details/152594884&rut=2ea9d2926423814f0c72df18929bb87fe87fd51d21ec45624adbbec869aadb02', 'type': 'ddg', 'title': '数据说话：Qwen3.8-27B-Uncensored-GGUF 基准评测全解读（MMLU、GSM8K 与安全测试）'}
- {'url': 'https://blog.csdn.net/gitblog_00378/article/details/153459748&rut=5b1d1a4da15211e9555a92d8c2221fcd48fd65875f44354fd5c93737c21e637a', 'type': 'ddg', 'title': 'Qwen3.8-9B 数学与代码能力实测：从 GSM8K 到 MMLU 的评测结果全解读-CSDN博客'}
