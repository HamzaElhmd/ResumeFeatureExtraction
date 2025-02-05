from transformers import pipeline, XLMRobertaConfig, XLMRobertaForTokenClassification, AutoTokenizer

def setup():
    # Initialize the NER pipeline with a pre-trained model
    roberta_ner = pipeline('ner', model='xlm-roberta-large-finetuned-conll03-english', aggregation_strategy='simple')

    # Load the configuration and model for text classification
    distilbert_model = XLMRobertaForTokenClassification.from_pretrained("model")

    # Load the tokenizer for DistilBERT
    distilbert_tokenizer = AutoTokenizer.from_pretrained("tokenizer")

    # Create a text classification pipeline
    distilbert_tg = pipeline("ner", model=distilbert_model, tokenizer=distilbert_tokenizer, aggregation_strategy='simple')

    return roberta_ner, distilbert_tg
