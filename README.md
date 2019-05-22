# ConvertMD  
A very simple converter from .md to .txt  

*Usage:*  
`convmd.py <source> <destination>`  
`<source>.txt` is used if `<destination>` is ommited.  

*Features:*  
- Remove '#&nbsp; ', '##&nbsp; ', '###&nbsp; ' and add '------' underneath; also blank lines before and after if needed.  
- Lone '#'s to blank line.  
- Remove all '*...*' formatting.  
- '- - ' and '- - - ' to '&nbsp; &nbsp; - ' and '&nbsp; &nbsp; &nbsp; &nbsp; - '  
- Option (commented out) to keep indent after `- `  
- '>' to '->&nbsp; '  
- Backtick to single quote
- Fence code between '~' adding blank line before and after if needed.  
- Strip image tags '![#...'  
- Remove '[]' from link Names (keep the links between '()')  
- Do not allow more than one consecutive blank line.  
