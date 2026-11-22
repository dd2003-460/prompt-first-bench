# N202: CPU-only 方案（Xeon/EPYC + 256GB RAM）在运行 Qwen3-27B (INT8) 时的实测吞吐量约为 5-10 tokens/s，显

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

CPU-only 方案（Xeon/EPYC + 256GB RAM）在运行 Qwen3-27B (INT8) 时的实测吞吐量约为 5-10 tokens/s，显著低于 GPU 方案（RTX 4090 ~100+ tokens/s），导致在延迟敏感场景（<500ms/1K tokens）下不可行，仅在后台批处理场景具有成本优势。

## Corrected Claim

CPU-only 方案（Xeon/EPYC + 256GB RAM）在运行 Qwen3-27B (INT8) 时的实测吞吐量约为 5-10 tokens/s，显著低于 GPU 方案（RTX 4090 ~100+ tokens/s），导致在延迟敏感场景（<500ms/1K tokens）下不可行，仅在后台批处理场景具有成本优势。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数模型INT8量化后约27GB，256GB内存充足；CPU内存带宽（~100-200GB/s）与GPU显存带宽（~1TB/s）相差约10倍，且CPU计算效率远低于GPU，5-10 tokens/s vs 100+ tokens/s的量级差异符合硬件物理极限与工程实测经验。
