# N11: 显存带宽对 Token 生成速率 (Tokens/s) 的物理限制公式为 Throughput ≈ Memory_Bandwidth_GBps / Bytes_

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

显存带宽对 Token 生成速率 (Tokens/s) 的物理限制公式为 Throughput ≈ Memory_Bandwidth_GBps / Bytes_per_token_accessed，其中 Bytes_per_token_accessed 取决于权重大小和 KV Cache 读取量

## Corrected Claim

显存带宽对 Token 生成速率 (Tokens/s) 的物理限制公式为 Throughput ≈ Memory_Bandwidth_GBps / Bytes_per_token_accessed，其中 Bytes_per_token_accessed 取决于权重大小和 KV Cache 读取量

## Evidence

父节点级核验未通过：不完备（子节点分别阐述了‘分子（每Token读取量）’和‘分母/最终结果（吞吐率计算）’，两者逻辑上互补且不重叠，因此正交性好。但是，父节点定义的通用物理限制公式中明确包含 'Batch Size' 隐含因素（通常 Throughput 随 Batch Size 变化而改变，或者至少 Bytes_per_token 的定义需澄清是单请求还是总批次），以及更关键的：父节点公式是通用的，但子节点仅覆盖了 'RTX 4090' 这一特定硬件和 '32K/Batch=1' 这一特定场景，未覆盖公式中其他变量（如不同带宽、不同模型大小导致的 Bytes_per_token 变化规律）的通用解释或推导过程，导致对父节点“物理限制公式”本身的完备性支撑不足（即只给了一个实例，没解释公式本身的构成逻辑）。）
