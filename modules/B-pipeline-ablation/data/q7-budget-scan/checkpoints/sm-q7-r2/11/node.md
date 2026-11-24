# N39: HDD+SSD 分层方案的电力成本：HDD 功耗约 6-8W/盘（读写），400TB 需 40-80 块盘；SSD 热层 100TB 需 10-20 块盘。总磁

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

HDD+SSD 分层方案的电力成本：HDD 功耗约 6-8W/盘（读写），400TB 需 40-80 块盘；SSD 热层 100TB 需 10-20 块盘。总磁盘功耗约 300-700W，加上服务器其他部件，单节点功耗 500-900W。假设 2 节点，总功耗 1000-1800W。年电费 ≈ ¥10,000-¥19,000/年。

## Corrected Claim

HDD+SSD分层方案的电力成本：HDD 功耗约 6-8W/盘（读写），400TB 需 40-80 块盘；SSD 热层 100TB 需 10-20 块盘。总磁盘功耗约 300-700W，加上服务器其他部件，单节点功耗 500-900W。假设 2 节点，总功耗 1000-1800W。年电费取决于电价和负载率，按0.6元/度估算约为 ¥5,000-¥10,000/年（需根据实际电价调整）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1聚焦于硬件功耗参数的修正与细化（从父节点的粗略范围收敛到具体数值）；节点2基于节点1的结果进行系统级功耗和电费的重新计算（包含PUE等工程因子，这是对父节点缺失项的必要补充）；节点3提供对比结论和决策意义。三者层层递进，无重复或矛盾。）

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_33701251/article/details/159742859&rut=06a39a4dcd2ec5072301a60510e443e2ab3cc6e92d4c4ec7f018e462e4cdb4de', 'type': 'ddg', 'title': 'Hdd与ssd终极对决：性能、成本与应用场景全解析-csdn博客'}
- {'url': 'https://17nas.com/power-calculator.php&rut=555158f4a19d8de42ae3c507bf2b3eba092ba1e4ff0efb8c4f393028a9d96ce1', 'type': 'ddg', 'title': '硬盘功耗计算器 - Nas电费成本估算 | 17nas'}
- {'url': 'https://www.webkt.com/article/7290&rut=ad52efc47498b6440be31bb949fca46bb88daebf6cac45dac84182185a238a42', 'type': 'ddg', 'title': 'SSD vs HDD功耗深度对比：为你的设备选择更节能的存储方案'}
