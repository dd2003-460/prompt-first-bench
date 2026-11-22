# N340: 在 2x7900 XTX 多卡工作点下，总 Capex 为 2*$899 (GPU) + $1800 (平台: 双PCIe x8主板+$300, AMD CPU

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

在 2x7900 XTX 多卡工作点下，总 Capex 为 2*$899 (GPU) + $1800 (平台: 双PCIe x8主板+$300, AMD CPU+$300, 64GB RAM+$200, 1600W电源+$300, 机箱+$200, 散热+$300, 其他+$200) = $3598；相比 2x4090 节省 $1600 Capex，但 ROCm 生态成熟度较低可能导致软件维护成本增加和性能损失，需纳入 TCO 的隐性成本考量。

## Corrected Claim

在 2x7900 XTX 多卡工作点下，总 Capex 为 2*$899 (GPU) + $1800 (平台: 双PCIe x8主板+$300, AMD CPU+$300, 64GB RAM+$200, 1600W电源+$300, 机箱+$200, 散热+$300, 其他+$200) = $3598；相比 2x4090 节省 $1600 Capex，但 ROCm 生态成熟度较低可能导致软件维护成本增加和性能损失，需纳入 TCO 的隐性成本考量。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（2*899+1800=3598），硬件配置（双卡PCIe x8、64GB RAM、1600W电源）符合2x7900 XTX的工程常识，ROCm生态劣势为公认事实。
