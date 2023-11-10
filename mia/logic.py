import spacy
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from .knowledge_base import knowledge_base
from .train_data import train_data

nlp = spacy.load("pt_core_news_sm")

# Extrair palavras dos dados de treino
X_train = [text for text, _ in train_data]
y_train = [intent for _, intent in train_data]

# Vectorizando dados com CountVectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)

# Treinador, ajuda a definir intenção
clf = LinearSVC()
clf.fit(X_train, y_train)

# Método para definir intenção (assunto)
def classify_intent(text):
    features = vectorizer.transform([text])
    intent = clf.predict(features)[0]
    return intent


# Função para gerar respostas com respostas dinamicas
def generate_response(intent):
    if intent in knowledge_base:
        responses = knowledge_base[intent]
        response = random.choice(responses)
        # Placeholders que substituem determinadas palavras nas respostas
        placeholders = {
        "{direction}": random.choice(["direita","esquerda"]),
        "{place}": random.choice(["Nova Iorque", "Chicago", "Paris", "Pernambuco", "Carpina", "Belford Roxo", "casa da sua mãe"]),
        "{cardinal}": random.choice(["norte","sul", "leste", "oeste"]),
        "{temperatura}": random.choice(["quente","frio","congelante","pelando","quente pra carai"]),
        "{clima}": random.choice(["nublado","chuvoso","ensolarado","limpo","quente pra carai"]),
        "{Research}": random.choice(["Pesquise","Procure informação", "Encontre", "Investigigue", "Examine", "Procure", "Colete informação", "Explore detalhes"]),
        "{research}": random.choice(["pesquise","procure informação", "encontre", "investigigue", "examine", "procure", "colete informação", "explore detalhes"]),
        "{researchInfinitivo}": random.choice(["pesquisar","procurar informação", "encontrar", "investigigar", "examinar", "procurar", "coletar informação", "explorar detalhes"]),
        "{Recommendation}": random.choice(["Eu sugiro", "Você pode considerar","Recomendo","Considere", "Que tal"]),
        "{recommendation}": random.choice(["eu sugiro", "você pode considerar","recomendo","considere", "que tal"]),
        "{location}": random.choice(["no centro", "por perto", "na sua area", "na casa de sua mãe"]),
        "{Affirmation}": random.choice(["Claro","Certamente", "Pode ser", "Tá bem"]),
        "{affirmation}": random.choice(["claro", "certamente","pode ser", "tá bem"]),
        "{time}": random.choice(["hoje", "amanhã", "pela tarde"]),
        "{number}": str(random.randint(1, 200)),
        "{numbersmall}": str(random.randint(1, 10)),
        "{numbersmal1}": str(random.randint(1, 10)),
        "{hours}": str(random.randint(1, 24)), 
        "{minutes}": str(random.randint(1, 59)), 
        "{adjective_good_male}": random.choice(["incrível", "ótimo", "bom","maravilhoso","fantástico","magnífico","excelente","supimpa","massa","legal"]),
        "{adjective_good_female}": random.choice(["incrível", "ótima", "boa","maravilhosa","fantástica","magnífica","excelente","supimpa","massa","legal"]),
        "{verbExplore}": random.choice(["explore", "descubra", "experiencie", "tente","desbravar"]),
        "{verbExploreInfinitivo}": random.choice(["explorar", "descobrir", "experienciar", "tentar","desbravar"]),
}
        # Substitui placeholders por variações para uma conversa mais dinamica
        for placeholder, value in placeholders.items():
            if value:
                response = response.replace(placeholder, value)
        return response
    else:
        return random.choice(["Eu não entendi o que você disse :/", "Pode frasear de novo sua pergunta?","Fala direito porra"])
    
# Função que lida com a conversa
def chatbot():
    print("Oi, meu nome é Mia, como posso lhe ajudar?")
    while True:
        user_input = input("> ")
        intent = classify_intent(user_input)
        response = generate_response(intent)
        print(response)
                  
if __name__ == "__main__":
    chatbot()
