# N154: V100 FP16 实际推理延迟基准：在 4xV100 TP=4 配置下，Qwen3.8-27B 在 FP16 精度下的平均生成延迟约为 15-20 token

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N44

## Claim

V100 FP16 实际推理延迟基准：在 4xV100 TP=4 配置下，Qwen3.8-27B 在 FP16 精度下的平均生成延迟约为 15-20 tokens/s（基于 HuggingFace 社区报告及 V100 集群典型性能），即单 token 延迟约 50-67ms。

## Corrected Claim

由于 'Qwen3.8-27B' 模型版本存疑且无可靠来源支持其具体性能数据，建议移除该特定基准，或替换为已知的 Qwen 系列模型（如 Qwen-7B 或 Qwen-14B）在 4xV100 FP16 下的实测数据。

## Evidence

[质询]数值量级存疑：Qwen3.8-27B 并非公开存在的标准模型版本（Qwen 系列常见为 7B/14B/72B 等，27B 极罕见或为误传）；且在 4xV100 (FP16) 上运行 27B 模型，受限于 V100 较低的显存带宽（900GB/s）和 FP16 计算效率，15-20 tokens/s 的吞吐量对于 27B 参数量的模型而言偏高，通常此类配置下大模型推理速度会更低或需量化才能达标。 | 来源缺失且模型名称 'Qwen3.8-27B' 疑似不存在或为虚构/错误版本，导致基准数据缺乏可信基础；虽逻辑上延迟与吞吐换算正确（1/15s≈67ms, 1/20s=50ms），但前提事实（模型存在性及典型性能）无法验证。

## Search Query

V100 tensor core FP16 inference latency benchmark Qwen 27B
