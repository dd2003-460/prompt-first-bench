# N339: W7900 上 FP8/INT8 量化内核缺失的具体影响：ROCm 6.0 对 RDNA3 的 FP8 支持仅限于部分 GEMM 操作，Qwen3-27B 的 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117

## Claim

W7900 上 FP8/INT8 量化内核缺失的具体影响：ROCm 6.0 对 RDNA3 的 FP8 支持仅限于部分 GEMM 操作，Qwen3-27B 的 KV Cache 量化至 FP8 需依赖 `compressed-tensors` 库，若该库在 ROCm 下未优化，KV Cache 写入/读取带宽利用率下降至理论值的 60-70%，导致 Decode 阶段吞吐从理论 576 GB/s 上限降至有效 ~350-400 GB/s，实际 tokens/s 下降 25-35%。

## Corrected Claim

ROCm 6.0 对 RDNA3 的 FP8 支持可能不完整，Qwen3-27B 的 KV Cache 量化若依赖未充分优化的库（如 compressed-tensors），可能导致 KV Cache 读写带宽利用率下降，进而降低 Decode 阶段吞吐，但具体性能损失比例需实测验证。

## Evidence

[质询]该陈述包含大量具体的经验性数值（如带宽利用率60-70%、吞吐下降25-35%、具体库名compressed-tensors在ROCm下的特定表现），这些属于硬件/软件生态的经验事实，无法从第一性原理推导，且缺乏来源支持，存在数值臆测风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

ROCm RDNA3 FP8 KV cache quantization performance penalty vLLM
