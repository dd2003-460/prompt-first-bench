# N45: Qwen3-27B 总参数量验证：Total = 4.295e9 (Attn) + 8.657e9 (FFN) + 1.246e9 (Embed) ≈ 14.1

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Qwen3-27B 总参数量验证：Total = 4.295e9 (Attn) + 8.657e9 (FFN) + 1.246e9 (Embed) ≈ 14.198e9？ 注意：这与 27B 不符。需检查 Qwen3 是否使用 GQA 导致 Attention 参数减少，或者 27B 是包含其他组件。实际上 Llama 30B 的 FFN 更大。重新计算：若 Total=27e9，则 27e9 - 1.246e9 = 25.754e9 用于 Transformer Blocks。Per Block = 25.754e9 / 64 ≈ 402.4e6。Per Block Attn = 4*4096*4096 ≈ 67.1e6。Per Block FFN = 402.4e6 - 67.1e6 = 335.3e6。3 * 4096 * intermediate = 335.3e6 => intermediate ≈ 27,147。这与给定的 11008 不符。说明 N8 中的参数可能对应的是 14B 或 32B 的变体，或者 N8 的参数本身有误/需核验。[待核验：Qwen3-27B 的确切 intermediate_size 和 n_layers，N8 中的参数组合算出的参数量约为 14.2B，而非 27B。若为 27B，intermediate_size 应约为 27000 或 n_layers 更多。]

## Corrected Claim

Qwen3-27B 的总参数量确认为 27B（来源 [1], [2] 支持），但基于给定参数（hidden=4096, layers=64, inter=11008）计算出的参数量约为 14.2B，与 27B 不符。这表明 N8 中提供的架构参数组合（特别是 intermediate_size 或 n_layers）与 27B 模型的实际配置不匹配，需查阅官方模型卡获取确切的 intermediate_size（通常 27B 模型的 FFN 维度会显著大于 11008 以容纳更多参数）或层数。

## Evidence

[质询]参考来源仅确认了模型名称（Qwen3.6-27B）和总参数量级（27B），但未提供具体的架构超参数（如 intermediate_size, n_layers, hidden_size 等），无法直接验证 N45 中关于参数分解计算的具体数值（如 intermediate_size 应为 27000 还是 11008）是否准确。此外，来源标题提及 'Qwen3.6' 而节点提及 'Qwen3'，存在版本命名上的细微差异，虽大概率指代同一系列，但缺乏精确的架构文档支持。 | 来源 [1] 和 [2] 确认了 Qwen3.6-27B 存在且参数量为 27B，支持了节点中 'Total=27e9' 的前提假设，但来源未提供具体的 FFN 中间层维度（intermediate_size）或层数等架构细节，无法直接证实或证伪节点中推导出的 'intermediate_size ≈ 27,147' 或 'N8 参数有误' 的具体结论，属于经验事实且缺乏直接来源支持。

## Search Query

Qwen3 27B exact architecture parameters n_layers intermediate_size config.json

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00208/article/details/157234872&rut=fd32cd314b47879c1868e58111da6abce308d377a7d7d8eebea9661ab840bb2e', 'type': 'ddg', 'title': 'Qwen3.6-27B最佳实践：3大采样参数组合+8万token输出设置，解锁模型全部潜力-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_33437929/article/details/162111963&rut=313784d10a9f35f21b33929d480cfc1d1299e59fa217f79a5ba093ee37c2c4a6', 'type': 'ddg', 'title': 'Qwen3.6-27B开源模型：27B参数量下的长上下文推理优化实践-CSDN博客'}
