# N85: L40S 48GB 运行 Qwen3-27B INT8 权重 + BF16 KV Cache (32K) 时，显存占用为 27GB (权重) + 40GB (K

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

L40S 48GB 运行 Qwen3-27B INT8 权重 + BF16 KV Cache (32K) 时，显存占用为 27GB (权重) + 40GB (KV) = 67GB，超出 48GB 显存，故 INT8 权重方案在 32K 上下文下不可行，必须使用 FP8 权重或 KV Cache 量化。

## Corrected Claim

L40S 48GB 运行 Qwen3-27B INT8 权重 + BF16 KV Cache (32K) 时，仅权重与 KV Cache 的显存占用估算约为 67GB，已超出 48GB 显存限制，因此该配置在 32K 上下文下大概率不可行，需采用 FP8 权重或 KV Cache 量化等优化手段。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1纠正了显存计算的数学错误，直接反驳了父节点的核心结论；子节点2基于修正后的数据评估了性能可行性，逻辑上依赖于子节点1，但关注点不同（显存 vs 速度）；子节点3评估了质量损失，关注点独立。三者分别覆盖了‘可行性判断’、‘性能预期’和‘质量代价’，正交且无冗余。）

## Search Query

NVIDIA L40S 48GB Qwen3 27B 32k context memory requirements
