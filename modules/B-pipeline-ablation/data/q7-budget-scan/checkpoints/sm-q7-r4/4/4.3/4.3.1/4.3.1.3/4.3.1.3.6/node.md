# N721: RAID控制器DMA引擎将SSD数据拷贝到系统内存再送CPU进行校验计算的内存带宽占用约为重建速率的2倍，即3.0GB/s重建对应6.0GB/s内存带宽消耗

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N250, N251, N252

## Claim

RAID控制器DMA引擎将SSD数据拷贝到系统内存再送CPU进行校验计算的内存带宽占用约为重建速率的2倍，即3.0GB/s重建对应6.0GB/s内存带宽消耗

## Corrected Claim

RAID控制器DMA引擎将SSD数据拷贝到系统内存再送CPU进行校验计算的内存带宽占用约为重建速率的2倍，即3.0GB/s重建对应6.0GB/s内存带宽消耗

## Evidence

先验知识/题面给定，逻辑校验通过：RAID重建涉及数据从存储读取到内存（1x带宽）及后续处理/写入产生的额外内存流量，通常总内存带宽消耗约为重建速率的2倍，符合工程常识。
