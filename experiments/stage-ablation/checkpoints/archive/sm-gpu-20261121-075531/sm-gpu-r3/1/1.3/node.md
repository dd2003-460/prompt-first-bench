# N8: 激活值与框架开销显存占用量 ≈ 1-2GB (PyTorch/CUDA runtime, 临时激活值缓冲, 取决于batch size=1)

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

激活值与框架开销显存占用量 ≈ 1-2GB (PyTorch/CUDA runtime, 临时激活值缓冲, 取决于batch size=1)

## Corrected Claim

激活值与框架开销显存占用量 ≈ 1-2GB (PyTorch/CUDA runtime, 临时激活值缓冲, 取决于batch size=1)

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点严格区分了'动态激活值'（依赖序列长度/模型结构）与'静态框架开销'（依赖运行时环境/后端），两者在显存构成上互斥且无重叠。父节点提到的'PyTorch/CUDA runtime'和'临时激活值'分别被第二个和第一个子节点覆盖，逻辑完备。）
