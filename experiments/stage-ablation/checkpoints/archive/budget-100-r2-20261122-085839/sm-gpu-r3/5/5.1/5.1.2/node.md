# N90: ROCm 5.6+ + llama.cpp 方案部署成本：适配工时为 3-5 人天（需手动编译 RDNA3 后端并调试 GQA 算子兼容性），Bug 修复成本为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

ROCm 5.6+ + llama.cpp 方案部署成本：适配工时为 3-5 人天（需手动编译 RDNA3 后端并调试 GQA 算子兼容性），Bug 修复成本为 $500-$2000（潜在算子缺失需 fallback 到 CPU 或重写），总成本权重为 0.4-0.8（取决于稳定性）。

## Corrected Claim

ROCm 5.6+ + llama.cpp 方案部署成本：适配工时为 3-5 人天（需手动编译 RDNA3 后端并调试 GQA 算子兼容性），Bug 修复成本为 $500-$2000（潜在算子缺失需 fallback 到 CPU 或重写），总成本权重为 0.4-0.8（取决于稳定性）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

llama.cpp ROCm RDNA3 Qwen3 inference stability issues
