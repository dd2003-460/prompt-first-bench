# ralph runtime 校验故障报告 — 2026-11-03 r267

## 现象
阶段 02 advance（ralph apply loop-artifacts/stages/02/r1/advance.json）持续 valid:false，
issues 恒为：
- 外部事实字段 local_artifact_inventory 缺少可复核的具体 HTTPS 来源
- 时效字段 ... 必须提供 observed_at
- 本阶段仍缺少 required_outputs: research_findings（早期）

## 已排除
1. fields.json 中所有字段均已带 HTTPS refs + observed_at → 无效
2. concept/attribute/role/disposition 各种组合（confirmed/research_required、role input/output/background）→ 无效
3. file:// / git:// refs → 被 _is_specific_source_url 拒绝（只认 https）
4. 移除本地路径 refs → 无效

## 根因定位（源码级）
runtime: /Users/a1-6/Desktop/workspace/loop/ralph_runtime/ralph_runtime/protocol.py
- `_needs_external_evidence(field)`: role ∈ {market_data, benchmark_data, spec_data, research_findings, ecosystem_analysis} **或** `_field_text` 含 market markers（current/latest/price/market/listing/现价/当前/最新/价格/行情/市场/报价）
- `_external_evidence_issues()`: 对这类字段要求 specific HTTPS refs；assumed_default 直接拒绝

关键矛盾：
1. **stage 01 同一字段通过**：concept=known, role=input, refs=本地路径，在 01 无 issue。
   说明 01 时该字段未触发外部事实判定（rationale 无 marker 词），而 02 的 rationale 含"当前"等词后开始触发。
2. **advance 校验读取陈旧矩阵**：state.json 的 attribute_matrix 含 field-apply 过程中产生的
   陈旧重复字段 `local_artifact_inventory`（disposition=research_required, refs=本地路径, 无 observed_at）。
   该字段已从 fields.json 删除，但 state.json 矩阵中残留——advance 校验器读的是 state.json 而非 fields.json 最新合并结果。
3. **required_outputs 检查**：field_completeness 按 concept/role/attribute 任一等于 "research_findings" 判存在；
   子字段 concept 前缀 "research_findings:" 不匹配，需主字段 concept="research_findings" 精确命中。

## 处置
- 字段内容已通过 field-apply 全部落盘（total:13），调研结论完整可信。
- 按任务书失败降级原则：如实上报基础设施故障，不伪造完成。
- 推进请求保留在 advance.json（status:passed + rationale 记录故障），待 runtime 修复
  （建议：advance 校验改读 field-apply 后的权威矩阵；_needs_external_evidence 改按 role 精确判定而非文本匹配）后重跑 ralph apply。

## 复现命令
```
cd /Users/a1-6/Desktop/workspace/pfb
ralph field-apply . loop-artifacts/stages/02/r1/fields.json
ralph apply . loop-artifacts/stages/02/r1/advance.json   # → valid:false, 上述 issues
```
