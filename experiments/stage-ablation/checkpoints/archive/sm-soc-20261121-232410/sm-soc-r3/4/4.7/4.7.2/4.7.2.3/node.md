# N194: 10%价值阈值的具体数值化：0.1 * V 的绝对金额估算，若 V=100元，则阈值为10元；该阈值与 C_wait * T_wait 的临界点 T_crit 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

10%价值阈值的具体数值化：0.1 * V 的绝对金额估算，若 V=100元，则阈值为10元；该阈值与 C_wait * T_wait 的临界点 T_crit = (0.1 * V) / C_wait 对应，当 T_wait > T_crit 时，即使有降价预期，买家也因成本过高而放弃等待，直接咨询或离开。

## Corrected Claim

10%价值阈值的具体数值化：0.1 * V 的绝对金额估算，若 V=100元，则阈值为10元；该阈值与 C_wait * T_wait 的临界点 T_crit = (0.1 * V) / C_wait 对应，当 T_wait > T_crit 时，即使有降价预期，买家也因成本过高而放弃等待，直接咨询或离开。

## Evidence

先验知识/题面给定，逻辑校验通过：阈值定义与临界时间公式在代数上自洽，量纲合理（金额/成本=时间），符合经济学中等待成本与收益权衡的基本逻辑。

## Search Query

critical time threshold waiting cost 10 percent value
