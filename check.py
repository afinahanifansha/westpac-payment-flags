from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
html = (root / "index.html").read_text()
assert '<html' in html and '<script>' in html
assert 'George wants you as his trusted person' in html
assert 'Maya · Boutique' in html and 'Sam · Paris' in html
assert 'Northbridge Electronics, Perth WA' in html
assert not re.search(r'>Call (Dad|Son|David)</button>', html)
assert 'Calling Dad' not in html and 'Calling David' not in html
assert 'Search contacts' not in html
assert 'No access to your phone contacts.' in html
assert 'Give his a call' not in html
assert 'Margaret' not in html
assert not re.search(r'<(?:script|link)[^>]+(?:src|href)=["\']https?://', html)
for path in ['README.md', 'docs/ARCHITECTURE.md', 'docs/SAFETY.md', 'docs/DEMO.md', 'docs/SUBMISSION.md']:
    assert (root / path).is_file(), path
print('PASS: standalone prototype, scenario copy, no personal call actions, and documentation.')
