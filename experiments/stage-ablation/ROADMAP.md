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
| K7 预算扫描 | 预算-质量 Pareto 什么形状? | RUNNING 13/15 | 曲线 + 拐点 (k7_pareto.py 已就绪) |
| T-JUDGE-1 | 怎么客观打分? | ACTIVE | embedding judge + 磁体检测 + LLM 兜底 (102 条待跑) |
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
| `tasks/decomposition-research-agi-budget.md` | 主线 goal 分解 (A-E) + K1-K8 映射 + 执行记录 + arena T-PR-16 结果 |
| `tasks/design-research-agi-budget.md` | 设计文档 (K1-K8 改动项表 + 正交性自检) |
| `tasks/T-PR-17-decomp.md` | 路径依赖实验 (F1-F5, 4 臂定义, null control) |
| `modules/B-pipeline-ablation/research/T-JUDGE-1-decomp.md` | 客观 judge (J1-J6, 阈值/磁体/dual-track) |
| `modules/IDEA-INDEX.md` | 统一 idea 池 (#1-50) |
| `modules/B-pipeline-ablation/reports/t53b/anatomy-0.5184.md` | 0.5184 解剖报告 |

## 当前阻塞与下一步

1. K7 719_r2 在跑 (~1-2h) → 完成后: k7_pareto 全量 15 run + 质量轴声明
2. K7 释放 vLLM → T-JUDGE-1 J4 兜底 102 条 (27b 二元裁决, ~15min)
3. K7 释放 vLLM → T-PR-17 执行 (monkey-patch, 不碰 s5_state_machine.py)
4. D 确认 Q9-agi 3 个 [待核验] (AGI 操作化/硬件边界/可靠性定义) → gold 扩树
