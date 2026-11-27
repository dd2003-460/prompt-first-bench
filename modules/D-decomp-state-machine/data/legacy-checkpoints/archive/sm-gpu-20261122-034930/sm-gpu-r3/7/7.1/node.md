# N139: AMD MI300X显存带宽为5.3 TB/s (HBM3)，是RTX 4090 (1.0 TB/s)的5.3倍，在Memory-bound推理中理论峰值吞吐量

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

AMD MI300X显存带宽为5.3 TB/s (HBM3)，是RTX 4090 (1.0 TB/s)的5.3倍，在Memory-bound推理中理论峰值吞吐量约为RTX 4090的5倍，但需扣除PCIe/Infinity Fabric通信开销（多卡时）或单卡调度开销。

## Corrected Claim

AMD MI300X显存带宽为5.3 TB/s (HBM3)，是RTX 4090 (1.0 TB/s)的5.3倍，在Memory-bound推理中理论峰值吞吐量约为RTX 4090的5倍，但需扣除PCIe/Infinity Fabric通信开销（多卡时）或单卡调度开销。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X HBM3带宽5.3TB/s与RTX 4090 GDDR6X带宽约1TB/s的数值量级符合硬件规格常识，5.3倍带宽比在Memory-bound场景下对应约5倍理论吞吐量的推导逻辑自洽。

## Search Query

AMD MI300X HBM3 bandwidth GB/s specification
