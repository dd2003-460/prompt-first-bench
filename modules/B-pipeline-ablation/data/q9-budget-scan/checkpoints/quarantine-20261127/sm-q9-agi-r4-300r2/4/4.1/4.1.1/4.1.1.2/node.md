# N160: 工作点 B（平衡型/科研通用）：启用 MTP×2 且 η=0.7（混合任务场景），Throughput_eff = 15 * (1 + 0.7*1) = 25.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

工作点 B（平衡型/科研通用）：启用 MTP×2 且 η=0.7（混合任务场景），Throughput_eff = 15 * (1 + 0.7*1) = 25.5 tok/s，T_local(10k tokens) ≈ 392s；此配置下 KV Cache 压力中等，支持 max-num-seqs=8，稳定性优于工作点 A

## Corrected Claim

工作点 B（平衡型/科研通用）：启用 MTP×2 且 η=0.7（混合任务场景），Throughput_eff = 15 * (1 + 0.7*1) = 25.5 tok/s，T_local(10k tokens) ≈ 392s；此配置下 KV Cache 压力中等，支持 max-num-seqs=8，稳定性优于工作点 A

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 15*(1+0.7)=25.5 正确，时间估算 10000/25.5≈392s 正确，KV Cache 压力与并发数关系符合工程直觉。

## Search Query

speculative decoding K=2 vs K=4 tradeoff throughput stability vLLM
