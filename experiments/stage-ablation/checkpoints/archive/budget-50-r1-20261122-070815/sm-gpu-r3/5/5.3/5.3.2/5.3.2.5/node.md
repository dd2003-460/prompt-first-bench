# N358: Qwen3-27B 在 A100 80GB (Ampere) 上运行 BF16 精度时，Batch Size=1 的实测单 token 生成吞吐量（tokens

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N126

## Claim

Qwen3-27B 在 A100 80GB (Ampere) 上运行 BF16 精度时，Batch Size=1 的实测单 token 生成吞吐量（tokens/s）及 TTFT (ms)，用于建立数据中心卡的性能基线并与消费级卡对比。

## Corrected Claim

Qwen3-27B 在 A100 80GB (Ampere) 上运行 BF16 精度时，Batch Size=1 的单 token 生成吞吐量及 TTFT 需通过实际基准测试获取，当前缺乏具体实测数据。

## Evidence

[质询]该陈述声称拥有具体的“实测”数值（吞吐量及TTFT），但参考来源显示“本轮检索无可用来源”，且具体硬件性能指标属于经验事实，无法从第一性原理推导，缺乏数据支撑。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B vLLM benchmark A100 batch size 1 throughput tokens/s
