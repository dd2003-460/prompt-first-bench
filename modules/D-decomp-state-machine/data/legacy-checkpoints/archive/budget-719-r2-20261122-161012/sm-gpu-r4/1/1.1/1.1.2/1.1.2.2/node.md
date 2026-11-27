# N142: 激活值 (Activations) 显存占用估算：在 Batch Size=1 且使用 FlashAttention 等优化技术时，激活值开销通常小于 1GB；

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

激活值 (Activations) 显存占用估算：在 Batch Size=1 且使用 FlashAttention 等优化技术时，激活值开销通常小于 1GB；若 Batch Size > 1 或未启用优化，激活值随 Batch Size 线性增长，需根据最大并发数计算具体上限

## Corrected Claim

激活值 (Activations) 显存占用估算：在 Batch Size=1 且使用 FlashAttention 等优化技术时，激活值开销通常小于 1GB；若 Batch Size > 1 或未启用优化，激活值随 Batch Size 线性增长，需根据最大并发数计算具体上限

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了特定序列长度（32K）和特定批处理大小（Batch Size=1）的两种注意力机制对比，未涵盖父节点中提到的‘Batch Size > 1’时的线性增长规律，也未提供通用公式或不同参数下的估算方法，导致对父节点‘需根据最大并发数计算具体上限’这一关键指导原则的覆盖不完整。）
