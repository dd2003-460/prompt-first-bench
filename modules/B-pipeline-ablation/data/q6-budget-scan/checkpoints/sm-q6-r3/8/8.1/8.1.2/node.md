# N194: 服务器功耗的动态调整：CDN节点在低负载时段（如凌晨）可启用节能模式（CPU降频、硬盘休眠），平均功耗可能降至300W；若按平均350W计算，月耗电量 = 35

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

服务器功耗的动态调整：CDN节点在低负载时段（如凌晨）可启用节能模式（CPU降频、硬盘休眠），平均功耗可能降至300W；若按平均350W计算，月耗电量 = 350W * 720h / 1000 = 252kWh，比500W假设低30%；需根据实际负载曲线（峰值/均值比）修正功耗模型。

## Corrected Claim

服务器功耗的动态调整：CDN节点在低负载时段（如凌晨）可启用节能模式（CPU降频、硬盘休眠），平均功耗可能降至300W；若按平均350W计算，月耗电量 = 350W * 720h / 1000 = 252kWh，比500W假设低30%；需根据实际负载曲线（峰值/均值比）修正功耗模型。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 350W * 720h / 1000 = 252kWh 正确；(500-350)/500 = 30% 正确；CDN节点在低负载时通过CPU降频和硬盘休眠降低功耗至300-350W符合工程常识。

## Search Query

server energy saving mode CDN node average power consumption load profile
