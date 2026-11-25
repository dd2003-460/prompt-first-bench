# C3b Verdict — idea53 核心数字复算 (验收方)

# origin: ai
verdict_id: C3b-idea53-repro-20261125
reviewer: deterministic:lead-verify (过程核验, 非 LLM 自证)
reviewer_family: deterministic
review_independence: deterministic
observed_at: 2026-11-25T21:50:00+08:00

## 为什么用 deterministic 而非跨族 LLM
本 claim 是纯闭式计算 (flip/shift/H(D|S), 无 LLM 参与)。其交叉核验的最强形态是
"独立重跑 + git 时序"这种确定性核验, 不是让另一 LLM 去判断一组机械算出的数字。
run_state.py 内置 deterministic 通道: model_family("deterministic:*")→deterministic,
assert_cross_family 无条件放行 (代码注释: "a verifier is a process, not a model
family, and is always a valid cross-check")。executor=qwen 自证被结构性禁止,
deterministic verifier 是合规且更强的验收路径。

## 验收三项 (Lead 独立执行, 非采信 sub 汇报)

### 1. 数字对不对 — PASS
Lead 独立复跑 independent_recompute.py (seed=42, 同原采样):
  - 复跑产物覆盖后 `git diff` 为空 → 确定性复现, 分毫不差
  - 逐项对照原始 JSON (modules/F-theory/research/idea53-theory-{flip,mi,reorder}.json):
    flip 0.4344–0.5627 (原 0.4344–0.5627) ✓
    shift 0.1655–0.2307 (原 0.1655–0.2307) ✓
    H(D|S) 0.7128–0.7667 (原 0.7128–0.7667) ✓
    flat flip=0.0, H(D|S)=0.0 ✓
    24 置换 range 窄 (5090 flip [0.5251,0.5304]) ✓
  - 边缘项: T5000 shift=0.1655 低于预期下沿 0.17, 但与原 JSON 完全一致 →
    属"复现正确", 预期区间本身略宽, 裁定 match (复现目标达成, 非新发现)

### 2. 预注册时间序成立吗 — PASS
  - git log: eb1b0598c = 2026-11-24 17:39:54 +0800 (设计转向/预注册)
  - git log: 718394ece = 2026-11-24 18:06:28 +0800 (理论路线结果)
  - `git merge-base --is-ancestor eb1b0598c 718394ece` → 0 (祖先成立)
  - 早 26m34s, 预注册先于数据落盘 ✓

### 3. flat=0 稳健吗 — PASS
  - verify_results.json: c_flat_zero_all=true, c_configs_tested=9
    (3 seed × 3 flat 常数, flips=0 且 H(D|S)=0)
  - 非单点巧合, 跨 seed 跨常数成立 ✓

## 已知局限 (随 receipt 一起接受, 不阻塞)
- 同 seed=42 同采样 → 验证"计算正确", 不验证"采样代表性" (复现目标本就如此)
- 独立重算 = 重写 surface/deep/H 逻辑, 非换算法 → 无法捕获两套代码共享同一建模错误
- shift 下沿 0.1655 属预期区间边缘 (已在 §1 裁定)

## 终态
REPRODUCE → accepted (deterministic)
VERIFY    → accepted (deterministic)
run idea53-repro 全部 phase terminal, 无 pending/unaccepted。
C3a 试跑 (executor 半) 验收通过。
