BASE_TEMPLATE_STYLES = """
<style>
  .main-container {
    font-size: 24px; 
    font-family: sans-serif; 
    text-align: left; 
    padding: 20px;
  }
</style>
"""

HIGHLIGHT_TEMPLATE_STYLES = """
<style>
    mark {
        background: turquoise;
    }
</style>
"""

def to_base_template(value):
    template = f'<div class="main-container">{value}</div>'
    return f'{BASE_TEMPLATE_STYLES}{template}'

def to_base_highlight_template(value):
    template = f'<div class="main-container">{value}</div>'
    return f'{BASE_TEMPLATE_STYLES}{HIGHLIGHT_TEMPLATE_STYLES}{template}'
    
