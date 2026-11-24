# N165: 工作点B (20x32TB NVMe) 的年电力成本计算：20块32TB NVMe SSD静态功耗约0.5W/TB，动态功耗增量约0.3W/TB；总功耗 = 6

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

工作点B (20x32TB NVMe) 的年电力成本计算：20块32TB NVMe SSD静态功耗约0.5W/TB，动态功耗增量约0.3W/TB；总功耗 = 640TB * 0.8W/TB (加权平均) = 512W = 0.512kW；年电力成本 = 0.512kW * 1.4 (PUE) * 0.8¥/kWh * 8760h ≈ ¥5,022/年；折合每TB年电力成本 = 5022 / 577.6 ≈ ¥8.7/TB·年。

## Corrected Claim

工作点B (20x32TB NVMe) 的年电力成本计算：20块32TB NVMe SSD静态功耗约0.5W/TB，动态功耗增量约0.3W/TB；总功耗 = 640TB * 0.8W/TB (加权平均) = 512W = 0.512kW；年电力成本 = 0.512kW * 1.4 (PUE) * 0.8¥/kWh * 8760h ≈ ¥5,022/年；折合每TB年电力成本 = 5022 / 577.6 ≈ ¥8.7/TB·年。

## Evidence

先验知识/题面给定，逻辑校验通过：功耗计算（640TB * 0.8W/TB = 512W）及成本公式（0.512kW * 1.4 PUE * 0.8¥/kWh * 8760h ≈ 5022¥）算术正确，单位量级合理。
