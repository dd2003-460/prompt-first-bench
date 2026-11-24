# N546: 基准情景下，NVMe SSD 阵列的 5 年有效可用容量年化成本 C_annual_base 由折旧、电力、运维三部分构成：C_annual_base = (C

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N235

## Claim

基准情景下，NVMe SSD 阵列的 5 年有效可用容量年化成本 C_annual_base 由折旧、电力、运维三部分构成：C_annual_base = (C_hw_base/5) + P_total_NVMe * 8760 * E_price * k_pue + C_ops_annual。代入修正后 C_hw_base=¥2,025,000，P_total_NVMe≈2,500W (含基础设施)，E_price=¥0.6/kWh，k_pue=1.5，C_ops_annual=¥50,000，计算得 C_annual_base ≈ ¥405,000 + ¥19,710,000/1000*0.6*1.5 + ¥50,000 ≈ ¥405,000 + ¥19,710 + ¥50,000 = ¥474,710/年（注：电力项单位需统一，此处按 kW 计算：2.5kW * 8760h * 0.6 * 1.5 = ¥19,710，此项相对于硬件折旧极小，主要成本在硬件折旧）。

## Corrected Claim

基准情景下，NVMe SSD 阵列的 5 年有效可用容量年化成本 C_annual_base 由折旧、电力、运维三部分构成：C_annual_base = (C_hw_base/5) + P_total_NVMe * 8760 * E_price * k_pue + C_ops_annual。代入修正后 C_hw_base=¥2,025,000，P_total_NVMe≈2,500W (含基础设施)，E_price=¥0.6/kWh，k_pue=1.5，C_ops_annual=¥50,000，计算得 C_annual_base ≈ ¥405,000 + ¥19,710,000/1000*0.6*1.5 + ¥50,000 ≈ ¥405,000 + ¥19,710 + ¥50,000 = ¥474,710/年（注：电力项单位需统一，此处按 kW 计算：2.5kW * 8760h * 0.6 * 1.5 = ¥19,710，此项相对于硬件折旧极小，主要成本在硬件折旧）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合TCO计算常识，数值代入计算准确（2.5kW * 8760h * 0.6元/kWh * 1.5 PUE = 19,710元；405,000 + 19,710 + 50,000 = 474,710元），量纲与量级合理。
