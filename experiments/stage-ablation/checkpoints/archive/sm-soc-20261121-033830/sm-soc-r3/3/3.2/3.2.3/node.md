# N62: 消费者剩余提取量 ΔCS = (WTP_max - P_final) 在筛选成功后的期望值；若筛选机制将买家限定在 WTP > P_high 的子集，则平台/卖

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N15

## Claim

消费者剩余提取量 ΔCS = (WTP_max - P_final) 在筛选成功后的期望值；若筛选机制将买家限定在 WTP > P_high 的子集，则平台/卖家捕获的剩余比例 R_capture = (P_high - C) / (WTP_max - C)，需验证 R_capture 是否显著高于无筛选基准。

## Corrected Claim

消费者剩余提取量应明确为筛选后买家群体中 (WTP_i - P_final) 的期望值；R_capture 应基于筛选后买家 WTP 分布的期望值 E[WTP|WTP>P_high] 而非单一 WTP_max 进行计算，以反映真实捕获比例。

## Evidence

[质询]该陈述将消费者剩余提取量定义为 (WTP_max - P_final)，这在经济学上通常对应生产者剩余或总剩余的一部分，而非标准的消费者剩余（通常为 WTP - P）；此外，R_capture 公式假设 WTP_max 为单一确定值，忽略了筛选后买家 WTP 分布的异质性，导致捕获比例计算缺乏统计严谨性。 | 无可用外部证据；逻辑上公式结构自洽但定义存在术语混淆风险，且缺乏来源支持具体数值或基准对比，属于经验/模型设定事实，降级处理。

## Search Query

consumer surplus extraction second hand market high price listing buyer willingness to pay gap
