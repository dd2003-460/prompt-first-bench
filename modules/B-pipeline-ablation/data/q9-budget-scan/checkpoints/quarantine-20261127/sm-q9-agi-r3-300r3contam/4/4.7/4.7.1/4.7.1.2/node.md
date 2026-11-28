# N209: C_marginal_C 的精度修正：基于 AWS p4d.24xlarge ($32.77/hour) 的实测 T_inference（生成 1 token 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71, N72, N73

## Claim

C_marginal_C 的精度修正：基于 AWS p4d.24xlarge ($32.77/hour) 的实测 T_inference（生成 1 token 耗时），C_marginal_C = $32.77 / (3600 / T_inference_per_token)，需排除冷启动与队列等待时间，仅计算纯推理时间。

## Corrected Claim

C_marginal_C 的计算公式为：单位时间成本 / (3600 / T_inference_per_token)。其中单位时间成本应取当前所选区域和计费模式下 p4d.24xlarge 的实际费率（例如按需价格约为 $32.77/hour，具体以 AWS 实时报价为准），T_inference 需排除冷启动与队列等待，仅计纯推理时间。

## Evidence

[质询]p4d.24xlarge 的每小时价格随地区、计费模式（按需/预留/竞价）及时间波动，$32.77 仅为特定条件下的快照值，并非恒定常数；此外，T_inference 高度依赖模型大小和硬件配置，将其作为固定分母缺乏普适性。 | 来源 [3] 确认了 p4d.24xlarge 实例的存在及定价机制，但未提供固定的 $32.77 数值；该公式逻辑自洽，但具体价格属于经验事实且随市场变化，缺乏单一权威来源直接锁定该特定数值，故降级。

## Search Query

AWS p4d.24xlarge inference cost per token calculation

## Retrieval Sources

- {'url': 'https://aws.amazon.com/ec2/instance-types/p4/&rut=b0cc884c67eeabb5e56cff7a3b58aa1bbcc6ccde034dea821e415349513e6ac7', 'type': 'ddg', 'title': 'Amazon EC2 P4d Instances - AWS'}
- {'url': 'https://aws.amazon.com/cn/ec2/instance-types/p4/&rut=e93d3a3d514ba0d0cfd6bacb70ba3ddf37682ff6a2071d2c8ed62d939f8c6753', 'type': 'ddg', 'title': 'Amazon EC2 P4d 实例 — AWS'}
- {'url': 'https://cloudprice.net/aws/ec2/instances/p4d.24xlarge&rut=88d9de0beae776d229d0c4d52fde793bbf9bcbc0b33478adb46208a7fc6082c8', 'type': 'ddg', 'title': 'p4d.24xlarge specs and pricing | AWS | CloudPrice'}
