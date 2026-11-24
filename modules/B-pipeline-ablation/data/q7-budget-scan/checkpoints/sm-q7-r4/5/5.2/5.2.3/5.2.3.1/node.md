# N285: NVMe SSD 物理更换与固件刷写的基础人工工时 T_base = N_drives * t_swap + N_drives * t_firmware；假设 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

NVMe SSD 物理更换与固件刷写的基础人工工时 T_base = N_drives * t_swap + N_drives * t_firmware；假设 N_drives=50 (100TB扩容需~50块2TB NVMe)，t_swap=15min/drive, t_firmware=10min/drive，则 T_base = 50*(15+10)/60 = 20.8h，远超 N95 假设的 16h。

## Corrected Claim

NVMe SSD 物理更换与固件刷写的基础人工工时 T_base = N_drives * t_swap + N_drives * t_firmware；假设 N_drives=50 (100TB扩容需~50块2TB NVMe)，t_swap=15min/drive, t_firmware=10min/drive，则 T_base = 50*(15+10)/60 = 20.8h，远超 N95 假设的 16h。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（50*25/60≈20.83），参数假设（单盘更换+固件刷写耗时）符合工程常识，且明确标注为假设推导。

## Search Query

NVMe SSD replacement labor time firmware update standard
