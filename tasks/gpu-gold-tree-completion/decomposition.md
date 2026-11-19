# gpu gold 树完善 — 任务分解

> origin: ai · 2026-11-19
> goal: gpu-gold-tree-completion
> phase: 1-decompose

## 最终目标

完善 gpu gold 树（`bench/rubric-v3/ablation/gold-tree.md`，31 节点），使其满足 D 的要求：
1. 微架构显式分解（SM/TensorCore/L2/INT8/INT4 kernel 不藏在 MFU/η_bw 黑盒里）
2. TCO 分解完整性（份额和=100%，正交性全过）
3. 不同显卡搜索比较（V100/TPU/片上内存）
4. 厂商变体砍掉（只留旗舰）
5. 正交性在完备性之前逐步检查

## 分解树（正交子项）

```
gpu gold 树完善
├─ A. 微架构显式分解
│  ├─ A1. MFU 黑盒拆解（N-3.1.3，B2）
│  │  └─ 子项：SM 占用率 / TensorCore 利用率 / L2 命中率 / kernel 效率
│  ├─ A2. η_bw 黑盒拆解（N-3.2.4，B3）
│  │  └─ 子项：HBM 带宽利用率 / L2 缓存命中 / kernel launch 开销
│  └─ A3. 数值来源确认（每个子项的公式 + 实测值）
│
├─ B. TCO 分解完整性核查
│  ├─ B1. 现有 N-1 覆盖范围审计（持有成本 42.8%+49.3%+8.0%=100.1%）
│  ├─ B2. 缺失项识别（运维/网络/软件/人力/机会成本）
│  └─ B3. 份额重新分配（保证正交 + 和=100%）
│
├─ C. 不同显卡搜索比较
│  ├─ C1. 候选硬件扩展（现有 3090/M2Ultra/L40S/A100 → 加 V100/TPU/片上内存）
│  ├─ C2. 数值填充（从 knowledgebase/hardware/ 取）
│  └─ C3. 公式适用性验证（现有 gold 树公式对新硬件是否成立）
│
├─ D. 厂商变体砍掉
│  └─ D1. gold 树里是否有变体（需读全文确认；知识库已砍，gold 树可能没有）
│
└─ E. 正交性逐步检查
   ├─ E1. 正交性标准定义（什么算正交、什么算重叠）
   └─ E2. 每个新节点加入前检查（与现有 31 节点逐一比对）
```

## 缺口标注

| 子项 | 缺什么 | 怎么补 |
|---|---|---|
| A1/A2 | MFU/η_bw 子项的具体定义（SM 占用率怎么算、TensorCore 利用率怎么测） | 查 L5-blackbox.md（缺失）或 arena 调研 |
| A3 | 每个子项的实测数值 | 知识库 + arena 调研 |
| B2 | TCO 完整分解的行业标准（运维/网络/软件份额怎么定） | arena 调研（对标顶刊/高 star 开源） |
| C3 | 现有 gold 树公式对新硬件（TPU/片上内存）是否适用 | 需验证（TPU 没有 SM/TensorCore，公式可能不适用） |
| D1 | gold 树里是否有变体 | 读 gold-tree.md 全文（已读，初步判断没有变体，只有 3090/M2Ultra/L40S/A100） |
| E1 | 正交性标准 | 需定义（建议：两个节点如果共享同一个物理量或公式项，就算重叠） |

## 留空（不确定的标 [待核验]）

- L0-L5/calc.py 缺失 [待核验：是否在 archive 或旧 commit 里能找回来]
- MFU 子项的具体数值 [待核验]
- η_bw 子项的具体数值 [待核验]
- TCO 运维/网络/软件的份额 [待核验]
- TPU/片上内存是否适用现有 gold 树公式 [待核验]

## 任务表（phase2 执行用）

| # | 任务 | 验收标准 | 依赖 |
|---|---|---|---|
| T1 | 查 L5-blackbox.md（是否在 archive/旧 commit） | ✅ 完成：L0-L5 在 `projects/decomp/bench/gold/`（独立 git 仓库，pfb 搬家时引用没跟）；calc.py 确认缺失（两个仓库都没有）；B2/B3 完整定义已获取 | - |
| T2 | MFU 子项定义 + 数值（SM 占用率/TensorCore 利用率/L2 命中/kernel 效率） | 4 个子项，每个有公式 + 实测值（出处） | T1 |
| T3 | η_bw 子项定义 + 数值（HBM 带宽利用率/L2 缓存命中/kernel launch 开销） | 3 个子项，每个有公式 + 实测值（出处） | T1 |
| T4 | TCO 缺失项识别 + 份额重新分配 | 新 N-1 子项列表，份额和=100%，正交性全过 | - |
| T5 | 候选硬件扩展（V100/TPU/片上内存）+ 数值填充 | 3 类新硬件，每个有完整规格（出处：knowledgebase） | - |
| T6 | 公式适用性验证（TPU/片上内存） | 验证报告：哪些公式适用、哪些不适用、为什么 | T5 |
| T7 | 正交性标准定义 + 逐步检查 | 标准文档 + 31+新节点的正交性核对表 | T2/T3/T4/T5 |
| T8 | gold 树更新（tree.md 新增节点 + 公式 + SHARE 份额） | tree.md 更新，commit+push | T2-T7 |

## 正交性核对

- A（微架构）vs B（TCO）：正交（A 是性能侧，B 是成本侧）
- A vs C（显卡比较）：正交（A 是单卡内部分解，C 是跨卡比较）
- B vs C：正交（B 是成本分解，C 是硬件扩展）
- D（变体砍掉）：独立（知识库已做，gold 树初步判断没有变体）
- E（正交性检查）：元任务（检查 A/B/C/D 的产出是否正交）

## 与 S5 管线的关系

- 本 goal 完善的是"标准答案"（gold 树），S5 管线（verify-only 在跑）是"agent 能不能答对"
- 两条线独立：gold 树完善后，S5 管线的 gpu depth 指标会基于新 gold 树重新计算
- 不阻塞：verify-only 跑完对账 depth 是 pfb-hardening-v2 的事，本 goal 是 gpu-gold-tree-completion 的事
