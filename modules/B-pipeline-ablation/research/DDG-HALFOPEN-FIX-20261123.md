# origin: ai — DDG 熔断 half-open 探针修复 (待 r8 落地后 apply)

## 问题 (root cause 2026-11-23)

research_hook.py `_ddg_search` 熔断器 (line 354-408): `_ddg_fail_streak >= 2` → 进程内**永久**跳过 DDG。
DDG lite TLS 封锁是**间歇**的 (r4-r8 交替 FLAG: 100-r4 活 9min / 100-r5 活 3min / r7 全程死 0 SITE-WL),
但 run 持续 30-60min, 熔断一旦打开, run 中途 DDG 恢复也没人再探 → 剩余 20-50min 检索全空。

## 修复: half-open 探针

- 熔断打开时记 `_ddg_half_open_at = now + 600s`
- 熔断中: 未到探针时间 → 快跳 (return []); 到探针时间 → 放行一次真实探测
- 探针成功 → `[DDG-RECOVERED]` + streak=0 关闸; 失败 → streak+1, 下次探针再推迟 600s
- 进程内变量 (每 run 独立进程, 跨 run 天然重置, 不变)

## 验证 (mock 状态机 6 步, /tmp/rh_test.py 副本, 2026-11-23)

1. 连败2 → streak=2 熔断 ✓
2. 未到探针 → 快跳 ✓
3. 探针放行 + DDG 恢复 → results>0, streak=0 关闸, [DDG-RECOVERED] ✓
4. 关闸后正常 ✓
5. 再连败 → 重新熔断 ✓
6. 探针放行但 DDG 仍死 → streak+1, 下次探针推迟 598s ✓

注意: 首次 mock 测试 step 3 失败是 mock HTML 格式错 (单引号/属性序不匹配 parser regex), 非状态机问题; 正确格式重测 6/6 过。

## Apply (r8 落地后)

```bash
cd pfb && git apply modules/B-pipeline-ablation/research/ddg-halfopen-patch-20261123.patch
# 回归: python3 -c "import research_hook" 语法 + 上面 mock 测试
```

约束: 必须在 rep-scan 队列结束后动 (channel-mixing within budget tier 红线)。
