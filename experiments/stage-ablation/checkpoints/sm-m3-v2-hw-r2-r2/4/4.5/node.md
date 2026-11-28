# N25: 工作点A（纯本地极限）：仅使用4x V100-16GB推理Qwen3-27B，边际成本趋近于0（电费忽略不计），但受限于TP=4和MTP加速比，单任务吞吐上限约

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

工作点A（纯本地极限）：仅使用4x V100-16GB推理Qwen3-27B，边际成本趋近于0（电费忽略不计），但受限于TP=4和MTP加速比，单任务吞吐上限约为 $R_{local} \approx 50$ tokens/s（假设平均生成长度200 tokens），适合高频短程迭代，但无法处理长上下文复杂推理，质量上限受限于本地模型能力天花板。

## Corrected Claim

工作点A（纯本地极限）：仅使用4x V100-16GB推理Qwen3-27B，边际成本趋近于0（电费忽略不计），但受限于TP=4和MTP加速比，单任务吞吐上限约为 $R_{local} \approx 50$ tokens/s（假设平均生成长度200 tokens），适合高频短程迭代，但无法处理长上下文复杂推理，质量上限受限于本地模型能力天花板。

## Evidence

先验知识/题面给定，逻辑校验通过：4x V100-16GB显存充足（27B模型FP16约54GB，4卡共64GB），TP=4配置合理；50 tokens/s在4卡并行下符合大模型推理量级预期，逻辑自洽。
