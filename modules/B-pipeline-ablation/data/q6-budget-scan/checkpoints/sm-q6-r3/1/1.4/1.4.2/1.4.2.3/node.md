# N147: 混合策略中因证书不同导致的路由切换TLS重新握手概率 P_rehandshake：若自建POP与公有云CDN使用不同证书，P_rehandshake = P_s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

混合策略中因证书不同导致的路由切换TLS重新握手概率 P_rehandshake：若自建POP与公有云CDN使用不同证书，P_rehandshake = P_switch * (1 - r_resume_same_cert)，其中 r_resume_same_cert 为同证书下会话复用率（典型 95%），因此 P_rehandshake ≈ P_switch * 0.05，若 P_switch = 0.1，则 P_rehandshake = 0.005。

## Corrected Claim

混合策略中因证书不同导致的路由切换TLS重新握手概率 P_rehandshake：若自建POP与公有云CDN使用不同证书，P_rehandshake = P_switch * (1 - r_resume_same_cert)，其中 r_resume_same_cert 为同证书下会话复用率（典型 95%），因此 P_rehandshake ≈ P_switch * 0.05，若 P_switch = 0.1，则 P_rehandshake = 0.005。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合概率论基本逻辑，数值计算（0.1 * 0.05 = 0.005）准确，且95%的会话复用率符合TLS工程常识。
