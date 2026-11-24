# N33: NVMe SSD阵列的年度电力成本估算：500TB有效容量需约902.5TB物理容量，若使用1.92TB SSD，约需471块盘；单盘平均功耗20W，总功耗 =

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVMe SSD阵列的年度电力成本估算：500TB有效容量需约902.5TB物理容量，若使用1.92TB SSD，约需471块盘；单盘平均功耗20W，总功耗 = 471 * 20W = 9.42kW；加上控制器/背板/散热开销（约20%），总功耗约11.3kW；假设电价¥0.8/kWh，年电费 = 11.3kW * 24h * 365d * 0.8 ≈ ¥79,300元/年。

## Corrected Claim

基于假设的单盘功耗20W及电价¥0.8/kWh，500TB NVMe SSD阵列（约471块1.92TB盘）的年电力成本估算约为¥79,300元。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2与父节点存在严重数值矛盾（父节点固定20W，子节点推导为3.85W）；子节点3存在逻辑冗余和循环依赖（P_infra公式中引用了待求的P_total，且将散热功率简单设为总功耗10%在工程上不准确，应基于热流或独立估算）。）

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7626959842514616872/&rut=9290583ab1ed77c8e87515ced6424222f7f2c4f8bd379c05a684a7ffa92c0283', 'type': 'ddg', 'title': '电费刺客？一张表算清GPU服务器全生命周期能耗成本'}
