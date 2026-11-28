#!/usr/bin/env python3
"""T8c-ReAnchor-A: 从 reanchor-taskcard.md 解析 37 个替换点并应用到 6 个目标文件。
用法: python3 apply_reanchor.py [--dry]
规则(任务卡「执行方式」): 行内对取首末反引号间内容, 还原 \\->\\, \\n->换行, \\`->`;
围栏块取围栏间原文; 每点断言命中数==1, 否则停下(禁止模糊匹配)。
特例(任务卡锚点指引, 见回执 thinking_log):
  5a: 任务卡注明"多处 import calc 只改第一处(模块顶部)"——文件 L15 是注释行含该词,
      故按行首锚定 ^import calc 定位 L36 真实 import(唯一行首匹配)。
  5d: 任务卡 old 行首多一个空格与实际不符(实际 f" 紧跟缩进), 按任务卡锚点
      "找到 ≈0.679" 用行首锚定 ^f"c_pass= 定位, 数值/精度/文案按任务卡 new 改。
"""
import re, sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
CARD = os.path.join(ROOT, 'tasks/think-trigger/exp-results/reanchor-taskcard.md')


def unescape(s):
    return re.sub(r'\\(.)', lambda m: {'n': '\n', '`': '`'}.get(m.group(1), m.group(1)), s)


def parse_card():
    lines = open(CARD, encoding='utf-8').read().split('\n')
    files, cur = [], None
    for ln in lines:
        m = re.match(r'^## 文件 \d+: ', ln)
        if m:
            cur = {'name': ln[m.end():].strip(), 'path': None, 'pts': []}
            files.append(cur)
            continue
        if cur is None:
            continue
        if ln.startswith('路径: '):
            cur['path'] = ln[len('路径: '):].strip()
            continue
        m = re.match(r'^### (\S+)\.', ln)
        if m:
            cur['pts'].append({'id': m.group(1), 'old': None, 'new': None})
            continue
        p = cur['pts'][-1] if cur['pts'] else None
        if p is None:
            continue
        mo = re.match(r'^old: `(.*)`$', ln)
        mn = re.match(r'^new: `(.*)`$', ln)
        if mo and p['old'] is None:
            p['old'] = unescape(mo.group(1)); continue
        if mn and p['new'] is None:
            p['new'] = unescape(mn.group(1)); continue
        if re.match(r'^old\b.*:$', ln) and p['old'] is None:
            p['kind'] = 'fence'; p['side'] = 'old'; p['infence'] = False; continue
        if re.match(r'^new\b.*:$', ln) and p['new'] is None:
            p['kind'] = 'fence'; p['side'] = 'new'; p['infence'] = False; continue
        if p.get('kind') == 'fence':
            if ln.strip().startswith('```'):
                if not p['infence']:
                    p['infence'] = True
                    p[p['side']] = ''
                else:
                    p['infence'] = False
                continue
            if p['infence']:
                p[p['side']] += ln + '\n'
    return files


def apply_point(txt, p):
    """返回 (new_txt, hits)。特例 5a/5d 走行首锚定正则。"""
    if p['id'] == '5a':
        pat = re.compile(r'^import calc.*$', re.M)
        hits = len(pat.findall(txt))
        return (pat.sub(lambda m: p['new'], txt, count=1), hits)
    if p['id'] == '5d':
        # 任务卡 old/new 在 f" 后都带一个幻影空格(两侧一致的转录假象), 实际行无此空格;
        # 按任务卡锚点"找到 ≈0.679"定位整行, 保留文件原有缩进与尾部 3 空格, 只改数值/精度。
        norm = p['new'].replace('f" ', 'f"', 1).rstrip('"') + '   "'
        pat = re.compile(r'^(\s*)f"c_pass=\{winner_c:[^\n]*$', re.M)
        hits = len(pat.findall(txt))
        return (pat.sub(lambda m: m.group(1) + norm, txt, count=1), hits)
    hits = txt.count(p['old'])
    return (txt.replace(p['old'], p['new'], 1), hits)


def main():
    dry = '--dry' in sys.argv
    files = parse_card()
    total = sum(len(f['pts']) for f in files)
    print(f'parsed {len(files)} files, {total} points')
    bad = []
    for f in files:
        path = os.path.join(ROOT, f['path'])
        txt = open(path, encoding='utf-8').read()
        for p in f['pts']:
            if p['old'] is None or p['new'] is None:
                bad.append((p['id'], 'PARSE_MISSING'))
                print(f"  {p['id']} PARSE_MISSING")
                continue
            txt, hits = apply_point(txt, p)
            print(f"  {p['id']} hits={hits}")
            if hits != 1:
                bad.append((p['id'], hits))
        if not dry:
            open(path, 'w', encoding='utf-8').write(txt)
            print(f"wrote {f['path']}")
    if bad:
        print('MISMATCH:', bad)
        sys.exit(2)
    print('ALL_POINTS_HIT' if dry else 'APPLIED_ALL')


if __name__ == '__main__':
    main()
