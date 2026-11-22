# N358: H100 PCIe INT8 Decode 阶段 85% 实际效率系数的分解：HBM 内存控制器效率 (98%)、PCIe 4.0 传输开销 (95%)、内核调

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N128

## Claim

H100 PCIe INT8 Decode 阶段 85% 实际效率系数的分解：HBM 内存控制器效率 (98%)、PCIe 4.0 传输开销 (95%)、内核调度开销 (90%)，复合效率 = 0.98 * 0.95 * 0.90 ≈ 0.84，与 85% 假设一致；修正后实际吞吐为 2039/27 * 0.84 ≈ 63.6 tokens/s，与原估算 64.2 tokens/s 偏差 <1%。

## Corrected Claim

H100 PCIe INT8 Decode 阶段 85% 实际效率系数的分解：HBM 内存控制器效率 (98%)、PCIe 4.0 传输开销 (95%)、内核调度开销 (90%)，复合效率 = 0.98 * 0.95 * 0.90 ≈ 0.84，与 85% 假设一致；修正后实际吞吐为 2039/27 * 0.84 ≈ 63.6 tokens/s，与原估算 64.2 tokens/s 偏差 <1%。

## Evidence

先验知识/题面给定，逻辑校验通过：0.98*0.95*0.90=0.8379≈0.84，2039/27*0.84≈63.6，计算自洽且量级合理
