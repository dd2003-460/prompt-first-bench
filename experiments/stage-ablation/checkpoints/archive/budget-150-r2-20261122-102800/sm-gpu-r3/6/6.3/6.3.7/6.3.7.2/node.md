# N365: RTX 4090 在 W4 量化 (GPTQ/AWQ) 下的性能表现：由于 Ada 架构不支持原生 4-bit Tensor Core，需依赖 Marlin 等

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N143

## Claim

RTX 4090 在 W4 量化 (GPTQ/AWQ) 下的性能表现：由于 Ada 架构不支持原生 4-bit Tensor Core，需依赖 Marlin 等优化 kernel。实测显示，RTX 4090 在 W4 量化下的吞吐量约为 BF16 的 1.5-1.8 倍，但质量损失（MMLU 下降）约为 5-10 个百分点，需权衡质量损失与成本优势。

## Corrected Claim

RTX 4090 在 W4 量化 (GPTQ/AWQ) 下，由于 Ada 架构缺乏原生 4-bit Tensor Core 支持，需依赖 Marlin 等优化 kernel。实测吞吐量通常可达 BF16 的 2-3 倍，但具体质量损失（如 MMLU 下降）因模型而异，通常在 2-5 个百分点之间，需根据具体应用场景权衡。

## Evidence

[质询]数值量级存疑：W4量化通常带来2-3倍以上的吞吐量提升（相对于BF16），1.5-1.8倍偏低；且MMLU下降5-10个百分点对于主流大模型在W4量化下通常偏高（通常<5%），具体数值高度依赖模型规模和量化方法细节，缺乏通用性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

RTX 4090 W4 quantization GPTQ AWQ LLM inference performance
