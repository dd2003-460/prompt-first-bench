# N67: 单服务器月成本 C_server 的构成拆解：C_server = C_hardware_depreciation + C_power + C_colocati

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

单服务器月成本 C_server 的构成拆解：C_server = C_hardware_depreciation + C_power + C_colocation_rent，其中 C_hardware_depreciation 为硬件折旧（假设3-5年直线折旧，初始成本¥15k-30k），C_power 为电力成本（PUE系数1.3-1.5，电价¥0.6-1.0/kWh，单服务器功耗300-500W），C_colocation_rent 为机柜租金（¥500-2000/月/台，视一线城市/二线城市差异）。

## Corrected Claim

单服务器月成本 C_server 的构成拆解：C_server = C_hardware_depreciation + C_power + C_colocation_rent，其中 C_hardware_depreciation 为硬件折旧（假设3-5年直线折旧，初始成本¥15k-30k），C_power 为电力成本（PUE系数1.3-1.5，电价¥0.6-1.0/kWh，单服务器功耗300-500W），C_colocation_rent 为机柜租金（¥500-2000/月/台，视一线城市/二线城市差异）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点代表了两种不同的硬件配置档位（高配/中配），彼此互斥且无重叠。它们共同覆盖了父节点公式中所有变量（折旧、电力、租金）在不同场景下的具体取值，符合参数实例化的逻辑，不属于冗余。）
