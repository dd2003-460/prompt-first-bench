# correctness 层设计 v0（修复 coverage 陷阱）

# origin: ai（2026-11-25，sub 任务；前 sub sa-0-54c3e480 死于输出 token 上限，本文档为其落盘）

## §0 问题定义：coverage 陷阱

- 现状：pfb 测量层（judge_v1.py, frozen f6072397f）只测 **coverage**（bge-m3 嵌入相似度 vs gold 36 单元），不测 **correctness**（推理链是否对齐 gold 结构）。
- D 已确认（2026-11-25）：coverage 是 correctness 的**必要条件非充分条件**；gold 稳定部分 = **树结构（准入规则 + 计算路径）**，不是赢家标签。
- 陷阱实例：一条输出可以高 coverage（提到带宽门、TCO、量化），但推理链在错误位置断裂，结论仍错。两种断点必须机械区分：
  - **A1 型（候选构建断点）**：winner 卡型/配置从未进入候选集。实锤：T8b arm_a[0] 全文 3090 count=0（salvage 已验证）。
  - **A3 型（排序/权重断点）**：winner 配置被完整评估（进候选表、进打分表）但最终排序垫底。实锤：T8b arm_a[2] 含 4×3090 完整评估上下文，加权分 5.9 垫底，最终推荐 2×4090（salvage 已验证）。
- 本层只回答一个问题：**correctness 层能否机械区分"coverage 够但结论错"的两类原因（A1 vs A3）**。不做质量提升 claim。

<!-- cont -->
