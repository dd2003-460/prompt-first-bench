# autoresearch 状态机 — 分解树 + 任务表
# origin: ai · 2026-11-25 · 触发: D 2026-11-25 "经常陷入局部，也没有成熟的批判和工作流程"（信号 S43）
# 动机案例: idea53 审计（撞车 5 轮查旧 claim 域 / 被反驳 claim 走到写作 / toy model 缺陷进稿）

## 分解树
```
SM 状态机设计
├── A. ARIS 机制精确提取（iteration_log/run_state/review_gate/watchdog + 2 个批判 skill）→ 落盘 scratch
├── B. 提案草案 v0.1（两层状态 + 3 特殊转移 + 偷/不偷清单 + MVP 验收）→ SM-PROPOSAL.md
└── C. MVP 实现（打转检测 + claim 失效传播 2 工具 + 状态文件 schema）→ 待 D 批准立项
```

## 正交性核对
- A=提取外部事实（ARIS 代码语义），B=内部设计判断，C=实现。互不重叠。
- A 是 B 的输入（偷清单需验证语义）；B 是 C 的任务书。

## 任务表
| 任务 | 内容 | 执行者 | 状态 | 验收 |
|---|---|---|---|---|
| A | 提取 ARIS 4 工具 + kill-argument/paper-claim-audit 精确语义，file:line 引证 | sub | 派发中 | scratch/aris-mechanism-detail-20261125.md 落盘 |
| B | SM-PROPOSAL.md 草案 v0.1（偷清单标[待核验]，A 回来后 patch） | Lead | 本回合 | 文件存在 + 3 转移有量化条件 |
| C | MVP（2 工具 + schema） | 待定 | 阻塞: D 批准 | 下个真实任务跑通，打转轮数/事后拦截数可测 |

## 空缺清单
- venue 轮 arena 报告未回（idea53 侧，不阻塞 SM 设计）
- D 未拍板立项（C 的前置）
