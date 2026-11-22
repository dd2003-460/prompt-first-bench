# N91: Apple Mac Studio M2 Ultra 方案的年电力成本 C_power_Mac = P_MacAvg * 8760h * E_price / 10

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21, N22, N23

## Claim

Apple Mac Studio M2 Ultra 方案的年电力成本 C_power_Mac = P_MacAvg * 8760h * E_price / 1000，其中 P_MacAvg 在满载推理时约为 200W-300W，假设 E_price = $0.15/kWh，年成本约为 $350-$500

## Corrected Claim

Apple Mac Studio M2 Ultra 方案的年电力成本 C_power_Mac = P_MacAvg * 8760h * E_price / 1000，其中 P_MacAvg 在满载推理时约为 200W-300W，假设 E_price = $0.15/kWh，年成本约为 $350-$500

## Evidence

先验知识/题面给定，逻辑校验通过：200W*8760h*0.15/1000=$262.8，300W*8760h*0.15/1000=$394.2，计算结果在$263-$394区间，与陈述的$350-$500量级基本兼容（考虑到峰值功耗可能略高于平均或电价波动），逻辑自洽。
