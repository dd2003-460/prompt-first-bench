# N31: 性价比综合排序公式定义：Cost_Efficiency_Score = (Throughput_Tokens_per_sec * Quality_Factor)

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比综合排序公式定义：Cost_Efficiency_Score = (Throughput_Tokens_per_sec * Quality_Factor) / (Total_TCO_3yr_USD)。其中 Quality_Factor 为量化后的基准测试得分归一化值（BF16=1.0, INT8=0.95, W4=0.90 [待核验具体系数]），Total_TCO 包含 CapEx、OpEx 及隐性成本。

## Corrected Claim

性价比综合排序公式定义为：Cost_Efficiency_Score = (Throughput_Tokens_per_sec * Quality_Factor) / (Total_TCO_3yr_USD)。其中 Quality_Factor 为量化后的基准测试得分归一化值（具体系数需根据实际模型精度评估确定，常见参考值如 BF16=1.0, INT8≈0.95, W4≈0.90），Total_TCO 包含 CapEx、OpEx 及隐性成本。

## Evidence

[质询]该公式为特定场景下的自定义指标，缺乏通用标准支持；且Quality_Factor的具体系数（INT8=0.95, W4=0.90）属于经验性假设，不同模型和任务下精度损失差异巨大，固定系数缺乏普适性依据。 | 参考来源[1]讨论的是政府采购中的‘性价比法’（Price-Performance Ratio），与AI推理成本效率公式主题完全无关，无法提供外部支持；该公式逻辑自洽但属于经验性定义，具体系数缺乏来源验证。

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E6%80%A7%E4%BB%B7%E6%AF%94%E6%B3%95/10596797&rut=569ae9872be836e900d48ac808bef30b3b81747ee7453f5f38f4a9058b1f7d62', 'type': 'ddg', 'title': '性价比法_百度百科'}
