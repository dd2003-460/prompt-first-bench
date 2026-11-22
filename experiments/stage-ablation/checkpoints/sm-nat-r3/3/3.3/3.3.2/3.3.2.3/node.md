# N189: ΔH_max 公式中的 (P_head - P_tail) 项需明确为字节加权请求概率差：ΔP_byte = (Σ_{i∈Top10%} p_i s_i / Σ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

ΔH_max 公式中的 (P_head - P_tail) 项需明确为字节加权请求概率差：ΔP_byte = (Σ_{i∈Top10%} p_i s_i / Σ_{all} p_i s_i) - (Σ_{i∈Tail90%} p_i s_i / Σ_{all} p_i s_i)。由于头部对象通常较小，字节加权后的 P_head_byte 可能显著低于请求加权 P_head_req，需通过数值积分计算。

## Corrected Claim

ΔH_max 公式中的 (P_head - P_tail) 项需明确为字节加权请求概率差：ΔP_byte = (Σ_{i∈Top10%} p_i s_i / Σ_{all} p_i s_i) - (Σ_{i∈Tail90%} p_i s_i / Σ_{all} p_i s_i)。由于头部对象通常较小，字节加权后的 P_head_byte 可能显著低于请求加权 P_head_req，需通过数值积分计算。

## Evidence

先验知识/题面给定，逻辑校验通过
