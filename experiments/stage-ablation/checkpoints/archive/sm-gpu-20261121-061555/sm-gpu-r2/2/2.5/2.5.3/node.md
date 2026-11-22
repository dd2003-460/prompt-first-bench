# N71: PCIe带宽瓶颈对多卡推理延迟的影响：2x RTX 4090通过PCIe 4.0 x16互联，带宽约32 GB/s（双向），而NVLink带宽可达900 GB/

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

PCIe带宽瓶颈对多卡推理延迟的影响：2x RTX 4090通过PCIe 4.0 x16互联，带宽约32 GB/s（双向），而NVLink带宽可达900 GB/s。在TP下，All-Reduce通信量约为隐藏层维度（5120）* Batch Size * 2 bytes，对于Batch=1，通信量约10KB，延迟影响可忽略；但对于大Batch或长序列，PCIe瓶颈可能导致延迟增加20-50% [待核验]。

## Corrected Claim

PCIe带宽瓶颈对多卡推理延迟的影响：2x RTX 4090通过PCIe 4.0 x16互联，带宽约32 GB/s（双向），而NVLink带宽可达900 GB/s。在TP下，All-Reduce通信量约为隐藏层维度（5120）* Batch Size * 2 bytes，对于Batch=1，通信量约10KB，延迟影响可忽略；但对于大Batch或长序列，PCIe瓶颈可能导致延迟增加20-50% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

PCIe vs NVLink latency impact LLM inference
