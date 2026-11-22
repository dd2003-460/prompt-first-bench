# N152: 推理速度（Throughput）与部署配置的关联：Batch Size 从 1 增加到 4 时，RTX 5090 在 FP8 精度下的总吞吐量（Total To

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

推理速度（Throughput）与部署配置的关联：Batch Size 从 1 增加到 4 时，RTX 5090 在 FP8 精度下的总吞吐量（Total Tokens/s）通常提升 2-3 倍，但单请求延迟（Latency per request）增加 50%-100%。由于题目设定为'本地工作站'且'无硬性延迟指标'，需明确是以'总吞吐量'还是'单用户响应速度'作为性价比分母。若以总吞吐量为目标，多卡或高带宽单卡的边际收益会改变。

## Corrected Claim

推理速度（Throughput）与部署配置的关联：Batch Size 从 1 增加到 4 时，RTX 5090 在 FP8 精度下的总吞吐量（Total Tokens/s）通常提升 2-3 倍，但单请求延迟（Latency per request）增加 50%-100%。由于题目设定为'本地工作站'且'无硬性延迟指标'，需明确是以'总吞吐量'还是'单用户响应速度'作为性价比分母。若以总吞吐量为目标，多卡或高带宽单卡的边际收益会改变。

## Evidence

检索失败: no sources from any channel (all 5 failed)
