# N83: 单POP节点月均带宽租赁成本 Bandwidth_Rent_Monthly = Reserved_Bandwidth_Mbps * Unit_Price_Per

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

单POP节点月均带宽租赁成本 Bandwidth_Rent_Monthly = Reserved_Bandwidth_Mbps * Unit_Price_Per_Mbps_Month，其中Reserved_Bandwidth_Mbps需覆盖该POP的峰值下行流量（Peak_Daily_Traffic_TB * 8 * 1000 / Peak_Hours），Unit_Price参考N36中的¥2.6-10/Mbps/月区间

## Corrected Claim

单POP节点月均带宽租赁成本 Bandwidth_Rent_Monthly = Reserved_Bandwidth_Mbps * Unit_Price_Per_Mbps_Month，其中Reserved_Bandwidth_Mbps需覆盖该POP的峰值下行流量（Peak_Daily_Traffic_TB * 8 * 1000 / Peak_Hours），Unit_Price参考N36中的¥2.6-10/Mbps/月区间

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点代表了三种不同的带宽采购策略/工作点（高冗余、平衡、低带宽），它们在带宽大小和单价上均不同，彼此互斥且无逻辑矛盾，符合正交性。父节点定义了成本计算公式及参数范围，子节点提供了该公式在三种典型场景下的具体实例化，覆盖了从保守到激进的不同业务场景，具备完备性。虽然子节点看起来像是一个参数的不同取值，但它们各自对应不同的业务假设（如是否覆盖长尾流量、冗余比例等）和对应的市场价格档位，并非简单的变量替换，而是具有不同语义的业务方案，因此不构成冗余。）

## Search Query

data center dedicated bandwidth cost per Mbps China tier 1 city
