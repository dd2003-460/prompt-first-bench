# N34: 在日均 2TB 下载量下，若平均对象大小 $s_{avg}$ 从 1MB 增加到 5MB，日均请求量 $R_{daily}$ 从 200 万降至 40 万，导致

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在日均 2TB 下载量下，若平均对象大小 $s_{avg}$ 从 1MB 增加到 5MB，日均请求量 $R_{daily}$ 从 200 万降至 40 万，导致公有云按流量计费成本不变，但自建节点的并发连接数下降 80%，使得 P99 延迟中的排队延迟显著降低。

## Corrected Claim

在日均 2TB 下载量下，若平均对象大小从 1MB 增加到 5MB，日均请求量从 200 万降至 40 万，公有云按流量计费成本保持不变；由于请求量大幅减少，自建节点的并发连接数预计显著下降，从而可能降低 P99 延迟中的排队延迟。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于排队延迟（L_queue）随并发连接数/到达率变化的非线性下降机制；子节点2聚焦于单流传输时间（T_transfer）随对象大小增加的线性增长及其对总P99延迟的综合影响。两者分别处理延迟公式中的不同分量，逻辑上互补且互不重叠，共同完整解释了父节点中P99延迟变化的两个主要驱动因素（排队改善 vs 传输恶化）。）

## Retrieval Sources

- {'url': 'https://www.gigacalculator.com/calculators/download-time-calculator.php&rut=85dc96fc304378a05f8da9945682c476c4cc2b3cd290e4dde75d5951dd4e5308', 'type': 'ddg', 'title': 'Download Time Calculator'}
- {'url': 'https://www.omnicalculator.com/other/download-time&rut=09ca720a107a01fc867cfee398fb8ffc0e2d35647d90ef5b1db86e382a2c8f15', 'type': 'ddg', 'title': 'Download Time Calculator'}
- {'url': 'https://calculatorlib.com/zh/data-transfer-calculator&rut=6e331f2ee1d98dbd0f2d11f94abd7c9735d464d3b194a6e557f2f45928fe0db3', 'type': 'ddg', 'title': '数据传输时间计算器 | 快速估算文件下载与上传时长 - CalculatorLib'}
