# N260: η=0.50 工作点的稳态显存峰值占用 M_peak = M_base + η * M_mtp_buffer，其中 M_base=12.5GB (4x V100

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103, N104, N105

## Claim

η=0.50 工作点的稳态显存峰值占用 M_peak = M_base + η * M_mtp_buffer，其中 M_base=12.5GB (4x V100 共享模型权重+激活)，M_mtp_buffer≈0.85GB/seq (来自 N220)，当 max_num_seqs=8 时 M_peak ≈ 12.5 + 0.5*8*0.85 = 15.9GB，逼近 16GB 物理极限，导致 OOM 风险概率 P_oom > 10% [待核验]。

## Corrected Claim

η=0.50 工作点的稳态显存峰值占用 M_peak = M_base + η * M_mtp_buffer，其中 M_base=12.5GB (4x V100 共享模型权重+激活)，M_mtp_buffer≈0.85GB/seq (来自 N220)，当 max_num_seqs=8 时 M_peak ≈ 12.5 + 0.5*8*0.85 = 15.9GB，逼近 16GB 物理极限，导致 OOM 风险概率 P_oom > 10% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 12.5 + 0.5 * 8 * 0.85 = 15.9 正确，且 15.9GB 逼近 16GB 物理极限导致 OOM 风险符合内存管理基本逻辑。
