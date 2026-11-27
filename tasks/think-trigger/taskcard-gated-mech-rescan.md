# origin: ai
# 任务卡: gated 臂 mech 重扫 (三要素判据, 复用 q9_mech_level_scan.py)
# 前置: gated 2 runs 落盘 (taskcard-relevance-gate-150.md S2 完成)
# 目的: 同判据 (LLM 三要素) 下对比 gated vs baseline 150 的 mech/spec/other 分布 — 这是门禁实验的主验收 (关键词粗测只是先行指标)

## 执行 (单命令, 脚本已参数化 commit 76b28a2b0)
```bash
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/B-pipeline-ablation
GATED=data/q9-budget-scan-gated
python3 research/q9_mech_level_scan.py "$PWD/$GATED" "$PWD/$GATED/mech-level-scan-gated-20261127.json"
```
(~300 节点, 8/批, 预计 ~15min; 失败重试 3 次内置)

## S0 (2026-11-27 22:5x Lead 授权): 修 judge 短键 bug 再跑
背景 (上一轮 sub 只读探针坐实): judge(qwen3.8-27b@8787) 间歇性丢弃 run-tag 前缀——同一批 attempt1 返回全键 'gated-r1:N18', attempt2/3 返回短键 'N18'; 脚本 L71 精确全键校验 → 短键整批 missing → 3 重试耗尽 FATAL。Lead 已模拟验证 gated 38 批短键碰撞=0 (两 run 的 N-id 在任一批内不重复)。
修法 (仅改 research/q9_mech_level_scan.py 的 missing 校验段, 用下面 12 行替换原 4 行): 精确全键优先; 短键 (冒号后 id) 仅当该短键在批内唯一时才接受 (防混批歧义):
```python
                obj = extract_json(llm_call(prompt))
                short_seen = {}
                for k, *_ in batch:
                    s = k.split(":")[1]
                    short_seen[s] = short_seen.get(s, 0) + 1
                resolved = {}
                for k, *_ in batch:
                    if k in obj and obj[k] in ("mech", "spec", "other"):
                        resolved[k] = obj[k]
                    else:
                        s = k.split(":")[1]
                        if s in obj and obj[s] in ("mech", "spec", "other") and short_seen[s] == 1:
                            resolved[k] = obj[s]
                missing = [k for k, *_ in batch if k not in resolved]
                if missing:
                    raise ValueError(f"missing/invalid: {missing}")
                for k, *_ in batch:
                    labels[k] = resolved[k]
```
修完先干跑 1 批验证 (确认短键能被接受), 再跑全量。此修复向后兼容 baseline (全键命中时短键分支不触发)。本 S0 覆盖下方边界"不改脚本"一条, 仅限该 12 行替换。

## 产出
1. `$GATED/mech-level-scan-gated-20261127.json` (脚本生成: counts_by_level / counts_by_run / samples / conclusion)
2. 对比表 (**sub 自己写一段 ≤30 行 Python** 算, 结果 append 进 gated JSON 的 `comparison_vs_baseline` 字段):
   - 读 gated JSON 的 counts_by_run (gated-r1/r2) 聚合 → gated 的 mech/spec/other 率
   - 读 baseline `data/q9-budget-scan/mech-level-scan-20261127.json` 的 counts_by_run, 取 150-r1/r2/r3 聚合 → baseline 同判据率
   - Δother = baseline_other − gated_other (主指标, 预期 >0); Δmech = gated_mech − baseline_mech (护栏, 预期 ≥−5pp)
3. 1 commit: `feat(research): gated 臂 mech 重扫 + baseline 150 同判据对比`

## 验收
- JSON 存在, counts_by_run 两 run total 之和 = gated 实际节点数
- comparison 字段含两组率 + Δ
- 汇报 1 行: `gated other=A% mech=B% vs baseline other=C% mech=D% (Δother=±E pp, Δmech=±F pp), json 路径, commit hash`

## 边界
- 不改 run json / 不改脚本 (若脚本报错, 如实汇报不自行修)
- 不碰 baseline 数据目录 (只读)
- judge 一致性: 沿用 baseline 扫描的 calibration 结论 (44%, judge 偏松 other→mech) — 两组同判官同偏置, 相对差有效, 绝对值不可信, 汇报时注明
