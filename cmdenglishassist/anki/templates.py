BASE_TEMPLATE_STYLES = """
<style>
  table, td, th {
    border: 1px solid grey;
    border-collapse: collapse;
  }
  td, th {
    padding: 10px;
  }
  .main-container {
    font-size: 18px; 
    font-family: sans-serif; 
    text-align: left; 
    padding: 20px;
  }
  ul {
    list-style: none;
  }
  ul li::before {
    content: "- ";
    margin-left: -20px;
  }
  [class^="hi"] {
    padding: 4px 14px;
    border-radius: 3px;
  }
  .hi {
    background: aquamarine;
  }
  .hir {
    background: #ffa4a4;
  }
  .hiy {
    background: lightgoldenrodyellow;
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
    
