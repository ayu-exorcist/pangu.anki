from .pangu import spacing_text


def _prepare_qa_text(qa_text):
    space_qa_text = spacing_text(qa_text)
    return space_qa_text


def auto_space(qa_text, card, *args):
    qa_text = _prepare_qa_text(qa_text)
    return qa_text


def once_space(func):
    def get_space_qa(self, *args, **kwargs):
        _qa = func(self, *args, **kwargs)
        if hasattr(self, "_qa") and self._qa is not None:
            _qa = {key: _prepare_qa_text(info) for key, info in _qa.items() if isinstance(info, str)}
            self._qa = _qa
        return self._qa
    return get_space_qa
