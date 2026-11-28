# N215: T_inference 的实测方法：使用 vLLM 基准测试工具，在 70B 模型上测量 1024 token 生成的平均墙钟时间，扣除队列等待与预处理时间，得

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71, N72, N73

## Claim

T_inference 的实测方法：使用 vLLM 基准测试工具，在 70B 模型上测量 1024 token 生成的平均墙钟时间，扣除队列等待与预处理时间，得到纯推理吞吐率。

## Corrected Claim

T_inference 的实测方法：使用 vLLM 基准测试工具，在 70B 模型上测量 1024 token 生成的平均墙钟时间，扣除队列等待与预处理时间，得到纯推理吞吐率。

## Evidence

先验知识/题面给定，逻辑校验通过
