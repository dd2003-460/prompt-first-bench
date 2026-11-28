# N168: T_inference_max 的具体数值依赖于最大生成长度 L_gen 与硬件有效解码速度 v_decode (tokens/s)，即 T_inference

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58

## Claim

T_inference_max 的具体数值依赖于最大生成长度 L_gen 与硬件有效解码速度 v_decode (tokens/s)，即 T_inference_max = L_gen / v_decode + T_prefill，需实测 27B 模型在当前负载下的 v_decode 以消除估算偏差。

## Corrected Claim

T_inference_max 通常由预填充时间和生成时间组成，其中生成时间取决于最大生成长度与解码速度，具体数值需根据实际硬件和模型负载实测确定。

## Evidence

[质询]该陈述包含具体的工程经验参数（27B模型、特定负载下的v_decode需求），属于经验事实，无法仅从第一性原理严格推出具体数值或唯一解，且参考来源未提供该具体公式的实证数据支持。 | 逻辑自洽（推理时间由预填充和生成阶段组成，生成时间与长度成正比），但参考来源[1]仅介绍InferenceMAX基准测试套件，未直接支持该具体公式及27B模型的实测要求，属经验事实缺来源直接支持。

## Search Query

vLLM qwen 27b decoding speed tokens per second benchmark v100

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/InferenceMAX/68231139&rut=8d4d302be33a660cf51218f6279036b3165c333c32651af39df619f93c5c5443', 'type': 'ddg', 'title': 'InferenceMAX_百度百科'}
