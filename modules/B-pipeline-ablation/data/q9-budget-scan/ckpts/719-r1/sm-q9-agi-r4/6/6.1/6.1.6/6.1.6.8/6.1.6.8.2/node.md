# N731: 注意力稀释 (Attention Dilution) 导致任务完成率下降的量化机制：长上下文中关键信息被淹没的概率 P_dilute 与信息位置熵相关。若关键指

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N268

## Claim

注意力稀释 (Attention Dilution) 导致任务完成率下降的量化机制：长上下文中关键信息被淹没的概率 P_dilute 与信息位置熵相关。若关键指令位于 prompt 开头，在 4k context 中，注意力权重分布更均匀，最大注意力权重 w_max 从 n=1k 时的 ~0.3 降至 n=4k 时的 ~0.15。若模型依赖 w_max > 0.2 来锁定关键指令，则失败概率 P_fail ≈ 1 - sigmoid((w_max - 0.2)/0.05)。w_max=0.15 时，P_fail ≈ 1 - sigmoid(-1) ≈ 73%。此模型需实测验证。

## Corrected Claim

注意力稀释可能导致长上下文中关键信息被淹没。理论上，随着上下文长度增加，注意力权重分布趋于均匀，最大注意力权重 w_max 可能下降。若模型依赖较高的 w_max 锁定关键指令，其失败概率可能随 w_max 降低而上升。具体数值（如 w_max 降至 0.15 或失败率 73%）需针对特定模型进行实测验证，不可作为通用定量结论。

## Evidence

[质询]该陈述包含具体的经验参数（如 w_max 从 0.3 降至 0.15，sigmoid 阈值 0.2 和温度 0.05），这些数值并非第一性原理可推导，而是特定模型架构和训练数据下的经验观测值。缺乏通用性，且不同模型（如 Llama vs GPT）的注意力分布差异巨大，直接断言具体数值具有误导性。 | 经验事实，逻辑自洽但缺来源支持。虽然数学计算（sigmoid(-1)≈0.2689, 1-0.2689≈0.7311）正确，但核心前提（w_max 的具体数值变化及 sigmoid 拟合参数）属于未经证实的经验假设，且无外部来源支持。

## Search Query

LLM attention dilution long context key instruction failure rate empirical study
