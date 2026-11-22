# N56: 每步 KV Cache 读写体积量化：KV_Step_GB = (2 × 32 × 128 × Bytes_per_token) / (1024^3) × (S

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

每步 KV Cache 读写体积量化：KV_Step_GB = (2 × 32 × 128 × Bytes_per_token) / (1024^3) × (Seq_Len/Seq_Len) ≈ 0.00006 GB (每 token 增量)，但在生成阶段，每步需读取整个 KV Cache 历史，故有效带宽消耗为 KV_Total_GB × 2 (Read+Write)，需纳入分母。

## Corrected Claim

每步 KV Cache 读写体积量化：KV_Step_GB = (2 × 32 × 128 × Bytes_per_token) / (1024^3) × (Seq_Len/Seq_Len) ≈ 0.00006 GB (每 token 增量)，但在生成阶段，每步需读取整个 KV Cache 历史，故有效带宽消耗为 KV_Total_GB × 2 (Read+Write)，需纳入分母。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 每步增量计算符合 Transformer 架构原理（2×Head×Dim×Bytes），生成阶段需读取全部历史 KV 的带宽消耗描述符合自回归解码机制。
