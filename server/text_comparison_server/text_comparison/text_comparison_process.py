import json
from server.json_sort_server.json_sort.json_sort_process import json_sort
from server.text_comparison_server.text_comparison.difflib import HtmlDiff


def comparison_process(main, sub, flag):
    try:
        if flag:
            if "'" in main and '"' not in main:
                main = main.replace("'", '"')
            elif "'" in main and '"' in main:
                if main.index('"', 1) > main.index("'", 1) and "_import_" not in main and "_from_" not in main:
                    main = json.dumps(eval(main))
            if "'" in sub and '"' not in sub:
                sub = sub.replace("'", '"')
            elif "'" in sub and '"' in sub:
                if sub.index('"', 1) > sub.index("'", 1) and "_import_" not in sub and "_from_" not in sub:
                    sub = json.dumps(eval(sub))
            main_text = json.dumps(json_sort(json.loads(main)), indent=4, ensure_ascii=False).splitlines()
            sub_text = json.dumps(json_sort(json.loads(sub)), indent=4, ensure_ascii=False).splitlines()
            html = HtmlDiff().make_file(main_text, sub_text).encode()
            return html
        else:
            main_text = main.splitlines()
            sub_text = sub.splitlines()
            return HtmlDiff().make_file(main_text, sub_text).encode()
    except:
        main_text = main.splitlines()
        sub_text = sub.splitlines()
        return HtmlDiff().make_file(main_text, sub_text).encode()
