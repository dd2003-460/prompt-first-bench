# N61: 源站后端处理时间P99：T_origin_processing_P99 = T_DB_lookup + T_transcode_check + T_auth，其

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

源站后端处理时间P99：T_origin_processing_P99 = T_DB_lookup + T_transcode_check + T_auth，其中T_DB_lookup为元数据库查询（典型1-5ms），T_transcode_check为转码状态检查（典型0-10ms，若需实时转码则显著增加），T_auth为鉴权（典型1-3ms），合计典型5-18ms。

## Corrected Claim

源站后端处理时间P99：T_origin_processing_P99 = T_DB_lookup + T_transcode_check + T_auth，其中T_DB_lookup为元数据库查询（典型1-5ms），T_transcode_check为转码状态检查（典型0-10ms，若需实时转码则显著增加），T_auth为鉴权（典型1-3ms），合计典型5-18ms。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个独立分量（T_DB_lookup, T_transcode_check, T_auth），逻辑上互斥且无重叠；三个子节点完整覆盖了父节点定义的所有组成部分；各子节点描述的是不同组件的延迟构成，并非同一参数的不同取值，因此无冗余。）
