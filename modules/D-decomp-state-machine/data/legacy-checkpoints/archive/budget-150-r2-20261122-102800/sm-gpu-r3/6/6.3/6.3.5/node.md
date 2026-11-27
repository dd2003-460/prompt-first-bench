# N141: BF16 精度支持：NVIDIA RTX 4090/A100/H100 均原生支持 BF16 计算 (Tensor Core)；AMD RX 7900 XTX 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45, N46, N47

## Claim

BF16 精度支持：NVIDIA RTX 4090/A100/H100 均原生支持 BF16 计算 (Tensor Core)；AMD RX 7900 XTX 通过 ROCm 支持 BF16，但性能约为 FP16 的 80-90% (由于指令集差异)，且内存带宽利用率降低约 10%。

## Corrected Claim

NVIDIA RTX 4090/A100/H100 均原生支持 BF16 计算 (Tensor Core)；AMD RX 7900 XTX 通过 ROCm 支持 BF16，但受指令集和软件栈优化程度影响，其 BF16 性能通常低于 FP16，具体性能损耗因驱动版本和工作负载而异。

## Evidence

[质询]AMD RX 7900 XTX 在 ROCm 下 BF16 性能仅为 FP16 的 80-90% 且内存带宽利用率降低 10% 属于具体经验性能数据，缺乏公开基准测试支持，且不同软件栈版本下表现差异较大，该具体数值区间可能不准确或过时。 | NVIDIA 支持 BF16 为公认事实，逻辑自洽；但 AMD 具体性能损耗比例（80-90%）及带宽利用率降低 10% 为经验事实，无来源支持且无法从第一性原理严格推出，故降级。
