# N23: 黑盒清单汇总：(1) 地形-大气耦合系数 C_D(x,y,t) 无实时观测，只能靠静态 DEM+土地利用分类估算，误差 ±50%；(2) 眼墙对流崩塌临界 Re

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

黑盒清单汇总：(1) 地形-大气耦合系数 C_D(x,y,t) 无实时观测，只能靠静态 DEM+土地利用分类估算，误差 ±50%；(2) 眼墙对流崩塌临界 Reynolds 数无理论公式，依赖经验阈值 Vmax>50m/s；(3) 垂直风切变剖面在登陆后 12h 内的演变无可靠预报，GFS 模式 250hPa 风切变误差 ±5 m/s，直接影响流出阻塞程度评估

## Corrected Claim

黑盒清单汇总：(1) 地形-大气耦合系数 C_D(x,y,t) 无实时观测，只能靠静态 DEM+土地利用分类估算，误差 ±50%；(2) 眼墙对流崩塌临界 Reynolds 数无理论公式，依赖经验阈值 Vmax>50m/s；(3) 垂直风切变剖面在登陆后 12h 内的演变无可靠预报，GFS 模式 250hPa 风切变误差 ±5 m/s，直接影响流出阻塞程度评估

## Evidence

先验知识/题面给定，逻辑校验通过
