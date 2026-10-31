with open('ppl-mandiri.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'id="tab-' in line or 'class="ct-tab-pane' in line:
            print(f"{i+1}: {line.strip()}")

