# N80: 核验Qwen3.8-27B实际架构：查阅HuggingFace config.json确认num_key_value_heads值，若为GQA(num_kv_h

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

核验Qwen3.8-27B实际架构：查阅HuggingFace config.json确认num_key_value_heads值，若为GQA(num_kv_heads=8)则每token KV开销=(2*48*8*128*2bytes)/4=491.5KB/卡，最大上下文=10.5GB/491.5KB≈21,750 tokens；若为MHA(num_kv_heads=32)则开销=1.97MB/卡，最大上下文≈5,430 tokens，两者均远超N37声称的3.5 tokens（N37计算错误源于未除以TP=4）。

## Corrected Claim

基于假设的架构参数（GQA kv_heads=8 或 MHA kv_heads=32），计算表明最大上下文长度远超3.5 tokens，证实N37的计算错误源于未考虑张量并行（TP=4）导致的显存分摊。具体数值需以实际模型config为准。

## Evidence

[质询]该陈述包含具体的模型架构参数（如 num_key_value_heads=8 或 32, head_dim=128, layers=48），这些属于经验事实。由于检索失败，无法验证 Qwen3.8-27B 的实际配置是否确实如此，存在参数假设错误的风险。 | 经验事实，逻辑自洽但缺来源支持。数学计算过程正确：GQA场景下 (2*48*8*128*2)/4 = 491.5 KB，10.5GB/491.5KB ≈ 21750 tokens；MHA场景下 (2*48*32*128*2)/4 = 1.966 MB，10.5GB/1.966MB ≈ 5340 tokens（原文5430略有偏差但量级正确）。核心结论“N37未除以TP导致错误”在逻辑上成立，但因缺乏外部来源确认具体架构参数，降级处理。

## Search Query

Qwen3 27B config.json num_key_value_heads architecture parameters
