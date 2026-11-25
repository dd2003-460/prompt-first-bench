# C4 验收 — autoresearch 闭环试跑 (idea53-repro) 三病各一个可测数字
# origin: ai
run: idea53-repro · 状态机 .aris/runs/idea53-repro.json (两 phase accepted, 终态 COMPLETE)
finding 日志: .aris/runs/idea53-repro.iterations.jsonl (7 条)
executed_at: 2026-11-25 (C4) · executor: qwen3.8-27b subagent · 未联网, 未碰真实 run 状态 (sha256 前后一致, 见病③)

## 病① 陷入局部 (anti-local-optima)

**可测数字**: 7 轮 finding 记账, stale 峰值 0, pivot 未触发 (PIVOT_STRUCTURAL_AT=2 /
ESCALATE_HUMAN_AT=4 均未触及) — 每轮有新发现, 计数器行为正确。

**证据路径**:
- 逐条统计 .aris/runs/idea53-repro.iterations.jsonl (7 行, 用 python json 解析):
  - log_finding 次数 = 7 (INIT×1, REPRODUCE×3, VERIFY×3), new_findings 合计 10
  - stale_count 轨迹 = [0,0,0,0,0,0,0], 峰值 0, 零发现轮 = 0 轮
  - pivot 字段 = 7×"none"; 无 structural, 无 human escalate
- 阈值定义: pfb/tools/aris/iteration_log.py 行 42–43
  (PIVOT_STRUCTURAL_AT=2, ESCALATE_HUMAN_AT=4), pivot_for() 行 95–100
- TRIAL-RECEIPT.md 行 33–34 独立佐证: "stale 轨迹 0×8 峰值 0; 是否触发 pivot: 否"

**诚实边界**:
- 本试跑是顺畅任务 (每轮都有新 finding), 没有真正考验"打转时会不会被踢出去"。
- pivot 路径未被实际触发: 只能证明 stale 计数器正确递增 (0 轮零发现 → 恒 0 → 恒 none),
  **不能证明** 真出现连续零发现时会正确触发 structural pivot / human escalate。
- 要验证 pivot 触发, 需在受控副本里注入 ≥2 轮零 finding 再观测 pivot 字段 (本次未做,
  因任务书只要求统计真实日志; 该测试可作为 C5 候选)。

## 病② 无常设批判 (standing critique)

**可测数字**: kill-argument verdict=WARN, still_unresolved=1 点 (P_4 major),
其中 3/5 点已被现有证据化解 (answered_by_current_text), 1 点部分化解 (P_3 minor)。

**证据路径**:
- 完整双线程全文 + 映射表输入输出: c4/kill-argument-verdict.md (commit 95d3fbfc1)
- 协议: pfb/tools/aris/prompts/kill-argument.md (verdict 由映射表从逐点计数机械算出,
  不由任一线程自评 — 本文件只记录映射表命中行, 不自评)
- 逐点结果: P_1 同 seed 同义反复=answered (TRIAL-RECEIPT.md 行 39 自认局限) ·
  P_2 共享建模错误=answered (行 40 自认) · P_3 shift 下沿 0.1655<0.17=partially
  (minor, 验收方有意立场, C3b-verdict.md 行 29–30) · P_4 ID3/C4.5 定位缺失=still_unresolved
  (major, trial/ 全部 6 份材料无先例引用) · P_5 24 置换证据强度=answered
  (independent_recompute.json perm range 窄)
- 映射表命中: still_unresolved=1 @ major, 无 critical → 行 2 "WARN /
  unresolved_major_or_minor" (FAIL 行需 critical, 未命中)

**诚实边界**:
- 双线程由同一 subagent (qwen3.8-27b) 顺序撰写, 非两个独立模型会话 — 任务书明确允许
  (批判角色≠验收角色, C3b 验收方是 deterministic:lead-verify)。独立性弱于原文设计的
  "两次独立模型调用": 攻击线程与裁定线程共享同一底层模型, 裁定线程可能继承攻击线程
  的盲点 (例如 P_4 若攻击线程没想到, 裁定线程也大概率想不到)。
- 攻击备忘录按任务书提示构造 (ID3/C4.5 撞车/同 seed/shift 下沿/模型假设), 非纯盲攻 —
  这是"按协议做定向批判", 不是"零提示盲杀", 漏掉的任务书未提示的攻击轴不计入。
- verdict=WARN 的含义: 复现 claim 在限定范围内可防御, 但 1 个 major 定位缺陷挡住 PASS;
  不改变 C3b 已 accepted 的复现结论 (kill-argument 审的是 claim 文本的防御力, 不是
  复现数字的正确性)。

## 病③ claim 失效不传播 (invalidation propagation)

**可测数字**: 失效演示 2/2 符合预期 — 副本 resume→VERIFY (强制重审),
真实 run resume→COMPLETE (terminal 不被误重审)。

**证据路径** (机械演示, 全部在副本上做):
- a. 复制: `cp -r .aris/runs/ → c4/state-copy/.aris/runs/` (run_state.py 的 root 参数
  解析 `<root>/.aris/runs/<run_id>.json`, 故副本需含 .aris/ 层); 副本 sha256 复制后 =
  真实文件 sha256 = 369ca638993e9571642a5c112a92c7e2c92f6189664f668fcb9f7052fed4715c
- b. 副本上模拟 claim 被推翻: `run_state.py set c4/state-copy idea53-repro VERIFY done`
  (VERIFY 从 accepted 退回 done; REPRODUCE 保持 accepted)。`resume c4/state-copy`
  输出 = **VERIFY** (stderr 显示 status=done, 非 terminal) → 失效强制重新审查,
  不被 accepted 状态掩盖
- c. 反向: `resume . idea53-repro` (真实 run, 两 phase accepted) 输出 = **COMPLETE**
  → accepted 是 terminal, 不被误重审
- 真实 run 状态保护: 操作前 sha256 = 操作后 sha256 = 369ca638… (逐字节未变;
  resume 是纯读操作, set 只作用于副本)
- resume 语义依据: pfb/tools/aris/run_state.py 行 22–25 (resume 解析到第一个非
  terminal phase; done-but-not-accepted 是 resume 目标), TERMINAL_STATUSES 行 68

**诚实边界**:
- 演示的是"phase 状态退回 done 后 resume 会指向它"这一状态机行为, 即"失效信号
  (状态回退) 会传播到 resume 决策"。它**不**证明: ① 谁会在 claim 被推翻时真的把
  phase 退回去 (本演示是人工模拟, 无自动失效检测器); ② 下游已 accepted 的 phase
  (此处 REPRODUCE) 是否也需要连带重审 — 状态机只保证 resume 停在第一个非 terminal,
  不保证"失效传播到所有依赖 phase"。
- 副本操作用了 run_state.py 官方 CLI (set), 未手改 JSON; 真实文件字节零改动 (sha256 证明)。

## 汇总 (三病 × 可测数字)

| 病 | 可测数字 | 状态 |
|---|---|---|
| ① 陷入局部 | 7 轮 finding 记账, stale 峰值 0, pivot 未触发 (每轮有新发现, 正确) | 计数器正确; 触发路径未实测 |
| ② 无常设批判 | verdict=WARN, still_unresolved=1 (major), 3/5 点已化解 | 协议可跑通; 双线程同模型, 独立性受限 |
| ③ 失效不传播 | 副本 resume→VERIFY, 真实 resume→COMPLETE, 2/2 符合预期 | 状态机行为符合设计; 无自动失效检测器 |
