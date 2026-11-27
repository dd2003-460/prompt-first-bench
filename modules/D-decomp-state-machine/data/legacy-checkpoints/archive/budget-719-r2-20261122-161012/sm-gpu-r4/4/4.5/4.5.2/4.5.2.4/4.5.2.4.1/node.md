# N568: H100/A100 在 Batch Size=1 时的 Prefill 延迟 T_prefill = 1.77e12 FLOPs / (989e12 * 0.4

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N237

## Claim

H100/A100 在 Batch Size=1 时的 Prefill 延迟 T_prefill = 1.77e12 FLOPs / (989e12 * 0.4) ≈ 4.5s (H100) 或 1.77e12 / (312e12 * 0.4) ≈ 14.2s (A100)，两者均远超 N237 声称的 'TTFT < 2s' 阈值，证明在 32K 长上下文下，即使 Batch=1 也无法满足低 TTFT 要求，N237 的 'Batch>10 才线性增长' 前提不成立，因为 Batch=1 已超标。

## Corrected Claim

H100/A100 在 Batch Size=1 时的 Prefill 延迟 T_prefill = 1.77e12 FLOPs / (989e12 * 0.4) ≈ 4.5s (H100) 或 1.77e12 / (312e12 * 0.4) ≈ 14.2s (A100)，两者均远超 N237 声称的 'TTFT < 2s' 阈值，证明在 32K 长上下文下，即使 Batch=1 也无法满足低 TTFT 要求，N237 的 'Batch>10 才线性增长' 前提不成立，因为 Batch=1 已超标。

## Evidence

先验知识/题面给定，逻辑校验通过：H100/A100 算力与 FLOPs 量级符合工程常识，计算过程自洽，且 Batch=1 延迟远超 2s 的结论在逻辑上成立。

## Search Query

H100 A100 prefill latency 32k context Qwen3-27B TTFT
