# N191: Intel Max 1550 的 FP8 算力真实性核验：官方规格表中 '2.5 PFLOPS (sparse)' 通常指理论峰值，实际 LLM 推理中由于稀疏

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

Intel Max 1550 的 FP8 算力真实性核验：官方规格表中 '2.5 PFLOPS (sparse)' 通常指理论峰值，实际 LLM 推理中由于稀疏度限制和内存带宽瓶颈，有效算力通常仅为峰值的 30-50%，即实际可用算力约为 0.75-1.25 PFLOPS，需据此修正 Prefill 阶段吞吐量估算 [待核验]

## Corrected Claim

Intel Max 1550 的官方规格 '2.5 PFLOPS (sparse)' 为理论峰值。实际 LLM 推理中，受稀疏度实现难度和内存带宽瓶颈影响，有效算力通常低于峰值，具体效率需参考实际基准测试数据，一般经验估计可能在峰值的 30-50% 左右，但具体数值需实证验证。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点2存在逻辑重叠和数值冲突。子节点1将有效算力限定为稠密峰值的50%（1.25 PFLOPS），而子节点2给出一个范围（0.75-1.25 PFLOPS，即峰值的30-50%）。子节点1实际上是子节点2上限情况的特例，两者在“有效算力估算”这一核心维度上不正交。此外，子节点3直接使用了子节点1/2得出的算力数值进行计算，属于推导结果，与子节点1/2的“估算过程”存在包含关系，而非完全独立的正交维度。）

## Search Query

Intel Max 1550 FP8 sparse FLOPS real-world inference performance
