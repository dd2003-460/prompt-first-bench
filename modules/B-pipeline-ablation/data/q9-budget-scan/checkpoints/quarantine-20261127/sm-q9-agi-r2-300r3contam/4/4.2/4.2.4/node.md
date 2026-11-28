# N58: 多智能体投票的端到端延迟T_total = T_inference_max + T_aggregation，其中T_inference_max = T_sing

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

多智能体投票的端到端延迟T_total = T_inference_max + T_aggregation，其中T_inference_max = T_single * L_eff(N)（取最慢智能体时间），T_aggregation ≈ 0.5s（固定聚合开销）。对于N=3，若T_single=5s，T_total ≈ 5*1.2*3 + 0.5 = 18.5s；对于N=5，T_total ≈ 5*1.3*5 + 0.5 = 33s。

## Corrected Claim

多智能体投票的端到端延迟 T_total = T_inference_max + T_aggregation。若智能体并行运行，T_inference_max 取决于最慢智能体的耗时，通常近似为 T_single * L_eff(1)（假设负载因子主要受单任务复杂度影响，而非智能体数量线性增加），而非 T_single * L_eff(N) * N。具体数值需根据实际系统负载模型确定。

## Evidence

[质询]公式逻辑存在严重缺陷：T_inference_max 定义为“取最慢智能体时间”，但在并行架构下，所有智能体同时开始推理，总延迟应取决于最慢的那个智能体的耗时（即 max(T_i)），而不是所有智能体耗时的总和（sum(T_i)）。陈述中计算 N=3 时使用了 5*1.2*3，暗示将三个智能体的时间相加，这与“max”的定义及并行投票的常识相悖。此外，L_eff(N) 的具体数值（1.2, 1.3）缺乏来源支持，属于经验参数。 | 逻辑校验发现内部矛盾：'max'操作不应导致时间随N线性累加（除非是串行执行，但'投票'通常隐含并行或独立评估后汇总，且题目明确说'取最慢'）。若为并行，T_inference_max 应约为 T_single * L_eff(1) 或类似常数，而非乘以 N。由于 source 为 knowledge，虽不需外部来源，但逻辑不自洽且包含未定义的经验系数，故降级。
