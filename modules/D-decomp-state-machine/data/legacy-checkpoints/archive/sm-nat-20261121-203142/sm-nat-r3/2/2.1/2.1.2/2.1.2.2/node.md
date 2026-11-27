# N100: 缓存驻留时间 T_residence 的高成本工作点：若最小对象大小 x_min = 10KB（典型网页资源），E[S] = 110KB；T_residence

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

缓存驻留时间 T_residence 的高成本工作点：若最小对象大小 x_min = 10KB（典型网页资源），E[S] = 110KB；T_residence ≈ (128*1024^3) / (578 * 110*1024) ≈ 2,000 秒 ≈ 33 分钟；此时头部对象驻留时间大幅缩短，LRU 命中率下界 H_LRU 将显著下降，需重新评估 C/M 覆盖率。

## Corrected Claim

缓存驻留时间 T_residence 的高成本工作点：若最小对象大小 x_min = 10KB（典型网页资源），E[S] = 110KB；T_residence ≈ (128*1024^3) / (578 * 110*1024) ≈ 2,000 秒 ≈ 33 分钟；此时头部对象驻留时间大幅缩短，LRU 命中率下界 H_LRU 将显著下降，需重新评估 C/M 覆盖率。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 (128*1024^3)/(578*110*1024) ≈ 2000 秒准确，量级合理，符合缓存驻留时间的基本物理/经济直觉。

## Search Query

impact of larger average object size on cache residence time and hit rate
