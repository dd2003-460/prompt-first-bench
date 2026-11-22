# N110: Qwen3-27B 预填充阶段 (Prefill) 的理论计算量 (FLOPs) 计算公式为 2 * N_params * L，其中 N_params=27e9

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

Qwen3-27B 预填充阶段 (Prefill) 的理论计算量 (FLOPs) 计算公式为 2 * N_params * L，其中 N_params=27e9, L=32768，计算结果约为 1.77 TFLOPs。

## Corrected Claim

Qwen3-27B 预填充阶段 (Prefill) 的理论计算量 (FLOPs) 计算公式为 2 * N_params * L，其中 N_params=27e9, L=32768，计算结果约为 1.77 TFLOPs。

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 27e9 * 32768 = 1.769472e15 ≈ 1.77 TFLOPs，计算正确且符合Transformer预填充阶段计算量估算公式。
