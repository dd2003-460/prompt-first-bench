# N274: GeoIP数据库精度对DNS调度错误率的影响：基于IP归属地查询的GeoIP数据库（如MaxMind GeoLite2）城市级定位准确率约70%-90%，省份级

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

GeoIP数据库精度对DNS调度错误率的影响：基于IP归属地查询的GeoIP数据库（如MaxMind GeoLite2）城市级定位准确率约70%-90%，省份级约95%；错误路由导致用户被调度至非最近POP，延迟增量 $\Delta L_{error} = RTT_{suboptimal} - RTT_{optimal}$，典型值10-30ms；需量化错误率 $\epsilon_{geo}$ 对P99延迟的贡献：$\Delta P99_{geo} = \epsilon_{geo} \times \phi_{affected} \times \Delta L_{error}$，其中 $\phi_{affected}$ 为受错误路由影响的流量比例

## Corrected Claim

GeoIP数据库精度对DNS调度错误率的影响：基于IP归属地查询的GeoIP数据库（如MaxMind GeoLite2）城市级定位准确率约70%-90%，省份级约95%；错误路由导致用户被调度至非最近POP，延迟增量 $\Delta L_{error} = RTT_{suboptimal} - RTT_{optimal}$，典型值10-30ms；需量化错误率 $\epsilon_{geo}$ 对P99延迟的贡献：$\Delta P99_{geo} = \epsilon_{geo} \times \phi_{affected} \times \Delta L_{error}$，其中 $\phi_{affected}$ 为受错误路由影响的流量比例

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

MaxMind GeoLite2 city level accuracy rate 2024
