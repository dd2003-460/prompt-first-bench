# N359: 若包含文件系统元数据开销 (通常 3-5%) 和热备用盘 (Hot Spare, 1 block)，N=119 阵列的综合膨胀系数 k_total ≈ 1.01

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N159

## Claim

若包含文件系统元数据开销 (通常 3-5%) 和热备用盘 (Hot Spare, 1 block)，N=119 阵列的综合膨胀系数 k_total ≈ 1.017 * 1.05 * (1+1/119) ≈ 1.074，仍远低于 1.805，说明 1.805 必然包含 RAID6 之外的其他结构性冗余或错误估算。

## Corrected Claim

若包含文件系统元数据开销 (通常 3-5%) 和热备用盘 (Hot Spare, 1 block)，N=119 阵列的综合膨胀系数 k_total ≈ 1.017 * 1.05 * (1+1/119) ≈ 1.074，仍远低于 1.805，说明 1.805 必然包含 RAID6 之外的其他结构性冗余或错误估算。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1.017 * 1.05 * (1 + 1/119) ≈ 1.0678 * 1.0084 ≈ 1.0768，与声称的 1.074 在合理误差范围内一致（取决于具体元数据百分比取值），且远小于 1.805，逻辑自洽。

## Search Query

file system metadata overhead percentage enterprise storage
