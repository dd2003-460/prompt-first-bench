# N66: 修正 N23 中 T_decode 公式的分子项：Decode 阶段（每生成 1 个 token）的总计算量 FLOPs ≈ 2 * L_params + KV

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

修正 N23 中 T_decode 公式的分子项：Decode 阶段（每生成 1 个 token）的总计算量 FLOPs ≈ 2 * L_params + KV_Reading_FLOPs，其中 KV_Reading_FLOPs 主要取决于 KV Cache 读取带宽而非 FLOPs 计算，原公式 T_decode ≈ L * (M + KV_len) / (2 * FLOPS * MFU) 错误地将内存读取操作建模为 FLOPs 计算，应改为 T_decode ≈ (Weight_Size + KV_Cache_Size_per_token) / Memory_Bandwidth

## Corrected Claim

修正 N23 中 T_decode 公式的分子项：Decode 阶段（每生成 1 个 token）的总计算量 FLOPs ≈ 2 * L_params + KV_Reading_FLOPs，其中 KV_Reading_FLOPs 主要取决于 KV Cache 读取带宽而非 FLOPs 计算，原公式 T_decode ≈ L * (M + KV_len) / (2 * FLOPS * MFU) 错误地将内存读取操作建模为 FLOPs 计算，应改为 T_decode ≈ (Weight_Size + KV_Cache_Size_per_token) / Memory_Bandwidth

## Evidence

父节点级核验未通过：不完备（父节点的核心任务是‘修正公式’，即定义正确的理论模型（T_decode = Size/BW）。然而，唯一的子节点仅提供了‘代表性工作点’的具体数值计算案例，缺失了对修正后公式本身的定义、变量解释或通用推导。这导致子节点未能覆盖父节点‘修正公式’这一核心动作，仅覆盖了‘应用验证’方面，属于不完备。）

## Search Query

LLM decode phase latency calculation memory bandwidth bound vs compute bound
