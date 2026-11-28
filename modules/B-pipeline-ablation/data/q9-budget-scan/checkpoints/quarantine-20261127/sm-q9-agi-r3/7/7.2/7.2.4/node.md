# N267: NVFP4 在 V100 (Compute Cap 7.0) 上因缺乏原生 FP4 Tensor Core 支持，其推理吞吐量相比 FP16 的实际加速比为 [

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N92

## Claim

NVFP4 在 V100 (Compute Cap 7.0) 上因缺乏原生 FP4 Tensor Core 支持，其推理吞吐量相比 FP16 的实际加速比为 [待核验]，若实测值 < 1.5，则触发 N92 描述的切换至 INT8 的条件；需实测 V100 上 NVFP4 反量化到 FP16 的 kernel 耗时占比。

## Corrected Claim

NVFP4 在 V100 (Compute Cap 7.0) 上因缺乏原生 FP4 Tensor Core 支持，需通过软件模拟实现推理。实测显示其在 27B 模型上可达 35.5 tok/s，但具体相比 FP16 的加速比需结合 FP16 基准测试确定；若实测加速比 < 1.5，则建议切换至 INT8。

## Evidence

[质询]陈述中声称加速比数值为“[待核验]”，这是一个占位符而非具体事实；此外，虽然来源提供了吞吐量数据（35.5 tok/s），但未提供同条件下 FP16 的基准吞吐量，因此无法从现有来源直接计算出确切的加速比数值，也无法确认其是否小于 1.5。 | 来源 [1] 和 [2] 证实了 NVFP4 在 V100 上是通过软件模拟实现的（无原生硬件支持），并给出了特定模型下的吞吐量（35.5 tok/s），但未提供 FP16 对比数据以计算加速比，故具体数值缺乏直接支持，仅能确认技术路径和定性逻辑。

## Search Query

V100 NVFP4 quantization performance overhead V100 no native FP4 support

## Retrieval Sources

- {'url': 'https://github.com/maco1979/nvfp4-v100&rut=afc180d886d64b69dacbfbc0070dabb0733bdd2681af1f561709145f88c8ba87', 'type': 'ddg', 'title': 'NVFP4 on V100 — Software-Simulated FP4 Inference - GitHub'}
- {'url': 'https://github.com/maco1979/nvfp4-v100/blob/main/README.md&rut=c55e18a74de69f87faffc39df1aafe4c399ddc031aec54d163b3827b4928c3b5', 'type': 'ddg', 'title': 'nvfp4-v100/README.md at main · maco1979/nvfp4-v100 · GitHub'}
