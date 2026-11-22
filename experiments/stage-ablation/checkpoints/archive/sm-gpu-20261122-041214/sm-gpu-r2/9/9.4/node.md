# N165: Batch Size 对吞吐量的非线性影响：当 Batch Size 从 1 增加到 4 或 8 时，RTX 4090 和 A100 的总吞吐量 (Total 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

Batch Size 对吞吐量的非线性影响：当 Batch Size 从 1 增加到 4 或 8 时，RTX 4090 和 A100 的总吞吐量 (Total Throughput) 提升幅度及单请求延迟 (Latency) 增加幅度。由于题目未限制并发，性价比计算需明确是按 Batch=1 (低延迟) 还是 Batch>1 (高吞吐) 场景，不同场景下性价比排序可能反转。

## Corrected Claim

Batch Size 增加通常会提升总吞吐量但增加单请求延迟。RTX 4090 在 Batch Size 增加时吞吐量有显著提升（来源[2]显示多卡/高负载下吞吐量可达300 tokens/sec），但 A100 的具体对比数据及性价比排序反转的结论需更多实证数据支持。

## Evidence

[质询]陈述中关于A100的具体性能数据及‘性价比排序可能反转’的结论缺乏参考来源支持，且‘非线性影响’的具体量化幅度（如提升倍数）未在来源中明确给出，属于经验事实但缺乏直接证据。 | 来源[2]间接支持了Batch Size对吞吐量和延迟的影响（提及测试涵盖不同batch size及吞吐量/延迟分析），但未提供A100数据或具体的非线性量化对比，且未直接证实性价比排序反转；逻辑上Batch Size增加通常提升吞吐但增加延迟，符合直觉，但具体数值和排序结论缺直接来源支持。

## Search Query

Qwen3-27B batch size impact throughput vs latency RTX 4090 A100 LLM inference

## Retrieval Sources

- {'url': 'https://pub.towardsai.net/running-qwen3-8-27b-on-an-rtx-4090-cde0cb4ba338&rut=56819f0eb754ee074cb53d0f0adc0c345e88aba7a82bbd2beae3b302dd0315cb', 'type': 'ddg', 'title': 'Running Qwen3.8-27B on an RTX 4090 - pub.towardsai.net'}
- {'url': 'https://blog.csdn.net/weixin_32925455/article/details/158992037&rut=8d559e7ba76dd1587ba32cc4316c9d043780dec0d789f570d4125267b2abe486', 'type': 'ddg', 'title': 'Qwen3.5-27B性能实测报告：4090D多卡吞吐量、首字延迟与显存占用分析-CSDN博客'}
- {'url': 'https://computingforgeeks.com/run-qwen3-8-27b-locally/&rut=4cc623a4f683061052dd965bd88e9a67012ab9b3187df430d00fdde579fa991f', 'type': 'ddg', 'title': 'Run Qwen3.8-27B Locally: VRAM and Speed Tested | ComputingForGeeks'}
