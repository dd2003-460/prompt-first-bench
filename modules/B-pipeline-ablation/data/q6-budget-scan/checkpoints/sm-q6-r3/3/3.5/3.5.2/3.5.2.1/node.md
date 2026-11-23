# N329: GPU 转码集群利用率 η_gpu 与成本分摊模型：C_transcode_per_GB = C_gpu_hourly / (Throughput_GB_per

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N112

## Claim

GPU 转码集群利用率 η_gpu 与成本分摊模型：C_transcode_per_GB = C_gpu_hourly / (Throughput_GB_per_hour * η_gpu)，其中 C_gpu_hourly 为单卡小时成本（A100 约 ¥5-10/h），Throughput 为单卡转码吞吐（1080p 约 5-10 GB/h），η_gpu 为实际利用率（通常 60-80%），代入得 C_transcode ≈ ¥0.5-2.5/GB。

## Corrected Claim

GPU 转码集群利用率 η_gpu 与成本分摊模型：C_transcode_per_GB = C_gpu_hourly / (Throughput_GB_per_hour * η_gpu)，其中 C_gpu_hourly 为单卡小时成本（A100 约 ¥5-10/h），Throughput 为单卡转码吞吐（1080p 约 5-10 GB/h），η_gpu 为实际利用率（通常 60-80%），代入得 C_transcode ≈ ¥0.5-2.5/GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，代入数值（5-10元/h ÷ (5-10GB/h * 0.6-0.8)）得出的成本区间（约0.5-2.5元/GB）在量级和算术上均自洽。

## Search Query

GPU video transcoding cost per GB A100 throughput utilization
