# N179: N51的T_comm项量化：T_comm = (Model_Layers × Activation_Size) / (NVLink_Bandwidth × TP

- **status**: pending
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

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 825)
