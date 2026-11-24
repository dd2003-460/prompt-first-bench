# N334: 故障频率 p_fail 的时间尺度修正：p_fail=0.0154/月 是月度概率，但 Cost_latency_extra 公式中 T_fault=4/24 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

故障频率 p_fail 的时间尺度修正：p_fail=0.0154/月 是月度概率，但 Cost_latency_extra 公式中 T_fault=4/24 是日比例；需统一时间尺度：月故障次数 = p_fail × 30 ≈ 0.462次/月；每次故障持续4小时，月度总故障时长 = 0.462 × 4h ≈ 1.85h/月；修正后 Cost_latency_extra = ΔL × R_daily × (1.85/720) × Lambda。

## Corrected Claim

故障频率 p_fail 的时间尺度修正：p_fail=0.0154/月 是月度概率，但 Cost_latency_extra 公式中 T_fault=4/24 是日比例；需统一时间尺度：月故障次数 = p_fail × 30 ≈ 0.462次/月；每次故障持续4小时，月度总故障时长 = 0.462 × 4h ≈ 1.85h/月；修正后 Cost_latency_extra = ΔL × R_daily × (1.85/720) × Lambda。

## Evidence

先验知识/题面给定，逻辑校验通过：月度概率转换为月度期望次数（0.0154*30≈0.462）及总时长（0.462*4≈1.85h）的数学推导正确，时间尺度统一逻辑自洽。
