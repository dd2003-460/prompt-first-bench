# N34: 自建边缘节点的平均故障恢复时间（MTTR）通常为 4-8 小时（含硬件更换与配置同步），而公有云 CDN 的 MTTR 通常 < 15 分钟（自动故障转移），导

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

自建边缘节点的平均故障恢复时间（MTTR）通常为 4-8 小时（含硬件更换与配置同步），而公有云 CDN 的 MTTR 通常 < 15 分钟（自动故障转移），导致自建方案在 SLA 赔付风险上需预留额外 10-20% 的运维冗余预算

## Corrected Claim

自建边缘节点的MTTR通常显著高于公有云CDN（因涉及硬件更换与人工配置），而公有云CDN通过自动故障转移可实现分钟级恢复，因此自建方案在SLA保障上需预留更高的运维冗余预算。

## Evidence

[质询]该陈述包含具体的经验性数值（自建MTTR 4-8小时、公有云MTTR <15分钟、预算冗余10-20%），这些属于特定行业场景下的经验数据，无法从第一性原理推导，且参考来源仅定义了MTTR概念，未提供具体数值支持，存在来源缺失风险。 | 逻辑自洽（自建依赖人工/硬件更换耗时较长，公有云依赖自动化故障转移耗时较短，符合工程直觉），但参考来源[1]仅解释MTTR定义，未提供具体数值支持，属于经验事实且缺乏直接来源佐证。

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/noteview/81cbf174f41dc281e53a580216fc700abb685266.html&rut=56a66a34b9e805b945b199c5deb8f3da555311da4a060e681ec0e5e0edb9d845', 'type': 'ddg', 'title': '平均修复时间 (Mttr)计算方法全解'}
