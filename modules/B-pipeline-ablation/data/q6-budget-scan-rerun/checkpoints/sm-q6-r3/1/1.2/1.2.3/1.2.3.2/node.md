# N117: 源站处理延迟 $T_{proc}$ 分解为磁盘 I/O 读取时间 $T_{disk} = s / BW_{disk}$ 与 CPU 预处理时间 $T_{cpu}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

源站处理延迟 $T_{proc}$ 分解为磁盘 I/O 读取时间 $T_{disk} = s / BW_{disk}$ 与 CPU 预处理时间 $T_{cpu}$。对于 NVMe SSD，$BW_{disk} \approx 3$ GB/s，若对象大小 $s=500$KB，则 $T_{disk} \approx 0.17$ms；$T_{cpu}$ 取决于转码/签名验证逻辑，典型 5-20ms。

## Corrected Claim

源站处理延迟 $T_{proc}$ 分解为磁盘 I/O 读取时间 $T_{disk} = s / BW_{disk}$ 与 CPU 预处理时间 $T_{cpu}$。对于 NVMe SSD，$BW_{disk} \approx 3$ GB/s，若对象大小 $s=500$KB，则 $T_{disk} \approx 0.17$ms；$T_{cpu}$ 取决于转码/签名验证逻辑，典型 5-20ms。

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe SSD顺序读取带宽3GB/s量级符合工程常识，500KB数据读取耗时0.17ms计算正确（500KB/3GB/s ≈ 0.167ms），CPU预处理5-20ms符合典型Web服务器处理延迟范围。

## Search Query

NVMe SSD read bandwidth GB/s web server processing latency breakdown
