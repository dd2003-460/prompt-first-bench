# N24: OPEX 电力成本计算公式：OPEX_power = P_tco_total × T_hours × E_unit_price，其中 P_tco_total =

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

OPEX 电力成本计算公式：OPEX_power = P_tco_total × T_hours × E_unit_price，其中 P_tco_total = P_gpu × N_gpus + P_auxiliary（辅助功耗，含 CPU、内存、风扇等，通常占 GPU 功耗的 10%-20%），T_hours 为年运行小时数（如 8760h），E_unit_price 为当地电价（美元/kWh）；需区分消费级（无冗余电源）与数据中心级（80 Plus Titanium 效率）的 P_auxiliary 差异。

## Corrected Claim

OPEX 电力成本计算公式：OPEX_power = P_tco_total × T_hours × E_unit_price，其中 P_tco_total = P_gpu × N_gpus + P_auxiliary（辅助功耗，含 CPU、内存、风扇等，通常占 GPU 功耗的 10%-20%），T_hours 为年运行小时数（如 8760h），E_unit_price 为当地电价（美元/kWh）；需区分消费级（无冗余电源）与数据中心级（80 Plus Titanium 效率）的 P_auxiliary 差异。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（功率×时间×单价=成本），辅助功耗占比10%-20%符合数据中心工程常识，80 Plus Titanium效率描述准确。
