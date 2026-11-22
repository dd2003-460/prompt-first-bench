# N444: INT4 (AWQ, group_size=128) 量化导致模型在 HellaSwag 基准上的准确率下降约为 1.5-2.5%，具体数值取决于量化算法细节，

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N137

## Claim

INT4 (AWQ, group_size=128) 量化导致模型在 HellaSwag 基准上的准确率下降约为 1.5-2.5%，具体数值取决于量化算法细节，需通过实际推理测试验证 [待核验]。

## Corrected Claim

INT4 (AWQ, group_size=128) 量化通常会导致模型在基准测试上出现轻微精度下降，具体数值（如HellaSwag上的表现）取决于模型规模与量化校准细节，需通过实际推理测试验证。

## Evidence

[质询]该陈述包含具体的经验数值范围（1.5-2.5%），属于硬件/模型性能经验事实，无法从第一性原理推导。参考来源仅讨论了AWQ量化配置、Group Size的技术原理及权衡，未提供HellaSwag基准上具体的准确率下降数值，缺乏直接数据支持。 | 逻辑自洽（INT4量化通常导致轻微精度损失），但来源[1][2][3]仅涉及量化配置与原理，未提供HellaSwag具体下降数值，属经验事实且缺来源直接支持。

## Search Query

Qwen3-27B AWQ INT4 group_size=128 HellaSwag accuracy drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00791/article/details/168448598&rut=829cc182a9dbaada401d01896b2b1b7f7f6d543b3647398afc9a607d9e892382', 'type': 'ddg', 'title': '逐行解读Qwen3.8-27B-Quark-AWQ-INT4-W4A16的quantization_config：Group Size 128 ...'}
- {'url': 'https://geek-doc.cn/chip-design/intermediate/int4-awq-group-size-tradeoff&rut=9bfa5676f56836a2c78c5e828649e83f195a7bc150a298717f97e16b4d701c84', 'type': 'ddg', 'title': 'AWQ group size 折中：INT4 分组量化在精度、体积、kernel 效率上的三角取舍与选型经验'}
- {'url': 'https://blog.csdn.net/gitblog_00092/article/details/168144054&rut=178329845a0459cec0266d9bf21683477e42cba0e55281e267886247fc13452f', 'type': 'ddg', 'title': 'Phi-4-mini-instruct_ral 量化原理揭秘：AWQ、Group 128 与 UINT4 权重如何炼成'}
