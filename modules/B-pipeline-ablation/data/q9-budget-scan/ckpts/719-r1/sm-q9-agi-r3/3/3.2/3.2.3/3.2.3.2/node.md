# N189: 工作点2（平衡型）：设定 max-num-seqs=8，Seq_Len_max = 65536 tokens，总 KV 显存占用约 32GB，逼近 OOM 阈值

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

工作点2（平衡型）：设定 max-num-seqs=8，Seq_Len_max = 65536 tokens，总 KV 显存占用约 32GB，逼近 OOM 阈值，需启用 PagedAttention 碎片压缩（碎片率<5%），单请求 P99 延迟 < 5s，吞吐量最大。

## Corrected Claim

工作点2（平衡型）：设定 max-num-seqs=8，Seq_Len_max = 65536 tokens，在典型大模型推理场景下，总 KV 显存占用可达数十GB量级（如32GB），逼近 OOM 阈值，需启用 PagedAttention 碎片压缩（碎片率<5%），单请求 P99 延迟 < 5s，吞吐量较大。

## Evidence

[质询]数值量级与硬件配置强耦合，缺乏具体GPU型号（如A100/H100）及模型架构（如Llama-7B/70B）作为前提，导致“32GB”这一绝对数值无法从第一性原理推导，属于特定场景下的经验参数，存在口径混淆风险。 | source=knowledge，逻辑自洽（PagedAttention降低碎片、平衡型工作点特征描述符合常识），但具体显存占用数值为经验事实，无外部来源支持，依据经验事实排除条款降级。
