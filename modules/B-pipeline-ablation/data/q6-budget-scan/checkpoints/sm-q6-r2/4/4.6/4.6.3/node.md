# N144: 公有云基础设施成本 $C_{infra}^{pub}$ 的修正：虽然无固定硬件 CAPEX，但需计入预留实例/长期合约折扣后的带宽成本，即 $C_{infra}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

公有云基础设施成本 $C_{infra}^{pub}$ 的修正：虽然无固定硬件 CAPEX，但需计入预留实例/长期合约折扣后的带宽成本，即 $C_{infra}^{pub} = C_{bandwidth}^{pub} \cdot (1 - d_{discount})$，其中 $d_{discount} \in [10\%, 30\%]$（N17），此部分应合并至 $C_{bandwidth}^{pub}$ 或单独列出以避免重复计算。

## Corrected Claim

公有云基础设施成本 $C_{infra}^{pub}$ 的修正：虽然无固定硬件 CAPEX，但需计入预留实例/长期合约折扣后的带宽成本，即 $C_{infra}^{pub} = C_{bandwidth}^{pub} \cdot (1 - d_{discount})$，其中 $d_{discount} \in [10\%, 30\%]$（N17），此部分应合并至 $C_{bandwidth}^{pub}$ 或单独列出以避免重复计算。

## Evidence

先验知识/题面给定，逻辑校验通过
