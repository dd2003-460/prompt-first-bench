#!/usr/bin/env python3
"""补充46 固化: (c) repair 闭环事件级 dry-run

draft §4.1 承重数字来源:
  - 全局 3.7% (342/9196), no_source 4.9% (106/2184),
    value_mismatch 1.7% (8/479), other 3.5% (228/6533)
  - 节点级 6.0% (282/4698)

方法 (与 ad-hoc 分析一致, 口径固定):
  失败模式分类用 run json 的 rework_events.reason (rework 前的 evidence,
  比节点最终 evidence 准——后者被 rework 覆盖)。
  fixed = 节点最终 status == 'verified'。
  数据源: checkpoints/archive 全量 (83-run corpus + idea2 + rep-scan, 去重按 run 文件)。

scope: archive 全量 run json (runs-s5-sm-*.json, 排除 synth)。
"""
import json, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
ARCH = os.path.join(ROOT, 'experiments', 'stage-ablation', 'checkpoints', 'archive')

# 失败模式正则 (对齐 ad-hoc 口径, 基于 reason 实际中文文本):
#   value_mismatch: 来源存在但与 claim 矛盾/不一致 (版本不匹配/数值不符/虚构)
#   no_source:      检索失败 / 来源未提供该值 / 无法验证
#   其余: other (含空 reason)
# 顺序: value_mismatch 先 (更具体的矛盾信号), 再 no_source
RE_VALUE_MISMATCH = re.compile(
    r'不一致|不匹配|矛盾|虚构|版本不|数值.{0,6}不符|量级|mismatch|contradict', re.I)
RE_NO_SOURCE = re.compile(
    r'检索失败|no\s*source|未提供|无法验证|无可用来源|无法从.{0,20}推导|缺乏.{0,12}(来源|上下文)|no\s*retriev', re.I)
RE_LLM_ERROR = re.compile(r'llm.*error|timeout|API.*error', re.I)


def classify(reason):
    if not reason:
        return 'other'
    if RE_VALUE_MISMATCH.search(reason):
        return 'value_mismatch'
    if RE_NO_SOURCE.search(reason):
        return 'no_source'
    if RE_LLM_ERROR.search(reason):
        return 'llm_error'
    return 'other'


def main():
    run_files = set()
    for pat in ('sm-gpu-*', 'budget-*', 'sm-nat-*', 'sm-soc-*', 'idea2-*', 'repscan-*', 'rep-*'):
        run_files.update(glob.glob(os.path.join(ARCH, pat, 'runs-s5-sm-*.json')))
    run_files = {f for f in run_files if 'synth' not in os.path.basename(f)}
    print(f"run jsons: {len(run_files)}")

    # 节点最终 status: (file, id) → verified?  (node id 跨 run 重复: 都是 N1/N2/..., 必须带 file)
    node_status = {}
    for f in run_files:
        try:
            rj = json.load(open(f))
        except Exception:
            continue
        for n in rj.get('nodes', []):
            nid = n.get('id')
            if nid:
                node_status[(f, nid)] = (n.get('status') == 'verified')

    # 事件级
    ev = {}  # mode → [attempts, fixed]
    total_ev = [0, 0]
    # 节点级
    rework_nodes = set()
    rework_fixed = 0
    for f in run_files:
        try:
            rj = json.load(open(f))
        except Exception:
            continue
        for evn in rj.get('rework_events', []):
            mode = classify(evn.get('reason', ''))
            nid = evn.get('node_id')
            fixed = node_status.get((f, nid), False)
            ev.setdefault(mode, [0, 0])
            ev[mode][0] += 1
            ev[mode][1] += 1 if fixed else 0
            total_ev[0] += 1
            total_ev[1] += 1 if fixed else 0
        for n in rj.get('nodes', []):
            try:
                rc = int(n.get('rework_count', 0) or 0)
            except (TypeError, ValueError):
                rc = 0
            if rc > 0:
                nid = n.get('id')
                rework_nodes.add((f, nid))
                if n.get('status') == 'verified':
                    rework_fixed += 1

    print("\n=== 事件级 (rework_events.reason, rework 前 evidence) ===")
    for mode in ('no_source', 'value_mismatch', 'llm_error', 'other'):
        if mode in ev:
            a, fx = ev[mode]
            print(f"  {mode:16s} {fx:5d}/{a:5d} = {fx/a*100:5.1f}%")
    print(f"  {'GLOBAL':16s} {total_ev[1]:5d}/{total_ev[0]:5d} = {total_ev[1]/total_ev[0]*100:5.1f}%")

    print("\n=== 节点级 (rework_count>0, 最终 status) ===")
    print(f"  {rework_fixed}/{len(rework_nodes)} = {rework_fixed/len(rework_nodes)*100:.1f}%")


if __name__ == '__main__':
    main()
