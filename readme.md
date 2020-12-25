# <u>Dictionary</u>

## Features :
- Closest word match
- Show more than one meaning
- > More features coming soon

## Libraries used :

```python
import json
import difflib
from difflib import get_close_matches 
```

## How to get close matches ?
```python
file = json.load(open("data.json","r"))
close_match = get_close_matches(word,file.keys())
```
<hr>

- Youtube -> [YOUTUBE][youtube]
- Linkedin -> [Linkedin][linkd]
- Github -> [GITHUB][github]
- Github Site -> [Click here][site]
- Personal Site -> [Click here][site2]
  
[youtube]:https://www.youtube.com
[linkd]:https://www.linkedin.com/in/sahil-gupta-2905421a5/
[github]:https://github.com/Sahil1709
[site]:https://sahil1709.github.io
[site2]:https://sahilgupta.tk