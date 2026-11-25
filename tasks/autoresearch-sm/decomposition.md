# autoresearch 闭环 — 分解树 + 任务表
# origin: ai · 2026-11-25 · 触发: D "经常陷入局部，也没成熟批判和工作流程"（S43）
# 方向修正 2026-11-25: D "先试试现成的吧，本地跑研究还没满意闭环" → 先试 ARIS 现成的；自建 MVP 降级备选
# 路径决策 2026-11-25: 侦察确认 ARIS 是 Claude Code 插件（非独立程序）→ 路径 C（抽 4 脚本+6 prompt 接 pfb/ralph）

## 终点（不动）
autoresearch 跑出满意闭环（治三个病：陷入局部 / 无常设批判 / claim 失效不传播）

## 分解树（路径 C：抽 ARIS 件接入现有流程）
ARIS 件接入
├── C1 脚本移植：4 个 .py（run_state/iteration_log/review_gate/watchdog）+ 依赖 → pfb/tools/aris/，适配 model_family（加 qwen 族）
├── C2 Prompt 提取：6 个批判 skill 的 材料黑白名单+prompt 模板+verdict 映射表 → pfb/tools/aris/prompts/
├── C3 试跑：idea53 最小闭环（27b 执行 + iteration_log 计数 + arena 跨族验收 + kill-argument 批判）
└── C4 验收：vs 三个病（打转轮数 / 批判拦截 / claim 失效）
备选
└── B1 自建认知层 MVP（SM-PROPOSAL.md，commit 43c3897a4）—— ARIS 件接入不行再上
升级（C 跑顺后）
└── U1 直装 Claude Code 跑完整 ARIS 做对照（需 D 确认订阅）

## 任务表
| 任务 | 内容 | 执行者 | 状态 | 验收 |
|---|---|---|---|---|
| R1 | ARIS 运行方式侦察 | sub | 完成(deleg_c8dd2b41) | scratch/aris-run-feasibility-20261125.md |
| A | ARIS 4 工具+2 批判 skill 机制提取 | sub | 完成(deleg_ea67ecf4) | scratch/aris-mechanism-detail-20261125.md |
| C1 | 4 脚本 copy+model_family 适配+import 验证 | sub | 派发中(deleg_97a2d654) | pfb/tools/aris/ 文件存在 + import 不报错 |
| C2 | 6 批判 prompt 提取→任务书模板 | sub | 与 C1 同 sub | 6 个模板落盘 + 各含黑白名单+映射表 |
| C3a | idea53 数字复算+状态机驱动（executor 半） | sub | 派发中 | TRIAL-RECEIPT.md + iteration_log jsonl + acceptance-request.md |
| C3b | arena 跨族验收 + kill-argument 批判（验收半） | Lead | 待 C3a | accept() 落库 + 批判 verdict（代码算） |
| C4 | 验收 vs 三个病 | Lead | 待 C3 | 三病各一个可测数字 |
| B1 | 自建 MVP（备选） | 待定 | 阻塞: C 试完 | 见 SM-PROPOSAL §5 |
| U1 | 直装 Claude Code 对照 | 待定 | 阻塞: C 跑顺+D 确认订阅 | — |

## 正交性
C1=脚本层（引擎无关 .py），C2=prompt 层（批判协议），C3=集成试跑，C4=验收。C1/C2 同源合一个 sub，C3 依赖 C1+C2。

## 在途 / 空缺
- C1+C2 sub 在途（deleg_97a2d654，6/6 prompt + 7 .py 已落盘，收尾中）
- C3a 试跑 sub 本轮派发（含稳定性检查，防与 C1+C2 写冲突）
- D 是否有 Claude 订阅未知（只影响 U1 对照，不影响 C）
- idea53 的 venue 轮 arena 报告仍未回（不阻塞 C 路径）
