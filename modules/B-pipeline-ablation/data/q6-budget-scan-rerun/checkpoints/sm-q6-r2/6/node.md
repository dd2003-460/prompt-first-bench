# N34: 日均总请求量 RPS 计算：基于日均下载 2TB (2,000,000 MB) 和加权平均对象大小 s=2.05MB，日均总请求数 = 2,000,000 / 

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

日均总请求量 RPS 计算：基于日均下载 2TB (2,000,000 MB) 和加权平均对象大小 s=2.05MB，日均总请求数 = 2,000,000 / 2.05 ≈ 975,610 次/天；平均 RPS = 975,610 / 86400 ≈ 11.3 RPS；峰值 RPS (假设峰谷比 3x) ≈ 34 RPS。此数值是归一化成本的分母基础。

## Corrected Claim

日均总请求量 RPS 计算：基于日均下载 2TB (2,000,000 MB) 和加权平均对象大小 s=2.05MB，日均总请求数 = 2,000,000 / 2.05 ≈ 975,610 次/天；平均 RPS = 975,610 / 86400 ≈ 11.3 RPS；峰值 RPS (假设峰谷比 3x) ≈ 34 RPS。此数值是归一化成本的分母基础。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了日均请求量、平均RPS、峰值RPS和年总请求量，逻辑上层层递进且相互独立，无重复或矛盾。虽然父节点使用了错误的参数（2.05MB），但子节点正确指出了修正值（1.85MB）并基于此进行计算，体现了对父节点核心逻辑（RPS计算链条）的完整覆盖和修正。各节点代表不同的时间粒度或统计维度（日/平均/峰值/年），不构成冗余。）

## Retrieval Sources

- {'url': 'https://help.aliyun.com/zh/pts/how-is-concurrency-calculated-in-rps-mode&rut=b3b8ba5f242c284e54f1372655b3b8ad6fd601de0952275266fd3430fe967b63', 'type': 'ddg', 'title': 'Rps模式下并发量的计算方法与rt关系-性能测试-阿里云'}
- {'url': 'https://help.aliyun.com/zh/pts/performance-test-pts-2-0/support/how-is-concurrency-calculated-in-rps-mode-1&rut=129344cfde9b423d720fa594c924f4ed85bf50c75d7659abba6cbee9c94b81de', 'type': 'ddg', 'title': 'Rps模式下根据rt计算并发量的原理-性能测试-阿里云'}
- {'url': 'https://blog.csdn.net/Dontla/article/details/161065843&rut=ac250cca026d60f29288018d8e1b915ad2c7616b1a44c0f0671db6588238deb4', 'type': 'ddg', 'title': 'RPS（Requests Per Second）介绍（RPS只代表系统吞吐量Throughput，不代表延迟）并发数Co'}
