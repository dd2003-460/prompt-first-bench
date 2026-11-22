# N27: 性能基准测试误差源：不同推理框架（vLLM, TGI, llama.cpp）对同一硬件的吞吐量报告差异可达 10-20%，主要源于 KV Cache 管理策略和

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

性能基准测试误差源：不同推理框架（vLLM, TGI, llama.cpp）对同一硬件的吞吐量报告差异可达 10-20%，主要源于 KV Cache 管理策略和批处理大小不同；引用性能数据时必须标注框架版本和具体配置（如 batch_size=1, context_len=32k）。

## Corrected Claim

性能基准测试误差源：不同推理框架（vLLM, TGI, llama.cpp）对同一硬件的吞吐量报告差异可达 10-20%，主要源于 KV Cache 管理策略和批处理大小不同；引用性能数据时必须标注框架版本和具体配置（如 batch_size=1, context_len=32k）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference framework performance variance vLLM vs llama.cpp benchmark discrepancy
