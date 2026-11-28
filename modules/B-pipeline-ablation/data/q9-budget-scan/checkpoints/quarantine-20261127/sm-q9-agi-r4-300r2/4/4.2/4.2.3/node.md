# N67: TP=4 AllReduce 通信开销占比 C_comm ≈ (2 * hidden_dim * seq_len * batch_size * dtype_by

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

TP=4 AllReduce 通信开销占比 C_comm ≈ (2 * hidden_dim * seq_len * batch_size * dtype_bytes) / (T_compute * bandwidth_effective)，在 V100 300GB/s NVLink 下，若 T_compute < 5ms，通信占比 >20%，成为主要瓶颈

## Corrected Claim

TP=4 AllReduce 通信开销占比 C_comm ≈ (2 * hidden_dim * seq_len * batch_size * dtype_bytes) / (T_compute * bandwidth_effective)，在 V100 300GB/s NVLink 下，若 T_compute < 5ms，通信占比 >20%，成为主要瓶颈

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上分别对应带宽实测、具体算例验证和临界参数推导，彼此正交且不冗余。但存在两个主要问题：1. 完备性缺失：父节点强调 T_compute < 5ms 是瓶颈条件，但子节点2给出的单层耗时仅 3.5ms（未含层数累积），而子节点3直接假设 T_compute=5ms 进行推导，缺乏从'单层'到'总计算时间'的逻辑桥梁，也未解释为何选择 5ms 作为基准；2. 概念混淆：子节点3将 seq_len 替换为 'tokens' 并得出 78k 的临界值，这在物理上不合理（通常指单条序列长度或总 token 数需明确定义，且 78k 远超常规上下文窗口，暗示公式中变量定义与父节点不一致）。）
