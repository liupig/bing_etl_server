import difflib
import json
from server.json_sort_server.json_sort.json_sort_process import json_sort


def comparison_process(main, sub):
    try:
        main_text = json.dumps(json_sort(json.loads(main)), indent=4, ensure_ascii=False).splitlines()
        sub_text = json.dumps(json_sort(json.loads(sub)), indent=4, ensure_ascii=False).splitlines()
        html = difflib.HtmlDiff().make_file(main_text, sub_text).encode()
        return html
    except:
        main_text = main.splitlines()
        sub_text = sub.splitlines()
        return difflib.HtmlDiff().make_file(main_text, sub_text).encode()
