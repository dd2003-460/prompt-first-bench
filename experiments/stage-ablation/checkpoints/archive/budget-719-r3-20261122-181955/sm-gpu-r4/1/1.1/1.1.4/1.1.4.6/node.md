# N147: RTX 3090 Ti 的 350W TDP 对应 P_avg 约为 245W，其能效比 (tokens/s per watt) 在 INT4 推理下约为 25

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N42, N43, N44

## Claim

RTX 3090 Ti 的 350W TDP 对应 P_avg 约为 245W，其能效比 (tokens/s per watt) 在 INT4 推理下约为 25-28 / 245 ≈ 0.10-0.11 tokens/s/W，高于 RTX 4090 的 11.5-15 / 315 ≈ 0.036-0.048 tokens/s/W (BF16)，但低于 4090 在 FP8 下的能效比。

## Corrected Claim

RTX 3090 Ti 的 TDP 通常为 450W，RTX 4090 的 TDP 为 450W。具体能效比需基于实际功耗和吞吐量数据重新计算，原陈述中的功率数值有误。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点存在逻辑矛盾与冗余。1. 正交性失败：子节点2声称N147的0.10-0.11偏低，而子节点4结论修正称3090 Ti显著高于4090，这与父节点中隐含的对比基准（父节点原文称3090 Ti为0.10-0.11）存在数值上的不一致，且子节点2与子节点4在解释能效比高低原因上存在逻辑重叠和潜在冲突（子节点2质疑父节点数据，子节点4直接基于新数据下结论）。2. 冗余：子节点1、2、3均重复描述了“理论吞吐量=带宽/内存”及“实测=理论*0.7”的计算逻辑，这应作为通用公式或参数提取，而非在每个子节点中重复叙述。）

## Search Query

RTX 3090 Ti vs RTX 4090 energy efficiency LLM inference tokens per second per watt
