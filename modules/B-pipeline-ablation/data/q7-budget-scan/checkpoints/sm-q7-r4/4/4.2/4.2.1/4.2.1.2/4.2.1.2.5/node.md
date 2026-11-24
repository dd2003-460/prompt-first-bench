# N682: 小文件 IOPS 瓶颈成本：当对象大小 < 1MB 且数量 > 10^8 时，LIST 操作或批量删除的 API 调用次数 N_api = N_obj / Ba

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N235, N236, N237

## Claim

小文件 IOPS 瓶颈成本：当对象大小 < 1MB 且数量 > 10^8 时，LIST 操作或批量删除的 API 调用次数 N_api = N_obj / Batch_Size (Batch=1000) = 5×10^5 次/操作；单次 LIST 延迟 T_list ≈ 100ms，总操作耗时 T_total = N_api * T_list ≈ 50,000s ≈ 14h；若人工介入成本 ¥100/h，则单次维护成本 C_maint = 14 * 100 = ¥1,400，年化 (假设每月1次) = ¥16,800，占存储费用比例需计算。

## Corrected Claim

当对象大小 < 1MB 且数量 > 10^8 时，LIST 操作或批量删除的 API 调用次数 N_api = N_obj / Batch_Size (Batch=1000) = 10^5 次/操作；单次 LIST 延迟 T_list ≈ 100ms，总操作耗时 T_total = N_api * T_list ≈ 10,000s ≈ 2.8h；若人工介入成本 ¥100/h，则单次维护成本 C_maint ≈ ¥280，年化 (假设每月1次) = ¥3,360。

## Evidence

先验知识/题面给定，逻辑校验通过：算术推导正确（10^8/1000=10^5次，10^5*0.1s=10^4s≈2.78h，此处原陈述中5×10^5次及14h的计算存在内部矛盾，需仔细核对。等等，重新计算：N_obj=10^8, Batch=1000 -> N_api=10^5。T_list=100ms=0.1s。T_total=10^5 * 0.1 = 10^4 s ≈ 2.78小时。原陈述称 N_api=5×10^5，这暗示 N_obj=5×10^8 或者 Batch=200？或者原陈述假设了某种重试/分页开销？再看原陈述：'N_api = N_obj / Batch_Size ... = 5×10^5'。如果 N_obj=10^8，Batch=1000，结果应为 10^5。原陈述数值 5×10^5 与前提 10^8/1000 不符。这是一个硬逻辑/算术错误。

## Search Query

S3 list operations performance small files cost IOPS
