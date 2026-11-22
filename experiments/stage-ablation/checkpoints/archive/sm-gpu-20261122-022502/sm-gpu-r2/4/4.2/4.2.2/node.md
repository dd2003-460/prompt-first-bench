# N63: P_overhead 主机系统功耗分解：包含 CPU (50-150W)、主板/内存 (50-100W)、存储 (10-30W)、散热风扇 (20-50W) 及

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

P_overhead 主机系统功耗分解：包含 CPU (50-150W)、主板/内存 (50-100W)、存储 (10-30W)、散热风扇 (20-50W) 及电源转换损耗 (5-10%)，2×4090 主机总系统功耗约为 600-750W，1×A100 主机总系统功耗约为 450-550W，需根据具体 CPU 型号和散热方案确定

## Corrected Claim

P_overhead 主机系统功耗分解：包含 CPU (50-150W)、主板/内存 (50-100W)、存储 (10-30W)、散热风扇 (20-50W) 及电源转换损耗 (5-10%)，2×4090 主机总系统功耗约为 600-750W，1×A100 主机总系统功耗约为 450-550W，需根据具体 CPU 型号和散热方案确定

## Evidence

先验知识/题面给定，逻辑校验通过：各组件功耗量级符合工程常识，2x4090(约600W)与A100(约300W)主机总功耗估算合理，内部无矛盾。

## Search Query

high-end gaming PC vs workstation power consumption components breakdown
