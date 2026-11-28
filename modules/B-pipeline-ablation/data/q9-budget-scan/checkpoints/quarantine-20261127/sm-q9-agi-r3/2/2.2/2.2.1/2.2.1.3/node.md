# N161: 模型解析响应时间(T_parse)并非固定常数，而是与工具返回结果的Token长度线性相关：T_parse ≈ (N_return_tokens / Throu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

模型解析响应时间(T_parse)并非固定常数，而是与工具返回结果的Token长度线性相关：T_parse ≈ (N_return_tokens / Throughput_decode)，其中Throughput_decode在27B模型上约为15-20 tokens/s；若工具返回JSON包含大量数据，T_parse可能从50ms激增至500ms以上，成为主要瓶颈。

## Corrected Claim

模型解析响应时间(T_parse)并非固定常数，而是与工具返回结果的Token长度线性相关：T_parse ≈ (N_return_tokens / Throughput_decode)，其中Throughput_decode在27B模型上约为15-20 tokens/s；若工具返回JSON包含大量数据，T_parse可能从50ms激增至500ms以上，成为主要瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：解码吞吐量与Token数成线性关系符合LLM推理基本原理，27B模型15-20 tokens/s及对应延迟量级（50ms-500ms+）在工程实践中合理且自洽。
