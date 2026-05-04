import os


def ft_tqdm(lst: range) -> None:
    """
    Minimal tqdm-like progress generator for a range.
    Yields items from the range while printing a progress bar.
    """
    total = len(lst)
    for i, item in enumerate(lst, start=1):
        # calculate progress
        frac = i / total
        bar_length = 40
        filled = int(frac * bar_length)
        bar = '[' + '=' * filled + '>' * (1 if filled < bar_length else 0)
        + ' ' * (bar_length - filled - (1 if filled < bar_length else 0)) + ']'
        percent = f"{frac * 100:6.2f}%"

        # attempt to fit terminal width
        try:
            cols = os.get_terminal_size().columns
            out = f"{bar} {percent} {i}/{total}"
            if len(out) > cols:
                out = out[:cols-3] + '...'
        except Exception:
            out = f"{bar} {percent} {i}/{total}"

        print(out, end='\r', flush=True)
        yield item

    # final line
    print()
