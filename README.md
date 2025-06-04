# Dynamic Web Base URL

This module makes `web.base.url` dynamic based on the incoming HTTP request.  
Useful when you serve multiple domains on one Odoo instance (e.g. `armlab.com`, `mijn.bronsgroen.be`, `odoo.bronsgroen.be`).

## Features

- Emails and portal links use the correct domain
- No more hardcoded redirection to the wrong host
- Lightweight and safe fallback behavior

## Installation

Clone or copy the module to your Odoo addons folder:

```bash
git clone https://github.com/wooter/web_base_url_dynamic.git
```

Then:
1. Restart Odoo
2. Activate Developer Mode
3. Update Apps List
4. Search for and install **Dynamic Web Base URL**

## Compatibility

- Odoo 17 (tested)
- Works with Odoo Community & Enterprise
