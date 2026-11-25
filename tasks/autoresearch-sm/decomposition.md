# autoresearch 闭环 — 分解树 + 任务表
# origin: ai · 2026-11-25 · 触发: D "经常陷入局部，也没成熟批判和工作流程"（S43）
# 方向修正 2026-11-25: D "先试试现成的吧，本地跑研究还没满意闭环" → 先试 ARIS 现成的；自建 MVP 降级备选

## 终点（不动）
autoresearch 跑出满意闭环（治三个病：陷入局部 / 无常设批判 / claim 失效不传播）

## 分解树（当前方向：先试现成 ARIS）
ARIS 试用
├── R1 运行方式侦察：入口/依赖/模型要求/能否本地 27b 跑 → 3 接入路径 + 推荐
├── R2 选定试跑任务：idea53（三个病时间线完整，可直接验收）
├── R3 跑闭环：ARIS 端到端跑 idea53
└── R4 验收：vs 三个病（打转轮数 / 批判拦截 / claim 失效）+ 满意度
备选（ARIS 试完不行再上）
└── B1 自建认知层 MVP（SM-PROPOSAL.md，commit 43c3897a4）

## 任务表
| 任务 | 内容 | 执行者 | 状态 | 验收 |
|---|---|---|---|---|
| R1 | ARIS 运行方式侦察（入口/依赖/模型/接入路径） | sub | 派发中 | scratch 落盘 + 3 路径 + 推荐 |
| R2 | 试跑任务 = idea53 | Lead | 已定（待 R1 确认可跑） | 任务名 + 验收锚点 |
| R3 | ARIS 端到端跑 idea53 | sub/arena | 待 R1 | 闭环产物落盘 |
| R4 | 验收 vs 三个病 | Lead | 待 R3 | 三病各一个可测数字 |
| B1 | 自建 MVP（备选） | 待定 | 阻塞: ARIS 试完 | 见 SM-PROPOSAL §5 |
| A | ARIS 4 工具 + 2 批判 skill 代码级语义提取 | sub | 在途(deleg_ea67ecf4) | scratch/aris-mechanism-detail 落盘 |

## 正交性
R1=能不能试（硬前置）→ R2=试什么 → R3=试 → R4=验。B1=备选路径，不并行。A=供 R3/R4 参考的机制细节。

## 空缺 / 在途
- 机制提取 sub（deleg_ea67ecf4）在跑：ARIS 4 工具 + 2 批判 skill 代码级语义
- R1 侦察 sub 本轮派发（deleg_c8dd2b41）
