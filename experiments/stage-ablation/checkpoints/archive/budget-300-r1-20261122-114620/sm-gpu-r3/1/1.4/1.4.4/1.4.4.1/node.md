# N174: vLLM 在 2x RTX 4090 (PCIe Gen4) 上执行 TP=2 时，NCCL All-Reduce 通信延迟 T_comm 约为 0.5-1.0

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

vLLM 在 2x RTX 4090 (PCIe Gen4) 上执行 TP=2 时，NCCL All-Reduce 通信延迟 T_comm 约为 0.5-1.0ms/layer，对于 Qwen3-27B 的 64 层架构，单次前向传播总通信延迟约为 32-64ms，占单 token 生成时间（~35ms @ 28tok/s）的 90-180%，导致 TP=2 在 PCIe 互联下吞吐反而低于单卡

## Corrected Claim

vLLM 在 2x RTX 4090 (PCIe Gen4) 上执行 TP=2 时，由于 PCIe 带宽限制，NCCL All-Reduce 通信延迟显著增加，导致 Qwen3-27B 的吞吐率相比单卡推理有明显下降，但具体延迟占比和绝对值需实测验证，通常不会达到通信延迟占总时间 90-180% 的极端情况。

## Evidence

[质询]数值量级与逻辑自洽性存在矛盾：若单卡生成时间为35ms，且TP=2下通信延迟占比高达90-180%（即31.5-63ms），则总延迟至少为66.5ms，对应吞吐应降至约15tok/s以下，而非维持35ms基准；此外，PCIe Gen4 x16带宽下，27B模型每层All-Reduce通信量较小，0.5-1.0ms/layer的延迟估计偏高，通常PCIe互联下TP=2的通信开销虽显著但未必导致吞吐‘反而低于单卡’到这种极端比例，且‘占单token生成时间’的表述混淆了通信延迟与总生成时间的关系。 | 先验知识/题面给定，逻辑校验未通过：通信延迟占比与总时间/吞吐数据存在内部矛盾，且PCIe Gen4下TP=2通信延迟量级估计偏高，缺乏来源支持且逻辑不自洽。

## Search Query

vLLM tensor parallelism latency PCIe Gen4 RTX 4090 NCCL overhead
