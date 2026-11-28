# N153: 典型科研数值计算脚本（如 10^6 次 Monte Carlo 采样，d=1000）的执行时间：基于 N102，JAX 在 V100 上耗时约 0.3s，加上数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

典型科研数值计算脚本（如 10^6 次 Monte Carlo 采样，d=1000）的执行时间：基于 N102，JAX 在 V100 上耗时约 0.3s，加上数据传输（PCIe 1GB/s，假设数据 100MB 则 100ms）和结果序列化（<50ms），总执行时间 P50 <0.5s

## Corrected Claim

典型科研数值计算脚本（如 10^6 次 Monte Carlo 采样，d=1000）的执行时间：基于 N102，JAX 在 V100 上耗时约 0.3s，加上数据传输（PCIe 1GB/s，假设数据 100MB 则 100ms）和结果序列化（<50ms），总执行时间 P50 <0.5s

## Evidence

先验知识/题面给定，逻辑校验通过：JAX在V100上执行10^6次Monte Carlo采样（d=1000）耗时约0.3s符合GPU计算性能预期；PCIe 1GB/s传输100MB数据耗时100ms及序列化<50ms均为合理工程估算，总时间P50<0.5s逻辑自洽且量级合理。
