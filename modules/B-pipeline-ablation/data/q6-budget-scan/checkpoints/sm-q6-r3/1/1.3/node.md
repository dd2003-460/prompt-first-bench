# N8: 公有云CDN带宽峰值支持能力：公有云CDN单区域带宽峰值上限 B_cloud_max 需满足 B_cloud_max ≥ B_peak，其中 B_peak = 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

公有云CDN带宽峰值支持能力：公有云CDN单区域带宽峰值上限 B_cloud_max 需满足 B_cloud_max ≥ B_peak，其中 B_peak = (2TB/8) / 86400 * 峰值系数 k_peak，k_peak通常取3-5

## Corrected Claim

公有云CDN带宽峰值支持能力：公有云CDN单区域带宽峰值上限 B_cloud_max 需满足 B_cloud_max ≥ B_peak，其中 B_peak = (2TB/8) / 86400 * 峰值系数 k_peak，k_peak通常取3-5

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上正交，分别涵盖了峰值计算、计费影响和弹性成本。但存在完备性问题：父节点的核心是‘带宽峰值支持能力’（即技术上限 B_cloud_max 是否满足需求），而子节点1虽然指出了带宽不是瓶颈，但子节点2和3完全偏离了‘技术能力/上限’这一主题，转而讨论‘成本’和‘计费模式’。父节点并未提及成本或计费策略，因此子节点2和3属于范围蔓延（Scope Creep），未严格围绕父节点定义的‘支持能力’进行分解。）

## Search Query

Alibaba Cloud CDN bandwidth limit per region peak traffic
