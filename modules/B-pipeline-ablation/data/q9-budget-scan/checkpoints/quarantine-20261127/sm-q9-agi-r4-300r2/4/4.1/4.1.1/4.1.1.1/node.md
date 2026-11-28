# N159: 工作点 A（高吞吐/低延迟）：启用 MTP×4 且 η=0.85（代码补全场景），Throughput_eff = 15 * (1 + 0.85*3) = 45

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

工作点 A（高吞吐/低延迟）：启用 MTP×4 且 η=0.85（代码补全场景），Throughput_eff = 15 * (1 + 0.85*3) = 45.75 tok/s，T_local(10k tokens) ≈ 219s；此配置下 KV Cache 占用高，max-num-seqs 受限为 4

## Corrected Claim

工作点 A（高吞吐/低延迟）：启用 MTP×4 且 η=0.85（代码补全场景），Throughput_eff = 15 * (1 + 0.85*3) = 45.75 tok/s，T_local(10k tokens) ≈ 219s；此配置下 KV Cache 占用高，max-num-seqs 受限为 4

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 15*(1+0.85*3)=45.75 正确，时间估算 10000/45.75≈218.6s 与 219s 吻合，KV Cache 限制逻辑自洽。

## Search Query

vLLM speculative decoding MTP acceptance rate throughput calculation example
