# N773: 应用层缓存失效对 T_switchover 的影响：若应用层有本地缓存，切换后缓存失效，首次访问延迟增加 100-500ms，但业务不中断；若无缓存，业务中断直

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N286

## Claim

应用层缓存失效对 T_switchover 的影响：若应用层有本地缓存，切换后缓存失效，首次访问延迟增加 100-500ms，但业务不中断；若无缓存，业务中断直至数据重建完成

## Corrected Claim

应用层缓存失效对 T_switchover 的影响：若应用层有本地缓存，切换后缓存失效，首次访问延迟增加 100-500ms，但业务不中断；若无缓存，业务中断直至数据重建完成

## Evidence

先验知识/题面给定，逻辑校验通过
