# C3a Trial Receipt — idea53 核心数字复算 (executor 半)

# origin: ai
run: idea53-repro · executor qwen3.8-27b · 2026-11-25 · ARIS run_state + iteration_log

## 重算数字表 (4 平台 × 40k workload, seed=42, 同原脚本采样)

| 指标 | 重算值 | 预期 | 判定 | 证据 |
|---|---|---|---|---|
| flip rate (min-max) | 0.4344–0.5627 | 43–56% | match | independent_recompute.json per_hardware.flip |
| mean_time_shift (min-max) | 0.1655–0.2307 | 0.17–0.23 | match | 同上 .shift (T5000 0.1655 略低于 0.17 下沿, 原 JSON 亦 0.1655, 属预期区间边缘 [不确定: 预期下沿 0.17 vs 实测 0.1655]) |
| H(D\|S) (min-max) | 0.7128–0.7667 | 0.71–0.77 | match | independent_recompute.json per_hardware.H_DS |
| flat-rate 对照 flip | 0.0 | 精确=0 | match | verify_results.json c (9/9 configs) |
| flat-rate 对照 H(D\|S) | 0.0 | ≈0 | match | 同上 |
| 24 置换不变性 | 各平台 flip/shift range 窄 (如 5090 flip [0.5251,0.5304]) | 24 置换一致 | match | independent_recompute.json perm |

注: 重算值与原结果 JSON (idea53-theory-{flip,mi,reorder}.json) 逐项一致 (ALL_MATCH, 容差 1e-3)。
shift 下沿 0.1655 (T5000) 低于任务预期下沿 0.17 —— 与原 JSON 一致, 但严格对照任务预期区间属边缘 [不确定]。

## 状态机使用记录

命令序列 (run_state.py / iteration_log.py):
1. start root=trial run_id=idea53-repro --phases REPRODUCE,VERIFY --executor qwen3.8-27b
2. iteration_log note INIT 1 (init)
3. set REPRODUCE running
4. iteration_log note REPRODUCE 3 / 2 / 1 (flip-shift-H / flat+perm / independent ALL_MATCH)
5. set REPRODUCE done --artifact independent_recompute.json
6. set VERIFY running
7. iteration_log note VERIFY 1 / 1 / 1 (prereg时序 / T5000手算 / flat=0稳健)
8. set VERIFY done --artifact verify_results.json

成功次数: start×1, set_status×4 (REPRODUCE running/done, VERIFY running/done), log_finding×7 (INIT 1 + REPRODUCE 3 + VERIFY 3)
stale 轨迹: 0,0,0,0,0,0,0,0 — 峰值 0 (每轮均有新 finding, 无 zero-finding 轮)
是否触发 pivot: 否 (stale 从未 ≥2, PIVOT_STRUCTURAL_AT=2 / ESCALATE_HUMAN_AT=4 均未触及)
终态: REPRODUCE=done(unaccepted), VERIFY=done(unaccepted), resume→REPRODUCE (第一个非 terminal, 待跨模型审计)
未调用 accept/mark-provisional — 验收留给 Lead 跨族。

## 已知局限
- 复算用同一 seed=42 同一采样 → 与原 JSON 必然一致, 只验证"计算正确", 不验证"采样代表性"。
- 独立重算是重写 surface/deep/H 逻辑交叉验证, 非换算法, 无法捕获"两套代码共享同一建模错误"。
- shift 下沿 0.1655 vs 预期 0.17: 边缘, 待验收方裁定是否算 match。
- 未重跑 LLM/judge 相关 (本 claim 为纯闭式计算, 无 LLM 依赖), 故 vLLM 饱和风险仅影响预检。
