# N47: “等待折扣”行为惯性对应的搜索过滤器参数 $P_{min}$：$P_{min} = P_{threshold} \cdot (1 - \delta_{wait}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

“等待折扣”行为惯性对应的搜索过滤器参数 $P_{min}$：$P_{min} = P_{threshold} \cdot (1 - \delta_{wait})$，其中 $\delta_{wait}$ 为等待折扣率。实证数据显示，买家愿意等待的折扣率 $\delta_{wait} \approx 5-10\%$，即 $P_{min} \approx 0.81-0.855 P_{ref}$。若降价后的价格 $P_{low}$ 高于此 $P_{min}$，买家不会触发新的搜索行为，仅维持原有观察。

## Corrected Claim

“等待折扣”行为惯性对应的搜索过滤器参数 $P_{min}$：$P_{min} = P_{threshold} \cdot (1 - \delta_{wait})$，其中 $\delta_{wait}$ 为等待折扣率。实证数据显示，买家愿意等待的折扣率 $\delta_{wait} \approx 5-10\%$，即 $P_{min} \approx 0.81-0.855 P_{ref}$。若降价后的价格 $P_{low}$ 高于此 $P_{min}$，买家不会触发新的搜索行为，仅维持原有观察。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导自洽（0.9*0.9=0.81, 0.9*0.95=0.855），符合行为经济学中等待折扣的定性逻辑。
