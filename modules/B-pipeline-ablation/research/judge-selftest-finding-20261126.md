# origin: ai
# judge selftest 红灯发现（2026-11-26，验收 bonus 改动时暴露）

## 现象
`judge_pipeline_v0.py --selftest` 报 4 FAIL，exit 1（守卫本身工作正常）：
- raw_outputs_t8b.arm_a[1]: verdict=A1 (期望 A2)
- raw_outputs_t8b.arm_a[2]: verdict=A1 (期望 A3)
- raw_outputs_t8b.arm_b[0]: verdict=A1 (期望 A2)
- raw_outputs_t8b.arm_b[1]: verdict=A1 (期望 A2)

## 定性：存量问题，非 bonus 改动引入
- 改动前版本（b2a1c0736^）跑同一 selftest → **完全相同的 4 FAIL、相同样本**。
- cov 那条（S5 cov=0.3889）两边都 PASS，bonus 纯旁路未碰 cov 分母（坐实）。

## 待判断（方向活，未擅自改）
SELFTEST_EXP 里 T8b 的期望 verdict（A2/A3）来自 J1 基准；当前 compute_correctness 对这 4 样本产出 A1。
两种可能，需定夺修哪边：
1. 期望值过期（J1 之后 correctness 口径合法演进）→ 改 SELFTEST_EXP 期望为 A1；
2. correctness_layer 回归（本该 A2/A3 却判 A1）→ 查 correctness_layer_v0 的 A1/A2/A3 判别逻辑。
判据：翻 J1 验收记录里这 4 样本当时的 verdict 依据；若当时判 A2/A3 且有理由 → 是回归；若口径本就 A1 → 期望过期。
在定夺前，selftest 永久红灯会被忽略（守卫失效风险），但 cov 主口径可信。
