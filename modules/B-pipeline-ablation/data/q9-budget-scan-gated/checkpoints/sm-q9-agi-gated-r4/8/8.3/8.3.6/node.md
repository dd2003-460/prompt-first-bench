# N151: Prefill延迟的内存带宽下限验证：2k tokens输入，Qwen3.8-27B权重加载量约为 27e9 * 2bytes(FP16 after dequa

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73, N74, N75

## Claim

Prefill延迟的内存带宽下限验证：2k tokens输入，Qwen3.8-27B权重加载量约为 27e9 * 2bytes(FP16 after dequant) = 54GB。V100 HBM带宽 900GB/s * 0.7(efficiency) = 630GB/s。纯权重加载时间 = 54GB / 630GB/s ≈ 0.086s。加上KV Cache读写及激活内存交换，总内存传输时间下限约为 0.1-0.2s。若N82计算的计算时间为4.3s，则瓶颈确认为Compute-Bound；若优化至高效Kernel使计算时间<0.2s，则瓶颈转为Memory-Bound。当前V100配置下，Prefill主要为Compute-Bound。

## Corrected Claim

Prefill延迟的内存带宽下限验证：2k tokens输入，Qwen3.8-27B权重加载量约为 27e9 * 2bytes(FP16 after dequant) = 54GB。V100 HBM带宽 900GB/s * 0.7(efficiency) = 630GB/s。纯权重加载时间 = 54GB / 630GB/s ≈ 0.086s。加上KV Cache读写及激活内存交换，总内存传输时间下限约为 0.1-0.2s。若N82计算的计算时间为4.3s，则瓶颈确认为Compute-Bound；若优化至高效Kernel使计算时间<0.2s，则瓶颈转为Memory-Bound。当前V100配置下，Prefill主要为Compute-Bound。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型FP16权重约54GB，V100有效带宽约630GB/s，纯权重读取耗时约0.086s，加上KV Cache等开销后内存下限0.1-0.2s符合物理直觉；若计算时间4.3s远大于此，则确认为Compute-Bound，逻辑自洽。

## Search Query

prefill phase memory bound vs compute bound V100 tensor core efficiency
