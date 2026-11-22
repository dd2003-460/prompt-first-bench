# N211: CPU 推理 Decode 阶段受限于内存带宽，理论上限公式为 Throughput_decode = Memory_Bandwidth / (KV_Cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

CPU 推理 Decode 阶段受限于内存带宽，理论上限公式为 Throughput_decode = Memory_Bandwidth / (KV_Cache_Per_Token + Weights_Size_Per_Layer_Access)，其中 Weights_Size_Per_Layer_Access 取决于是否启用层卸载或全量加载，若全量加载则分母接近总权重大小 13.5 GB

## Corrected Claim

CPU 推理 Decode 阶段受限于内存带宽，理论上限公式为 Throughput_decode = Memory_Bandwidth / (KV_Cache_Per_Token + Weights_Size_Per_Layer_Access)，其中 Weights_Size_Per_Layer_Access 取决于是否启用层卸载或全量加载，若全量加载则分母接近总权重大小 13.5 GB

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中提到的两种权重加载策略（全量加载 vs 层卸载/混合），两者在架构配置、带宽计算逻辑及实际性能表现上互斥且互补，覆盖了父节点公式中 Weights_Size_Per_Layer_Access 变化的主要场景。）
