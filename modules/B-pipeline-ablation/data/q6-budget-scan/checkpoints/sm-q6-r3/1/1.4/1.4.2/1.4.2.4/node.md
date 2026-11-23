# N148: 混合策略中TLS重新握手对P99延迟的贡献 ΔP99_tls = P_rehandshake * (t_handshake - t_reuse)，其中 t_ha

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

混合策略中TLS重新握手对P99延迟的贡献 ΔP99_tls = P_rehandshake * (t_handshake - t_reuse)，其中 t_handshake - t_reuse ≈ 20-50ms，若 P_rehandshake = 0.005，则 ΔP99_tls ≈ 0.1-0.25ms，对整体P99影响可忽略；若 P_switch 较高（> 0.5），则需考虑证书统一或会话同步机制。

## Corrected Claim

混合策略中TLS重新握手对P99延迟的贡献 ΔP99_tls = P_rehandshake * (t_handshake - t_reuse)，其中 t_handshake - t_reuse ≈ 20-50ms，若 P_rehandshake = 0.005，则 ΔP99_tls ≈ 0.1-0.25ms，对整体P99影响可忽略；若 P_switch 较高（> 0.5），则需考虑证书统一或会话同步机制。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（0.005 * 20ms = 0.1ms, 0.005 * 50ms = 0.25ms），量级符合TLS握手与复用的典型延迟差异，结论逻辑自洽。
