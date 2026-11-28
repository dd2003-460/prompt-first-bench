# N268: 在 H_shift=1.0 nats 且 η=0.40 的高偏移工作点下，MTP×4 的第 3 步接受率通常降至 0.50-0.60 区间，导致有效加速比 S_

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107

## Claim

在 H_shift=1.0 nats 且 η=0.40 的高偏移工作点下，MTP×4 的第 3 步接受率通常降至 0.50-0.60 区间，导致有效加速比 S_eff 从 3.4 降至约 2.2；此时 MTP 带来的延迟节省 ΔT_mtp ≈ (3.4-2.2)*T_token_gen ≈ 1.2 * 22ms ≈ 26ms/token，若 Critic 验证延迟 T_critic >> 26ms*N_tokens，则 MTP 对端到端时间的贡献 < 5%，建议降级为 MTP×2 以节省 KV Cache 显存用于增加并发。

## Corrected Claim

在 H_shift=1.0 nats 且 η=0.40 的高偏移工作点下，MTP×4 的第 3 步接受率通常降至 0.50-0.60 区间，导致有效加速比 S_eff 从 3.4 降至约 2.2；此时 MTP 带来的延迟节省 ΔT_mtp ≈ (3.4-2.2)*T_token_gen ≈ 1.2 * 22ms ≈ 26ms/token，若 Critic 验证延迟 T_critic >> 26ms*N_tokens，则 MTP 对端到端时间的贡献 < 5%，建议降级为 MTP×2 以节省 KV Cache 显存用于增加并发。

## Search Query

multi-token prediction acceptance rate long chain of thought reasoning degradation
