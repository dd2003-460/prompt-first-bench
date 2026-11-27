# 实验路线图（一页总图 · 2026-11-22）

# origin: ai
**用途**: D 问"按什么思路跑实验、要获得什么效果"——本文件是唯一入口。
规划细节在下方链接文件，本文件只画关系，不重复内容。

## 终极目标（D 2026-11-22 睡前指令）

在 D 硬件条件下（4×V100 + 本地 27b + 不改权重），找到**性价比最高、最快、最可靠**达到 AGI 的路径。
核心机制：**预算 = 覆盖度控制旋钮**——预算大 = 完整覆盖所有贡献因子（如 gold），预算小 = 压缩细节。
**主交付物**: 预算-质量 Pareto 曲线 + 拐点（性价比最优点）。

## 逻辑链（为什么跑这些实验，谁服务谁）

```
终极目标: D 硬件下性价比最快达 AGI
└── 主实验: 预算扫描 → Pareto 曲线 → 拐点          [K7, 在跑 13/15]
    ├── 前提① 管线值得跑吗?                        [T53b, CLOSED ✓ SM 胜裸跑]
    ├── 前提② 打分可信吗?                          [T-JUDGE-1, ACTIVE]
    │     └── 发现: 旧 judge coverage ≈ 长度代理 (r=0.861)
    │           → 质量轴 = 同族 LLM judge 分, 报告必须标注 self-judge 偏差
    ├── 机制验证: prompt 序列影响终态吗?            [T-PR-17, PENDING 等 K7 释放 vLLM]
    │     └── = D 收敛假说的直接检验 (null control 测纯扰动 X)
    └── 诊断: 最高分 run 为什么高?                  [0.5184 解剖, DONE]
          └── 不是结构深, 是 judge 分高 (同构对 Δ=0.167 > 预算档差异)
```

发表线（并行，不阻塞实验）: novelty 锚 = **评测协议**（gold 树 + 逐判定点连续分 +
n=10 复现性/CI/效应量），conf 0.75（arena T-PR-16 对抗核验后）。
TCO 时间分解 = 背景引用（十年老题，不能当 novelty）。套磁可现在进行（卖实验纪律）。

## 实验清单（一行一个: 回答什么 / 状态 / 交付物）

| 实验 | 回答的问题 | 状态 | 交付物 |
|---|---|---|---|
| T53b matched 批 | SM 管线比裸跑好吗? | CLOSED | SM 胜 nat +0.131 p=0.016 / gpu +0.105 p=0.022 |
| K6 merge 消融 | merge 是压缩瓶颈吗? | DONE | 否 (Δ=-0.013, A≈B) |
| K7 预算扫描 | 预算-质量 Pareto 什么形状? | DONE(11-24 池化) | cov 轴 ~300 节点饱和 + metacog 独立于预算 (k7-pareto-newjudge-20261124.md); Q7 跨题验证在 relay 链 |
| T-JUDGE-1 | 怎么客观打分? | ACTIVE | embedding judge + 磁体检测 + LLM 兜底 (102 条待跑) |
| gold 映射修复 | K7 的 gold 用对了吗? | DONE 3f5c713f7 | 旧 gold/Q1.md 是另一道题 (H100 SXM vs PCIe); 改挂 rubric-v3 37 节点树 + enriched sidecar, 覆盖 6/36→20/36 |
| T-PR-17 | prompt 序列影响终态吗? | PENDING | 4 臂消融 (canonical/verify-off/null-control/verify-late) |
| 0.5184 解剖 | 最高分 run 为什么高? | DONE | depth_score ≈ judge 分 (r=0.861), 非结构度量 |

## 命名与存放约定（防混用）

- **module** = 存放模块（脚本+数据+报告），如 `modules/B-pipeline-ablation/`
- **实验** = 一次有假设、有对照、有交付物的研究活动，ID 形如 T53b / T-PR-17 / T-JUDGE-1 / K7
- 实验的**执行脚本**在 `experiments/stage-ablation/`，**数据/报告**在 `modules/B-pipeline-ablation/`
- 各 decomp 子项编号 = 任务首字母分支编号（J1-J6 / F1-F5 / A-E），非全局；跨任务引用带全名

## 规划笔记位置（细节入口）

| 文件 | 内容 |
|---|---|
| `experiments/stage-ablation/tasks/decomposition-research-agi-budget.md` | 主线 goal 分解 (A-E) + K1-K8 映射 + 执行记录 + arena T-PR-16 结果 |
| `experiments/stage-ablation/tasks/design-research-agi-budget.md` | 设计文档 (K1-K8 改动项表 + 正交性自检) |
| `experiments/stage-ablation/tasks/T-PR-17-decomp.md` | 路径依赖实验 (F1-F5, 4 臂定义, null control) |
| `modules/B-pipeline-ablation/research/T-JUDGE-1-decomp.md` | 客观 judge (J1-J6, 阈值/磁体/dual-track) |
| `modules/IDEA-INDEX.md` | 统一 idea 池 (#1-50) |
| `modules/B-pipeline-ablation/reports/t53b/anatomy-0.5184.md` | 0.5184 解剖报告 |

## 当前阻塞与下一步（11-24 20:59 更新）

1. **Q7 719 r2/r3 过夜跑中**（r1 已完成：719 节点/judge 0.6635/cov 0.3269，曲线 5 点 R²=0.988；r2 ETA ~22:20，r3 ~24:15）。watcher 自动 post-run（SHA 查重 + replication-check + 报告）。落地后：cov 轴 n=3 + Q7 三域 cov 对比（GPU 饱和/Q6/Q7 未饱和 → 域依赖性初判成立）决定是否落 workshop §4.3
2. **K7 主交付物已出**（k7-pareto-newjudge-20261124.md, commit 2133853d4）：cov 轴 ~300 节点饱和（池化 n=8），metacog 轴独立于预算（ρ≈0）——预算只控制覆盖度不控制元认知。719-r1 边际机制已分解（+0.079 = 新 L5 层，非均匀提质）
3. T-JUDGE-1 J4 兜底 102 条（等 vLLM 释放）
4. T-PR-17：设计已强化（滚雪球 4 约束并入 F2b, c3153c956；新颖性弱 conf≤0.55 → claim 收窄为 suffix-ablation 设计）；runner + checkpoint preflight + 冒烟已派 subagent（sa-0-07937e31）；正式 run 等 vLLM 释放
5. D 确认 Q9-agi 硬件边界 → gold 已交付 Q9-v1（37 节点）+ v2 方法论修复（lexicographic 目标/证据质量登记, 885debea5），Lead 双源 web-LLM 核验通过（d2-q9v1-lead-verify-20261124.json）
