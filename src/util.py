def loop_replace_str(text_str="", replacements=[""]):
    """Does str.replace() for a list of strings.
    Args:
        text_str (str): text to remove from
        replacements (list, optional): list of strings to remove. Defaults to [""].
    Returns:
        string: text_str without the strings in replacements
    """

    if replacements != [""]:
        for i in replacements:
            text_str = text_str.replace(i, "")
    return text_str.strip()


def loop_replace_li(text_str_list=[], replacements=[""]):
    """Does str.replace() for a list of strings on a list of strings
    Args:
        text_str (li of str): text to remove from
        replacements (list, optional): list of strings to remove. Defaults to [""].
    Returns:
        string_li: text_str without the strings in replacements
    """
    new_li = []
    if replacements != [""]:
        for text_str in text_str_list:
            txt = " ".join(text_str.split())
            for ea in replacements:
                txt = txt.replace(ea, "")
            new_li.append(txt.strip())
    return new_li
