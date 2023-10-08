from summarizer import Summarizer


def return_summary(content):
    model = Summarizer()
    summary_dict = model(content)
    return summary_dict
