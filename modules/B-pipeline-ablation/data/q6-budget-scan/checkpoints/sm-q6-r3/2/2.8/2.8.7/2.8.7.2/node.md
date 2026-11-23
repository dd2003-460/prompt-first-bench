# N307: 短视频对象日均新增数 N_vid_daily = V_upload_vid_daily / s_vid_avg，其中 V_upload_vid_daily 假设

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

短视频对象日均新增数 N_vid_daily = V_upload_vid_daily / s_vid_avg，其中 V_upload_vid_daily 假设占 30% 即 60GB，s_vid_avg 取 5MB（短视频平均大小），故 N_vid_daily ≈ 12,000 个

## Corrected Claim

短视频对象日均新增数 N_vid_daily = V_upload_vid_daily / s_vid_avg，其中 V_upload_vid_daily 假设占 30% 即 60GB，s_vid_avg 取 5MB（短视频平均大小），故 N_vid_daily ≈ 12,000 个

## Evidence

先验知识/题面给定，逻辑校验通过：60GB / 5MB = 60 * 1024 MB / 5 MB ≈ 12288，与12,000量级一致，计算逻辑自洽。
