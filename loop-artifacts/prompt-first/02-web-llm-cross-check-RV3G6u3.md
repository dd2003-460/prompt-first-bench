# web-llm 交叉核对回执 — RV3G6-gmr-caliber-u3（2026-10-30）

> goal: U3 口径裁定（AUDIT L103/L166「gmr 6.4→8.6」归属）· 分支 ralph/rv3g6-gmr-caliber-u3
> 回执路径约定：per-goal 分文件（RV3B1-webllm-receipt-per-goal 前置执行；原路径 `02-web-llm-cross-check.md` 零 diff 不动）

## §0 · 运行状态

**工具故障（新登记，区别于既往「登录过期」）**：`ralph prompt-first web-llm` 无法启动——报 `[Errno 2] No such file or directory: '/Users/a1-6/Desktop/workspace/pfb/ralph-loop.md'`。该文件在本仓库工作树与 git 历史中均不存在（r122 前亦无）。即 ralph CLI 的项目入口文件缺失，web-llm 步骤本轮**未实际执行**（连 provider 调用都未发生）。

**处置**：本 goal 为纯仓库内数值溯源+文本修订，外部在线复核非必需（同 r122 erratum 口径：降级为仓库内双源机判比对——freeze doc §5 ↔ assert-gmr-recompute.py computed 列 ↔ G3 工件表格值三方对照）。web-llm 状态记 **unverified（工具故障，非登录问题）**，不阻塞。

**导出**：ralph-loop.md 缺失问题登记为新候选（见 04.5 导出节）——影响所有后续 goal 的强制 web-llm 步骤可执行性，优先级高于 RV3B1-webllm-receipt-per-goal（回执分文件是格式问题，本项是工具不可用问题）。

## §1 · 本 goal 的核验需求评估

U3 裁定的全部证据链在仓库内闭合：
- AUDIT L103/L166 引用值（6.4/8.6）↔ G3 F3b L48 表格值（6.4/8.6）逐字一致性 → grep 可机判
- 正确 global gmr 值（5.40→7.60）→ assert-gmr-recompute.py 从冻结 JSON 独立复算（不依赖任何文档文本）
- 两者差异的性质判定（口径误标 vs 数值错误）→ 由 G3 L48 表头口径名 + 计算协议决定，属文本证据

无一项需要外部来源。web-llm 即使可用，对本 goal 结论的边际贡献 ≈ 0（无外部事实待核）。