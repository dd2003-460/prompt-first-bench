# N188: 分层加权失效折扣系数 D_eff 的积分计算：D_eff = Σ (ByteShare_i) * (1 - P_update_i)，其中 ByteShare_i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N72

## Claim

分层加权失效折扣系数 D_eff 的积分计算：D_eff = Σ (ByteShare_i) * (1 - P_update_i)，其中 ByteShare_i = (S_i * F_i) / Total_Bytes，P_update_i = 1 - exp(-u * Δt_i)，Δt_i = 1/F_i（平均访问间隔）。对于头部对象（F_i > 1000/天），Δt_i < 0.001天，P_update_i < 0.001，折扣 ≈ 1。对于尾部对象（F_i < 1/天），Δt_i > 1天，P_update_i > 0.01，折扣 < 0.99。由于头部对象贡献 90% 的请求字节（N50），D_eff 主要由头部对象决定。估算：Top 10% 对象贡献 90% 字节，其平均 F_i ≈ 50,000/天，Δt ≈ 0.00002天，P_update ≈ 0.0000002，折扣 ≈ 1.0。Top 10-50% 对象贡献 9% 字节，平均 F_i ≈ 500/天，Δt ≈ 0.002天，P_update ≈ 0.00002，折扣 ≈ 0.99998。因此，D_eff ≈ 0.9999 以上，折扣极小。N72 中提到的 0.368-0.99 范围是基于 T_res 而非访问间隔的误用。

## Corrected Claim

分层加权失效折扣系数 D_eff 的积分计算：D_eff = Σ (ByteShare_i) * (1 - P_update_i)，其中 ByteShare_i = (S_i * F_i) / Total_Bytes，P_update_i = 1 - exp(-u * Δt_i)，Δt_i = 1/F_i（平均访问间隔）。对于头部对象（F_i > 1000/天），Δt_i < 0.001天，P_update_i < 0.001，折扣 ≈ 1。对于尾部对象（F_i < 1/天），Δt_i > 1天，P_update_i > 0.01，折扣 < 0.99。由于头部对象贡献 90% 的请求字节（N50），D_eff 主要由头部对象决定。估算：Top 10% 对象贡献 90% 字节，其平均 F_i ≈ 50,000/天，Δt ≈ 0.00002天，P_update ≈ 0.0000002，折扣 ≈ 1.0。Top 10-50% 对象贡献 9% 字节，平均 F_i ≈ 500/天，Δt ≈ 0.002天，P_update ≈ 0.00002，折扣 ≈ 0.99998。因此，D_eff ≈ 0.9999 以上，折扣极小。N72 中提到的 0.368-0.99 范围是基于 T_res 而非访问间隔的误用。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导自洽，基于Zipf分布假设的数值量级估算（头部对象高频访问导致更新概率极低，折扣系数接近1）符合数学逻辑，且无来源矛盾。
