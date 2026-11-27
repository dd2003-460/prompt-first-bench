# N94: N31中C_search占比40%的分解：C_search = C_browse + C_compare，其中C_browse为浏览N_items个商品的时间成

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29, N30, N31

## Claim

N31中C_search占比40%的分解：C_search = C_browse + C_compare，其中C_browse为浏览N_items个商品的时间成本（C_browse = N_items * t_browse * w_time，t_browse≈30秒/件，w_time为时间机会成本$0.05/分钟），C_compare为属性比对成本（C_compare = N_attributes * t_compare * w_time，t_compare≈10秒/属性），需通过用户行为日志统计平均N_items和N_attributes以校准。

## Corrected Claim

N31中C_search占比40%的分解：C_search = C_browse + C_compare，其中C_browse为浏览N_items个商品的时间成本（C_browse = N_items * t_browse * w_time），C_compare为属性比对成本（C_compare = N_attributes * t_compare * w_time），具体参数t_browse、w_time、t_compare需通过用户行为日志统计平均N_items和N_attributes以校准。

## Evidence

[质询]该陈述包含具体的经验参数（t_browse≈30秒/件, w_time=$0.05/分钟, t_compare≈10秒/属性），这些属于经验事实而非第一性原理可推导的数学或物理定律。在缺乏外部来源支持的情况下，这些具体数值缺乏实证依据，可能存在量级偏差或口径混淆（例如不同品类商品的浏览时间差异巨大，30秒/件可能不适用于所有场景）。 | 经验事实，逻辑自洽但缺来源支持。公式结构符合成本分解的基本逻辑，但具体参数值（30秒、$0.05/分钟、10秒）属于经验数据，无检索来源支持，无法验证其准确性，故降级为定性表述。

## Search Query

consumer search cost breakdown browsing comparison time cost second-hand platform user behavior log
