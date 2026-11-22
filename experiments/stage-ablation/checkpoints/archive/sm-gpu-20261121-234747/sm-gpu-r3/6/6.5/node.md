# N142: W4权重大小计算：Size_W4 = 27e9 * 0.5 bytes = 13.5GB（注意：W4通常为per-group量化，group_size=128，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

W4权重大小计算：Size_W4 = 27e9 * 0.5 bytes = 13.5GB（注意：W4通常为per-group量化，group_size=128，需额外存储scale因子，额外占用约2-4%）

## Corrected Claim

W4权重大小计算：Size_W4 = 27e9 * 0.5 bytes = 13.5GB（注意：W4通常为per-group量化，group_size=128，需额外存储scale因子，额外占用约2-4%）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了量化元数据开销（Scale）、量化模式差异（Zero-point）、以及非量化层（Embedding/LM Head）的显存影响。这三个方面在显存计算中是相互独立且必要的，共同构成了从‘纯权重估算’到‘实际部署显存’的完整修正链条，不存在重叠或逻辑矛盾。）
