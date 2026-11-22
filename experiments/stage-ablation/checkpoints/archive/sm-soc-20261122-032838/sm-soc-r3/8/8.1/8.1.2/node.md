# N296: 高溢价对 DwellTime 的边际贡献：计算 $\Delta \text{DwellTime} / \Delta P_{ask}$。假设买家在高溢价商品上的犹

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

高溢价对 DwellTime 的边际贡献：计算 $\Delta \text{DwellTime} / \Delta P_{ask}$。假设买家在高溢价商品上的犹豫时间增加量 $\Delta t = k \cdot (P_{ask} - P_{ref})$。若 $k=10$ 秒/10%溢价，则 $\Delta \text{DwellTime} = 10 \cdot 0.2 = 2$ 秒。若平台每增加1秒停留时间带来的效用增益为 $U_{sec}=0.1$ 单位，而 GMV 每增加1%带来的效用增益为 $U_{gmv}=1.0$ 单位，则需计算 $2 \cdot 0.1$ 是否大于因高溢价导致的成交概率下降带来的 GMV 损失。若成交概率下降 5%，GMV 损失为 $5\% \cdot P_{ref} \cdot Q \cdot U_{gmv}$，需比较两者数值。

## Corrected Claim

高溢价对 DwellTime 的边际贡献：计算 $\Delta \text{DwellTime} / \Delta P_{ask}$。假设买家在高溢价商品上的犹豫时间增加量 $\Delta t = k \cdot (P_{ask} - P_{ref})$。若 $k=10$ 秒/10%溢价，则 $\Delta \text{DwellTime} = 10 \cdot 0.2 = 2$ 秒。若平台每增加1秒停留时间带来的效用增益为 $U_{sec}=0.1$ 单位，而 GMV 每增加1%带来的效用增益为 $U_{gmv}=1.0$ 单位，则需计算 $2 \cdot 0.1$ 是否大于因高溢价导致的成交概率下降带来的 GMV 损失。若成交概率下降 5%，GMV 损失为 $5\% \cdot P_{ref} \cdot Q \cdot U_{gmv}$，需比较两者数值。

## Evidence

先验知识/题面给定，逻辑校验通过
