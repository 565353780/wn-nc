from wn_nc.Config.width import PRESET_WIDTHS

def getWidthRange(width_tag: str) -> list:
    if width_tag not in PRESET_WIDTHS.keys():
        print('[ERROR][width::getWidthRange]')
        print('\t width tag not valid! will return default range!')
        print('\t width_tag:', width_tag)
        print('\t valid width tags are:')
        print('\t', list(PRESET_WIDTHS.keys()))

        return PRESET_WIDTHS['l0']

    return PRESET_WIDTHS[width_tag]
