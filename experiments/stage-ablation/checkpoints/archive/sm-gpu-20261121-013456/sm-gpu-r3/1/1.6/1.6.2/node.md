# N66: Qwen3-27B 在 BF16 精度、Batch_Size=4、Seq_Len=32K 条件下，基于 GQA 架构 (Num_KV_Heads=8) 的 KV

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

Qwen3-27B 在 BF16 精度、Batch_Size=4、Seq_Len=32K 条件下，基于 GQA 架构 (Num_KV_Heads=8) 的 KV Cache 显存占用精确计算值为 2 * 64 * 8 * 128 * 32768 * 2 bytes * 4 / (1024^3) ≈ 17.2 GB，需分析多用户并发下的显存瓶颈及 OOM 风险。

## Corrected Claim

Qwen3-27B 在 BF16 精度、Batch_Size=4、Seq_Len=32K 条件下，基于 GQA 架构 (Num_KV_Heads=8) 的 KV Cache 显存占用计算值约为 17.2 GB，需分析多用户并发下的显存瓶颈及 OOM 风险。

## Evidence

[质询]参考来源[1]讨论的是 Qwen3.8-27B 在 L20 显卡上的部署，与节点中声称的 Qwen3-27B 及特定参数（Num_KV_Heads=8, Seq_Len=32K）下的精确显存计算无直接关联，且来源未提供该具体计算值的支持。 | 逻辑校验通过：公式 2 * 64 * 8 * 128 * 32768 * 2 * 4 / (1024^3) 计算结果约为 17.18 GB，与 17.2 GB 一致，量纲和数值合理。但参考来源[1]主题不匹配（Qwen3.8 vs Qwen3，且未涉及此特定KV Cache计算），属于经验事实且缺乏直接来源支持，故降级。

## Search Query

Qwen3-27B batch size 4 KV cache memory

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072597504793880030&rut=939cafd07a4e15ae1245f5a339b74e22b7f3b2377110377f185cd50347b447f0', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 BF16、FP8、MTP、单卡表现，以及与 Qwen3.6 MoE 的差距'}
