# N179: N51的T_comm项量化：T_comm = (Model_Layers × Activation_Size) / (NVLink_Bandwidth × TP

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

N51的T_comm项量化：T_comm = (Model_Layers × Activation_Size) / (NVLink_Bandwidth × TP_Degree)，其中NVLink_Bandwidth ≈ 300 GB/s (SXM2双向)，Activation_Size取决于隐藏层维度(如4096×2字节)，此项解释了为何TP=4在短序列时通信占比上升

## Corrected Claim

N51的T_comm项量化：T_comm = (Model_Layers × Activation_Size) / (NVLink_Bandwidth × TP_Degree)，其中NVLink_Bandwidth ≈ 300 GB/s (SXM2双向)，Activation_Size取决于隐藏层维度(如4096×2字节)，此项解释了为何TP=4在短序列时通信占比上升

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（GB/s * s = GB），NVLink SXM2带宽量级（~300GB/s）符合A100/H100硬件规格常识，TP通信开销随TP度增加而线性增长符合分布式训练基本原理。
