# N241: RTX 4090 运行 Qwen3-27B W4 量化时的 KV Cache 显存占用：若 KV Cache 保持 FP16 (常见配置)，计算同 N87 为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

RTX 4090 运行 Qwen3-27B W4 量化时的 KV Cache 显存占用：若 KV Cache 保持 FP16 (常见配置)，计算同 N87 为 2.0 GB (单序列 32K)；若 KV Cache 也量化为 INT8，则占用减半为 1.0 GB。

## Corrected Claim

RTX 4090 运行 Qwen3-27B W4 量化时的 KV Cache 显存占用：若 KV Cache 保持 FP16 (常见配置)，计算同 N87 为 2.0 GB (单序列 32K)；若 KV Cache 也量化为 INT8，则占用减半为 1.0 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（层数、头数、头维度）符合主流 LLM 设计，KV Cache 计算公式 2 * L * H * D * S * Bytes 在 FP16 下约为 2.0 GB，INT8 减半为 1.0 GB，量级与逻辑均自洽。
