# N318: Core_Peak_Bandwidth 的精确推导：日均下载 2TB，核心区域占 60%，则核心日均流量为 1.2TB。假设峰值系数 3，峰值集中在 4 小时，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N110

## Claim

Core_Peak_Bandwidth 的精确推导：日均下载 2TB，核心区域占 60%，则核心日均流量为 1.2TB。假设峰值系数 3，峰值集中在 4 小时，则 Core_Peak_Bandwidth = (1.2TB × 3) / 4h = 0.9TB/h ≈ 20.25 Gbps。预置 2x 峰值则为 40.5 Gbps。

## Corrected Claim

Core_Peak_Bandwidth = (1.2TB × 3) / 4h = 0.9TB/h ≈ 2.0 Gbps。预置 2x 峰值则为 4.0 Gbps。

## Evidence

先验知识/题面给定，逻辑校验通过：1.2TB * 3 / 4h = 0.9TB/h，0.9 * 8000 / 3600 ≈ 2.0 Gbps? 等等，计算检查：1 TB = 8000 Gb (通常工程估算用 10^12 bytes * 8 / 10^9 bits = 8000 Gb，或者 1024^4 * 8 / 10^9 ≈ 8589 Gb)。若按 1TB=8000Gb: 0.9 * 8000 / 3600 = 7200 / 3600 = 2 Gbps。若按 1TB=8589Gb: 0.9 * 8589 / 3600 ≈ 2.15 Gbps。题目中声称 0.9TB/h ≈ 20.25 Gbps。让我们重新检查单位换算。1 TB/h = 10^12 bytes / 3600 s = 2.77 * 10^8 bytes/s = 2.22 * 10^9 bits/s ≈ 2.22 Gbps。所以 0.9 TB/h ≈ 2 Gbps。题目中的 20.25 Gbps 是 10 倍左右的错误？或者题目使用了不同的 TB 定义？如果 1 TB = 8000 Gb，1 TB/h = 8000/3600 Gbps ≈ 2.22 Gbps。0.9 * 2.22 = 2 Gbps。如果题目认为 1 TB = 80000 Gb? 不可能。如果题目把小时当成了分钟？0.9 TB / 4 min? 不，题目说是 4 小时。如果题目把 TB 当成了 GB? 1.2 GB * 3 / 4h = 0.9 GB/h = 0.002 Gbps。如果题目把 1.2 TB 算成了 1200 GB，然后 1200 * 3 / 4 = 900 GB/h。900 GB/h = 900 * 8 / 3600 Gbps = 2 Gbps。怎么算都是 2 Gbps 左右。20.25 Gbps 对应的是 0.9 TB / 0.4 h? 或者 9 TB / 4h? 9 TB / 4h = 2.25 TB/h = 5 Gbps。还是不对。20.25 Gbps * 3600 / 8000 = 9.11 TB/h。这意味着峰值流量是 9.11 TB/h。而题目推导是 0.9 TB/h。这里存在明显的数量级计算错误（约10倍）。0.9 TB/h ≈ 2 Gbps，而非 20.25 Gbps。因此逻辑校验失败（数值计算错误）。
