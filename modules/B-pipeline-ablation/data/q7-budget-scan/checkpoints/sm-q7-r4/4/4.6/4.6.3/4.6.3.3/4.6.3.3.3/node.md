# N512: 若云存储发生大规模数据丢失需手动批量重新上传（极端故障场景），人力成本转为上传任务管理成本：T_upload_mgmt = (Total_Data_TB / U

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N222

## Claim

若云存储发生大规模数据丢失需手动批量重新上传（极端故障场景），人力成本转为上传任务管理成本：T_upload_mgmt = (Total_Data_TB / Upload_Bandwidth_Gbps) * (1/3600) * K_overhead；假设 500TB 数据，上传带宽 10Gbps，K_overhead=1.5（含元数据重建），耗时约 6.25 小时，人力成本 = 6.25 * 500 * 2 * 1.5 = ¥9,375/次，此为最坏情况上限

## Corrected Claim

若云存储发生大规模数据丢失需手动批量重新上传（极端故障场景），人力成本转为上传任务管理成本：T_upload_mgmt = (Total_Data_TB / Upload_Bandwidth_Gbps) * (1/3600) * K_overhead；假设 500TB 数据，上传带宽 10Gbps，K_overhead=1.5（含元数据重建），耗时约 111.1 小时，人力成本 = 111.1 * 500 * 2 * 1.5 = ¥166,650/次，此为最坏情况上限

## Evidence

先验知识/题面给定，逻辑校验通过：500TB=4000Gbit，4000/10=400h，400*1.5=600h? 不对，重新计算：500TB = 500 * 8000 Gbit = 4,000,000 Gbit。4,000,000 / 10 Gbps = 400,000 秒。400,000 / 3600 ≈ 111.1 小时。等等，题目中说是 6.25 小时。让我们仔细检查单位换算。通常 1 TB = 8 Tbit = 8,000,000 Mbit = 8,000,000,000 kbit... 或者更简单的：1 TB = 8 Tb (Terabits)。500 TB = 4000 Tb。带宽 10 Gbps = 0.01 Tbps。时间 = 4000 / 0.01 = 400,000 秒。400,000 / 3600 ≈ 111.11 小时。这与 6.25 小时相差巨大。难道带宽是 10 Gbps 还是 100 Gbps？如果是 100 Gbps，时间是 11.1 小时。如果是 1 Tbps，时间是 1.11 小时。6.25 小时对应的时间是 22500 秒。4000 Tb / 22500 s ≈ 0.177 Tbps = 177 Gbps。这与 10 Gbps 不符。或者数据量不是 500TB？如果时间是 6.25 小时 = 22500 秒，带宽 10 Gbps = 0.01 Tbps，数据量 = 22500 * 0.01 = 225 Tb = 28.125 TB。这与 500TB 不符。因此，数值计算存在严重错误。500TB 数据以 10Gbps 上传需要约 111 小时，而非 6.25 小时。这是一个硬性的数学/逻辑错误。

## Search Query

s3 data restoration upload cost calculation
