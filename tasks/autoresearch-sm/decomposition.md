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
| C1 | 4 脚本 copy+model_family 适配+import 验证 | sub | 完成(deleg_97a2d654, 70376e4bd) | pfb/tools/aris/ 6 .py + import OK + 跨族检查 OK |
| C2 | 6 批判 prompt 提取→任务书模板 | sub | 完成(同 C1) | 6 模板落盘 prompts/ + 黑白名单+映射表 |
| C3a | idea53 数字复算+状态机驱动（executor 半） | sub | 完成(deleg_dfb37a94, 6ac87dafc→2b545def8) | TRIAL-RECEIPT.md + 7 条 finding + acceptance-request.md；重算 ALL_MATCH |
| C3b | 验收半（accept 落库） | Lead | 完成(f0bd0f636) | 两 phase accepted (deterministic:lead-verify)；run→COMPLETE |
| C4 | 验收 vs 三个病 | Lead | 下一步 | 三病各一个可测数字 |
| B1 | 自建 MVP（备选） | 待定 | 阻塞: C 试完 | 见 SM-PROPOSAL §5 |
| U1 | 直装 Claude Code 对照 | 待定 | 阻塞: C 跑顺+D 确认订阅 | — |

## 正交性
C1=脚本层（引擎无关 .py），C2=prompt 层（批判协议），C3=集成试跑，C4=验收。C1/C2 同源合一个 sub，C3 依赖 C1+C2。

## 在途 / 空缺
- ~~C1+C2 sub 在途~~ 完成 (70376e4bd)
- ~~C3a 试跑~~ 完成 (deleg_dfb37a94, 6ac87dafc→2b545def8)；第一次派发 502 挂 (deleg_43186cdd)，第二次带饱和度预检通过
- ~~C3b 验收~~ 完成 (f0bd0f636)：**验收通道偏离任务书**——原计划 arena 跨族 LLM，实际用 deterministic 通道（纯闭式计算 claim，确定性核验更强且合规；run_state.py 内置该通道，C3b-verdict.md 记录了理由）
- C4 待做：三病各一个可测数字（打转轮数=iteration_log stale 轨迹；批判拦截=kill-argument 未跑→缺口；claim 失效传播=未测→缺口）
- kill-argument 批判本轮未跑（C3b 范围收窄为 accept 落库）——C4 时补，或并入下一个真实任务
- D 是否有 Claude 订阅未知（只影响 U1 对照）
