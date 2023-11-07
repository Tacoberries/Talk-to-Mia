import spacy
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC

nlp = spacy.load("pt_core_news_sm")

train_data = [
    # Sobre Mia
    ("O que você pode fazer?", "mia_capacidade"),
    ("Como você funciona?", "mia_capacidade"),
    ("Sobre quais assuntos você consegue responder?", "mia_assuntos"),  
    ("Quem é você?", "mia_apresentação"),
    ("O que é você?", "mia_apresentação"),
    ("Qual seu nome?", "mia_apresentação"),
    ("O que você faz?", "mia_propósito"),
    ("Quem é você, Mia?", "mia_apresentação"),
    ("O que é a Mia?", "mia_apresentação"),
    ("Mia, pode se apresentar?", "mia_apresentação"),
    ("Explique o que você é, Mia.", "mia_apresentação"),
    ("Mia, qual é o seu propósito?", "mia_propósito"),
    ("Qual é a sua função, Mia?", "mia_propósito"),
    ("Mia, por que você foi criada?", "mia_propósito"),
    ("O que você faz, Mia?", "mia_propósito"),
    
    # Jogos
    ("Me recomende um jogo.", "jogo"),
    ("Tem alguma recomendação de jogo?", "jogo"),
    
    # Clima
    ("Vai fazer sol amanhã?", "clima"),
    ("Como está a temperatura à noite?", "clima"),
    ("Me fale sobre as condições climáticas para o fim de semana.", "clima"),
    ("Dê-me uma atualização do clima para os próximos dias.", "clima"),
    
    # Filmes
    ("Você pode recomendar um filme para toda a família?", "filme"),
    ("Me fale sobre um filme recente de grande sucesso.", "filme"),
    ("Qual é um bom filme para assistir?", "filmes"),
    ("Compartilhe informações sobre os próximos lançamentos de filmes.", "filme"),
    
    # Restaurantes
    ("Estou com fome, onde posso encontrar um restaurante?", "restaurante"),
    ("Sugira um restaurante romântico para uma ocasião especial.", "restaurante"),
    ("Existem novos restaurantes na cidade que valem a pena experimentar?", "restaurante"),
    ("Me fale sobre os melhores restaurantes na cidade.", "restaurante"),
    
    # Direções
    ("Como chego ao aeroporto daqui?", "direções"),
    ("Você pode me ajudar a encontrar o caminho para a estação de trem mais próxima?", "direções"),
    ("Qual é a rota mais rápida para o shopping?", "direções"),
    ("Estou perdido; você pode me guiar até o centro da cidade?", "direções"),
    
    # Esportes
    ("Quem é o atual MVP da NBA?", "esportes"),
    ("Me fale sobre a partida recente de futebol entre os times A e B.", "esportes"),
    ("Qual é a pontuação do jogo de beisebol em andamento?", "esportes"),
    ("Me dê os destaques do último Super Bowl.", "esportes"),
    
    # Dever de casa
    ("Explique o conceito de cálculo para mim.", "dever_de_casa"),
    ("Você pode me ajudar com meu dever de história sobre a Segunda Guerra Mundial?", "dever_de_casa"),
    ("Estou tendo dificuldades com geometria; você pode me fornecer orientações?", "dever_de_casa"),
    ("Me fale sobre cientistas famosos e suas contribuições.", "dever_de_casa"),
    
    # Piada
    ("Compartilhe um trocadilho comigo.", "piada"),
    ("Me conte uma piada clássica de 'toc-toc'.", "piada"),
    ("Você conhece alguma piada sobre tecnologia?", "piada"),
    ("Me faça rir com uma história engraçada.", "piada"),
    
    # Livro
    ("Recomende um livro", "livro"),
    ("Me fale sobre livros bons", "livro"),
    ("Qual é um bom livro?", "livro"),
    ("Sugira um livro bom", "livro"),
    ("Me fale sobre autores renomados ou livros premiados", "livro"),
    ("Sugira uma coleção de livros", "livro"),
    
    # Programação
    ("Como posso começar a aprender aprendizado de máquina?", "programação"),
    ("Me fale sobre as linguagens de programação populares para desenvolvimento web.", "programação"),
    ("Explique o conceito de programação orientada a objetos.", "programação"),
    ("Quais são os melhores cursos de programação online disponíveis?", "programação"),
    
    # Notícias
    ("Me dê atualizações sobre o mercado de ações.", "notícias"),
    ("Me fale sobre os últimos avanços em energia renovável.", "notícias"),
    ("O que está acontecendo na política internacional?", "notícias"),
    ("Compartilhe informações sobre os avanços recentes na medicina.", "notícias"),
    
    # Tráfego
    ("Há tráfego pesado na estrada durante o horário de pico?", "trafégo"),
    ("Como estão as condições das estradas em caso de mau tempo?", "trafégo"),
    ("Me fale sobre fechamentos de estradas relacionados a construções.", "trafégo"),
    ("Existe um atalho para evitar congestionamentos de tráfego?", "trafégo"),
    
    # Comida
    ("Quais são alguns pratos italianos populares?", "comida"),
    ("Me fale sobre a história do sushi.", "comida"),
    ("Estou procurando receitas veganas; você pode recomendar algumas?", "comida"),
    ("Compartilhe dicas para assar biscoitos deliciosos.", "comida"),
    
    # Fatos Interessantes
    ("Me conte algo interessante.", "curiosidade"),
    ("Compartilhe um fato divertido", "curiosidade"),
    ("Qual é um fato interessante sobre algo?", "curiosidade"),
    ("Me fale sobre algo peculiar de todo o mundo.", "curiosidade"),
    
    # Linguagem
    ("Como posso praticar falar um novo idioma?", "linguagem"),
    ("Me fale sobre aplicativos de aprendizado de idiomas para crianças.", "linguagem"),
    ("Qual é a melhor maneira de aprender expressões idiomáticas?", "linguagem"),
    ("Compartilhe dicas para dominar a pronúncia em um idioma estrangeiro.", "linguagem"),
    
    # Exercício
    ("Qual é uma boa rotina de exercícios para ganhar músculos?", "exercicio"),
    ("Me fale sobre os benefícios do yoga para a saúde mental.", "exercicio"),
    ("Qual é a ciência por trás da perda de peso eficaz?", "exercicio"),
    ("Compartilhe dicas para manter a motivação durante o treinamento físico.", "exercicio"),
    
    # Notícias de Tecnologia
    ("Me fale sobre os recentes avanços em inteligência artificial.", "noticias_de_tecnologia"),
    ("Qual é o impacto da tecnologia 5G em dispositivos móveis?", "noticias_de_tecnologia"),
    ("Me dê uma visão geral das últimas tendências em cibersegurança.", "noticias_de_tecnologia"),
    ("Compartilhe informações sobre missões de exploração espacial.", "noticias_de_tecnologia"),
    
    # Viagem
    ("Quais são os destinos imperdíveis na Europa?", "viagem"),
    ("Me fale sobre dicas de segurança para viagens solo.", "viagem"),
    ("Sugira destinos de viagem econômicos.", "viagem"),
    ("Compartilhe histórias de suas próprias experiências de viagem.", "viagem"),
    
    # Filosofia
    ("Discuta o existencialismo e seus conceitos-chave.", "filosofia"),
    ("Quais são as principais teorias éticas na filosofia?", "filosofia"),
    ("Compartilhe pensamentos sobre a filosofia da felicidade.", "filosofia"),
    ("Discuta o conceito de livre arbítrio versus determinismo.", "filosofia")
]


# Data de treino com subtopicos específicos
train_data.extend([   
    # Clima com Localização\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    ("Como está o clima hoje em algum lugar do mundo?", "clima_localização"),
    ("Me dê a previsão do tempo para amanhã em algum lugar do mundo.", "clima_localização_prev"),
    ("Qual é a temperatura em algum lugar do mundo agora?", "clima_localização_temp"),
    ("Me fale sobre a precipitação em algum lugar do mundo.", "clima_localização_preci"),
    
    # Filme\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    ("Você pode recomendar um filme de comédia?", "filme_gênero_comedia"),
    ("Me recomende um filme de comédia.", "filme_gênero_comedia"),
    
    ("Você pode recomendar um filme de super-herois?", "filme_gênero_super"),
    ("Me recomende um filme de super-herois?", "filme_gênero_super"),
    
    ("Você pode recomendar um filme de ficção científica?", "filme_gênero_scifi"),
    ("Me recomende um filme de ficção científica?", "filme_gênero_scifi"),
    
    ("Você pode recomendar um bom filme animado?.", "filme_animação"),
    ("Me recomende um bom filme animado?.", "filme_animação"),
    
    # Jogos\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    ("Recomende um jogo de aventura emocionante.", "jogo_aventura"),
    ("Me Recomende um jogo de aventura.", "jogo_aventura"),
    
    ("Estou procurando por um jogo de estratégia desafiador. Alguma sugestão?", "jogo_estratégia"),
    ("Me recomende um jogo de estratégia", "jogo_estratégia"),
    
    ("Quero jogar algo multiplayer com meus amigos. Qual jogo você recomenda?", "jogo_multiplayer"),
    ("Me recomende um jogo multiplayer", "jogo_multiplayer"),
    
    ("Qual é um jogo de RPG épico que posso começar a jogar?", "jogo_rpg"),
    ("Me recomende um jogo de RPG", "jogo_rpg"),
    
    ("Estou interessado em jogos de simulação. Alguma recomendação?", "jogo_simulação"),
    ("Me recomende um jogo de simulação", "jogo_simulação"),
    
    ("Procuro um jogo de quebra-cabeça intrigante. O que você sugere?", "jogo_quebra_cabeça"),
    ("Me recomende um jogo de quebra-cabeça", "jogo_quebra_cabeça"),
    
    ("Quais são os melhores jogos de tiro em primeira pessoa disponíveis?", "jogo_tiro_primeira_pessoa"),
    ("Me recomende um jogo de tiro em primeira pessoa", "jogo_tiro_primeira_pessoa"),
    
    ("Recomende um jogo indie único que vale a pena jogar.", "jogo_indie"),
    ("Me recomende um jogo indie.", "jogo_indie"),
    
    ("Estou interessado em jogos de mundo aberto. Alguma recomendação?", "jogo_mundo_aberto"),
    ("Me recomende um jogo de mundo aberto", "jogo_mundo_aberto"),
    
    ("Quero jogar um jogo relaxante e casual. Qual você sugere?", "jogo_casual"),
    ("Me recomende um jogo casual", "jogo_casual"),
    ("Me recomende um jogo relaxante", "jogo_casual"),
    
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
    # Restaurante
    ("Estou com vontade de comida italiana; sugira restaurantes italianos próximos.", "restaurante_cozinha"),
    ("Sugira um restaurante romântico com área ao ar livre para nosso aniversário.", "restaurante_ocasião"),
    ("Existem novos restaurantes com música ao vivo na cidade?", "restaurante_característica"),
    ("Me fale sobre lugares de sobremesa famosos por seu cheesecake.", "restaurante_sobremesa"),
    
    # Direções
    ("Como chegar ao aeroporto do centro usando transporte público?", "direções_transportepúblico"),
    ("Você pode me ajudar a encontrar o posto de carregamento de veículo elétrico mais próximo?", "direções_carregamento_veículoelétrico"),
    ("Preciso de instruções para caminhar do hotel até o museu de arte.", "direções_a_pé"),
    ("Qual é a melhor rota para o centro de convenções durante o horário de pico?", "direções_tráfego"),
    
    # Esportes
    ("Quem é o artilheiro na Premier League nesta temporada?", "esportes_liga"),
    ("Me fale sobre a partida de tênis recente entre o Jogador A e o Jogador B.", "esportes_partida"),
    ("Qual é a pontuação do jogo de basquete entre os Times X e Y?", "esportes_jogo"),
    ("Me dê os destaques das últimas Olimpíadas.", "esportes_evento"),
    
    # Dever de Casa
    ("Explique o conceito de trigonometria.", "deverdecasa_matemática"),
    ("Você pode me ajudar com meu dever de história sobre o Antigo Egito?", "deverdecasa_história"),
    ("Estou com dificuldades em química; você pode me dar orientações?", "deverdecasa_ciência"),
    ("Me fale sobre autores famosos e suas contribuições literárias.", "deverdecasa_literatura"),
    
    # Piada
    ("Compartilhe um trocadilho relacionado à tecnologia.", "piada_tecnologia"),
    ("Me conte uma piada clássica de 'toc-toc'.", "piada_toc_toc"),
    ("Você conhece alguma piada sobre animais?", "piada_animais"),
    ("Me faça rir com uma piada sobre comida.", "piada_comida"),
    
    # Livro
    ("Recomende um romance clássico de Charles Dickens.", "livro_charles_dickens"),
    ("Recomende um livro clássico de Charles Dickens.", "livro_charles_dickens"),
    ("Recomende um livro de Charles Dickens.", "livro_charles_dickens"),
    
    ("Me fale sobre os autores ganhadores do Prêmio Pulitzer.", "livro_pulitzer"),
    
    ("Qual é uma boa série de livros de fantasia para jovens leitores?", "livro_jovens_adultos"),
    ("Me recomende uma boa série de livros para jovens adultos.", "livro_jovens_adultos"),
    
    ("Sugira uma biografia de um cientista famoso.", "livro_biografia"),
    
    ("Quem escreveu o clássico romance 'Orgulho e Preconceito'?", "livro_orgulho_preconceito_autor"),
    
    ("Me fale sobre os autores ganhadores do Prêmio Nobel em literatura.", "livro_nobel_prêmio_literatura"),
    
    ("Qual é a importância literária de 'Moby Dick'?", "livro_moby_dick"),
    
    ("Sugira uma coleção de contos de um autor renomado.", "livro_contos"),
    
    # Programação
    ("Como posso começar a aprender desenvolvimento web?", "programação_desenvolvimento_web"),
    ("Me fale sobre as linguagens de programação populares para ciência de dados.", "programação_ciência_dados"),
    ("Explique o conceito de recursão na programação.", "programação_recurssão"),
    ("Quais são os melhores recursos para aprender desenvolvimento de aplicativos móveis?", "programação_desenvolvimento_móvel"),
    
    # Notícias
    ("Me dê atualizações sobre o setor de tecnologia.", "notícias_tecnologia"),
    ("Me fale sobre as últimas descobertas na exploração espacial.", "notícias_espacial"),
    ("O que está acontecendo no mundo da política hoje?", "notícias_política"),
    ("Compartilhe informações sobre avanços recentes na pesquisa médica.", "notícias_medicina"),
    
    # Tráfego
    ("Existem fechamentos de estradas devido à construção na área central?", "tráfego_construção"),
    ("Como estão as condições das estradas em caso de chuva forte?", "tráfego_condições_chuva"),
    ("Me fale sobre acidentes na rodovia e seu impacto no tráfego.", "tráfego_acidentes"),
    ("Existe uma rota cênica para um passeio tranquilo neste fim de semana?", "tráfego_rota_cênica"),
    
    # Comida
    ("Quais são alguns pratos italianos de massa populares?", "comida_massa_italiana"),
    ("Me fale sobre a história do sushi e seus diferentes tipos.", "comida_historia_sushi"),
    ("Estou procurando receitas de sobremesas veganas; você pode recomendar algumas?", "comida_sobremesas_veganas"),
    ("Compartilhe dicas para assar um bolo de chocolate perfeito.", "comida_dicas_bolo_chocolate"),
    
    # Fato Interessante
    ("Me conte algo surpreendente sobre os planetas em nosso sistema solar.", "fato_interessante_sistema_solar"),
    ("Compartilhe um fato divertido sobre figuras históricas famosas e suas peculiaridades.", "fato_interessante_figuras_historicas"),
    ("Qual é um fato interessante sobre animais noturnos?", "fato_interessante_animais_noturnos"),
    ("Me fale sobre tradições únicas de diferentes culturas.", "fato_interessante_tradições_culturais"),
    
    # Linguagem
    ("Como posso melhorar minha pronúncia em espanhol?", "linguagem_pronúncia"),
    ("Me fale sobre aplicativos de aprendizado de idiomas para viajantes.", "linguagem_aplicativos_viajantes"),
    ("Quais são algumas frases comuns em francês para iniciantes?", "linguagem_frases_françês_iniciantes"),
    ("Compartilhe dicas para dominar habilidades de conversação em mandarim.", "linguagem_conversação_mandarim"),
    
    # Exercício
    ("Qual é uma rotina de exercícios adequada para melhorar a flexibilidade?", "exercício_flexibilidade"),
    ("Me fale sobre os benefícios da meditação para clareza mental.", "exercício_meditação_benefícios"),
    ("Como posso gerenciar efetivamente meu peso por meio de dieta e exercícios?", "exercício_gerenciamento_peso"),
    ("Compartilhe dicas para se manter motivado durante o treinamento para maratona.", "exercício_treinamento_maratona"),
    
    # Notícias de Tecnologia
    ("Me fale sobre avanços recentes em inteligência artificial.", "notícias_tecnologia_avanços_ai"),
    ("Qual é o impacto da tecnologia blockchain nas finanças?", "notícias_tecnologia_blockchain_finanças"),
    ("Me dê uma visão geral das últimas tendências em segurança de dados.", "notícias_tecnologia_tendências_segurança_dados"),
    ("Compartilhe informações sobre próximas missões espaciais.", "notícias_tecnologia_missões_espaciais"),
    
    # Viagem
    ("Quais são os locais históricos imperdíveis em Roma?", "viagem_locais_roma_históricos"),
    ("Me fale sobre dicas de segurança para viagens solo para viajantes femininas.", "viagem_dicas_viagem_solo_segurança_feminina"),
    ("Sugira destinos de viagem econômicos para mochileiros.", "viagem_destinos_econômicos_mochileiros"),
    ("Compartilhe sua experiência mochilando pelo Sudeste Asiático.", "viagem_experiência_mochilagem"),
    
    # Filosofia
    ("Discuta a filosofia existencialista de Jean-Paul Sartre.", "filosofia_existencialismo_sartre"),
    ("Quais são as principais teorias éticas na filosofia contemporânea?", "filosofia_teorias_éticas"),
    ("Compartilhe seus pensamentos sobre a filosofia da felicidade e bem-estar.", "filosofia_felicidade_filosofia"),
    ("Discuta o debate em torno do livre-arbítrio versus determinismo.", "filosofia_livre_arbítrio_determinismo")
])

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

# Base de Respostas
knowledge_base = {
    "mia_assuntos": [
        "Eu tenho respostas prontas para os assuntos clima, filmes, restaurantes, direções, esportes, piadas, jogos, livros, programação, notícias, comida, e filosofia. Tente me pedir sobre recomendações de jogos ou filmes!",
    ],
    "mia_apresentação": [
        "Eu sou a Mia, uma IA desenvolvida por um grupinho legal para interagir com você e fornecer informações, assistência e entretenimento.",
        "Meu nome é Mia. Estou aqui para responder às suas perguntas e oferecer ajuda de várias maneiras.",
        "Meu nome é, e sou uma IA que pode responder á algumas perguntas pré-determinadas, projetada para ser uma assistente virtual versátil.",
    ],
    "mia_propósito": [
        "Meu propósito é facilitar nossa comunicação, fornecer informações úteis e envolver você em conversas interativas.",
        "Fui criada para responder a uma ampla variedade de perguntas com respostas pré-definidas. Por enquanto, eu só consigo dar respostas sobre alguns assuntos, por isso desculpe se eu não conseguir responder algo, ou repetir minhas respostas!",
        "Estou aqui para tornar a busca por informações e a interação com a tecnologia mais acessíveis e convenientes para você.",
    ],
    "clima": [
        "Hoje está {clima} e {temperatura}.",
        "Espera-se algumas chuvas esta tarde.",
        "O clima está bastante imprevisível hoje.",
        "Você pode precisar de um guarda-chuva; há chance de chuva.",
        "Ouvi dizer que o dia lá fora será {clima}."
    ],
    "filme": [
        "O filme começa às {hours}h.",
        "O filme está programado para as {hours}h{minutes}.",
        "{recommendation} verificar o site do cinema para horários do filme.",
        "Não tenho certeza sobre o horário do filme agora.",
        "O filme que você procura está passando em vários horários hoje."
    ],
    "restaurante": [
        "{recommendation} o restaurante italiano na Rua Principal.",
        "Que tal experimentar o novo restaurante de sushi {location}?",
        "O restaurante mexicano {location} é excelente.",
        "{recommendation} do restaurante de frutos do mar {location}.",
        "Há um café aconchegante na esquina que serve ótimo café."
    ],
    
      "jogo": [
        "Para um jogo relaxante e casual, 'Animal Crossing: New Horizons' é perfeito para criar sua própria ilha.",
        "Relaxe e desafie seu cérebro com 'Calm Waters: A Point and Click Adventure' para uma experiência casual.",
        "'Slime Rancher' oferece uma jogabilidade relaxante enquanto cria seu próprio rancho de slime.",
        "Um jogo de aventura emocionante que você pode gostar é 'The Legend of Zelda: Breath of the Wild'.",
        "'Uncharted 4: A Thief's End' oferece uma experiência de aventura incrível com uma história envolvente.",
        "Para aventuras épicas, 'The Witcher 3: Wild Hunt' é altamente recomendado.",
        "Para diversão multiplayer com amigos, 'Among Us' é uma excelente escolha para traições e mistérios.",
        "'Rocket League' oferece partidas de futebol com carros e é ótimo para jogar com amigos.",
        "Experimente 'Overwatch' se você gosta de jogos de tiro em equipe com heróis únicos.",
        "'The Elder Scrolls V: Skyrim' é um RPG épico com um mundo vasto para explorar e missões cativantes.",
        "Entre em um mundo de fantasia com 'Dark Souls III', conhecido por seu desafio e atmosfera sombria.",
        "'Persona 5' é um RPG japonês aclamado por sua narrativa e personagens memoráveis.",
        "Para jogos de simulação, 'The Sims 4' oferece a experiência definitiva de criar e gerenciar vidas virtuais.",
        "Entre no mundo agrícola de 'Stardew Valley' e cultive sua fazenda.",
        "'Microsoft Flight Simulator' é uma simulação de voo incrivelmente realista para entusiastas da aviação.",
        "'The Witness' é um quebra-cabeça em mundo aberto repleto de desafios de lógica.",
        "Experimente 'Portal 2' para quebra-cabeças criativos envolvendo portais.",
        "'Baba Is You' é um jogo de quebra-cabeça único que permite reescrever as regras.",
        "Para tiroteio em primeira pessoa, 'Doom Eternal' oferece ação intensa contra demônios.",
        "Experimente 'Counter-Strike: Global Offensive' para partidas competitivas de tiro.",
        "'Half-Life: Alyx' leva a experiência de realidade virtual em primeira pessoa a outro nível.",
        "O jogo indie 'Hollow Knight' é uma aventura subterrânea emocionante.",
        "'Undertale' é uma experiência indie única com escolhas significativas.",
        "Explore um mundo misterioso em 'Journey', um jogo indie premiado.",
        "'Red Dead Redemption 2' oferece um mundo aberto expansivo no Velho Oeste.",
        "Para um cenário pós-apocalíptico, 'Horizon Zero Dawn' é altamente recomendado.",
        "'Assassin's Creed Valhalla' leva você para a Era Viking em um mundo aberto impressionante.",
        "Para um jogo relaxante e casual, 'Animal Crossing: New Horizons' é perfeito para criar sua própria ilha.",
        "Relaxe e desafie seu cérebro com 'Calm Waters: A Point and Click Adventure' para uma experiência casual.",
        "'Slime Rancher' oferece uma jogabilidade relaxante enquanto cria seu próprio rancho de slime.",
    ],
      
    "direções": [
        "Vire à {direction} na próxima interseção e dirija por {numbersmall},{numbersmal1} km.",
        "Segue reto, parça.",
        "Não tenho certeza sobre as direções; {recommendation} você {researchAtivo} sobre em um mapa.",
        "Para chegar lá, você vai querer seguir ao {cardinal} na Rodovia {numbers}.",
        "Vire à {direction} no semáforo e siga as placas."
    ],
    "esportes": [
        "A pontuação está atualmente empatada em {numbersmall}-{numbersmal1}.",
        "O time da casa está liderando por um ponto.",
        "Desculpe, não tenho acesso a placares de esportes em tempo real.",
        "Você pode verificar um site de notícias esportivas para as últimas atualizações.",
        "O jogo está na prorrogação; é uma partida emocionante!"
    ],
    "lição de casa": [
        "Claro, posso ajudar com sua lição de matemática. Qual é o problema?",
        "Não sou qualificado para ajudar com sua lição de casa, mas posso tentar.",
        "Vamos ver se podemos resolver seu problema de matemática juntos.",
        "{recommendation} verificar fóruns de matemática online para ajuda.",
        "Estou feliz em ajudar com perguntas de matemática, se puder."
    ],
    "piada": [
        "Por que o computador pegou um resfriado? Tinha muitas janelas abertas!",
        "Por que o espantalho ganhou um prêmio? Porque ele era excepcional em seu campo!",
        "Linhas paralelas têm muito em comum. É uma pena que elas nunca se encontrem!",
    ],
    "livro": [
        "{recommendation} 'O Grande Gatsby' de F. Scott Fitzgerald.",
        "{recommendation} 'O Sol é para Todos' de Harper Lee?",
        "{recommendation} ler '1984' de George Orwell; é um clássico.",
        "Se você gosta de fantasia, {recommendation} a trilogia 'O Senhor dos Anéis' é uma leitura obrigatória.",
        "Para os fãs de ficção científica, 'Duna' de Frank Herbert é {adjective_good}."
    ],
    "programação": [
        "Você pode melhorar suas habilidades de programação trabalhando em projetos e praticando regularmente.",
        "{recommendation} fazer cursos ou tutoriais de programação online.",
        "Aprender com projetos de código aberto pode ser uma experiência valiosa.",
        "Programação trata de resolver problemas; enfrente problemas desafiadores para aprender.",
        "Tente participar de comunidades de programação e desafios de codificação."
    ],
    "notícias": [
        "Desculpe, não tenho acesso a atualizações de notícias em tempo real.",
        "Você pode verificar um site de notícias ou aplicativo para as últimas notícias.",
        "Para notícias de última hora, {recommendation} seguir fontes de notícias confiáveis nas redes sociais.",
        "{research} sobre você mesmo, preguiçoso!",
        "Recomendo se manter informado sobre eventos atuais a partir de múltiplas fontes."
    ],
    "tráfego": [
        "O tráfego {location} está fluindo suavemente.",
        "Parece haver alguma congestão na {location}.",
        "Sugiro usar um aplicativo de navegação para atualizações de tráfego em tempo real.",
        "Você pode considerar uma rota alternativa para evitar o trânsito.",
        "Planeje sua viagem durante as horas de menor movimento para evitar tráfego pesado."
    ],
    "comida": [
        "Eu amo todos os tipos de culinária, mas a italiana é uma favorita pessoal.",
        "Eu sei lá, porra. Eu não como!",
        "Explorar novas cozinhas pode ser uma deliciosa aventura.",
        "A comida aproxima as pessoas; {recommendation} fazer um jantar com amigos.",
        "Para uma ocasião especial, experimente um restaurante de alta gastronomia com um menu degustação."
    ],
    "curiosidade": [
        "Claro! Você sabia que o mel nunca estraga? Arqueólogos encontraram potes de mel em tumbas egípcias antigas com mais de 3.000 anos e ainda perfeitamente comestíveis!",
        "Aqui está uma curiosidade: Os polvos têm três corações - um bombeia sangue para o corpo, e dois bombeiam sangue para as brânquias!",
        "Você sabia que um grupo de flamingos é chamado de 'flamboiante'?",
        "Na Suíça, é ilegal ter apenas um porquinho-da-índia porque eles são propensos à solidão!",
        "Aqui está uma curiosidade legal: A Torre Eiffel pode ficar 15 cm mais alta durante o verão devido à expansão do ferro no calor. Sabe o que mais expande no verão? ( ͡° ͜ʖ ͡°)"
    ],
    "livros": [
        "Muitas pessoas gostam de ler livros de J.K. Rowling.",
        "Existem tantos ótimos autores para escolher; depende do seu gosto!",
        "O mundo da literatura é vasto; explore diferentes gêneros e autores para encontrar seus favoritos.",
        "{recommendation} ingressar em um clube do livro para discutir livros e descobrir novos títulos.",
        "A leitura é uma maneira maravilhosa de expandir seu conhecimento e imaginação."
    ],
    "idioma": [
        "Aprender um novo idioma pode ser divertido! {recommendation} fazer aulas, usar aplicativos de aprendizado de idiomas e praticar com falantes nativos.",
        "A imersão é uma ótima maneira de aprender um idioma; tente assistir a filmes ou ler livros no idioma-alvo.",
        "Programas de intercâmbio de idiomas permitem que você pratique com falantes nativos enquanto os ajuda a aprender seu idioma.",
        "A consistência é fundamental no aprendizado de idiomas; reserve um tempo dedicado para a prática diária.",
        "Aprender um novo idioma pode abrir portas para novas culturas e experiências."
    ],
    "fitness": [
        "Para se manter em forma e saudável, experimente uma dieta equilibrada e exercícios regulares. Você pode se juntar a uma academia ou praticar um esporte que goste.",
        "Consultar um instrutor de fitness também pode ajudar a criar um plano de fitness personalizado.",
        "Yoga e meditação são ótimos para o bem-estar físico e mental.",
        "Lembre-se de que não se trata apenas do corpo; a saúde mental também é importante. {recommendation} práticas de atenção plena.",
        "Manter-se hidratado e dormir o suficiente são essenciais para a saúde geral."
    ],
    "notícias_tecnológicas": [
        "Para as últimas notícias de tecnologia, confira sites como TechCrunch, The Verge e Ars Technica.",
        "Você também pode assinar boletins de notícias de tecnologia para receber atualizações na sua caixa de entrada.",
        "{recommendation} seguir influenciadores de tecnologia nas redes sociais para insights e tendências.",
        "Podcasts são uma ótima maneira de se manter informado sobre tecnologia; encontre podcasts que cubram suas áreas de interesse.",
        "A indústria de tecnologia está em constante evolução, por isso é importante se manter atualizado."
    ],
    "viagem": [
        "{recommendation} explorar as belas praias de Bali, Indonésia!",
        "Você pode gostar de uma viagem à cidade histórica de Roma, Itália.",
        "{recommendation} fazer trilhas nas paisagens deslumbrantes da Patagônia, Argentina.",
        "Para uma experiência cultural, visite Kyoto, Japão, e explore seus templos e tradições.",
        "A Nova Zelândia oferece uma beleza natural deslumbrante e aventuras ao ar livre."
    ],
    "filosofia": [
        "O significado da vida é uma pergunta filosófica profunda que as pessoas têm ponderado por séculos. Pode variar muito de pessoa para pessoa. Eu gosto de aneis de cebola. Ache algo que você gosta e você já vai ter andando metade do caminho!",
        "Alguns buscam significado por meio de relacionamentos, realizações ou crescimento pessoal.",
        "Filósofos como Sócrates, Platão e Aristóteles exploraram questões sobre o propósito da vida e ética. Pergunte pra eles!",
        "Filósofos existencialistas como Jean-Paul Sartre discutiram a liberdade individual e a responsabilidade na busca de significado. Pergunte pra ele!",
        "{recommendation} ler obras filosóficas para explorar diferentes perspectivas sobre o significado da vida. Vai estudar!"
    ],
}

# Respostas Adicionais
knowledge_base.update({
    "finanças": [
        "Economizar dinheiro é importante. Considere criar um orçamento e cortar despesas desnecessárias.",
        "Investir sabiamente pode ajudar a fazer seu dinheiro crescer ao longo do tempo.",
        "Comece definindo metas financeiras e siga um plano de economia."
    ],
    "espaço": [
        "A exploração espacial tem uma história rica, desde o primeiro pouso humano na Lua até os rovers de Marte explorando o planeta vermelho.",
        "A NASA e outras agências espaciais fizeram descobertas significativas sobre nosso sistema solar e além.",
        "O Telescópio Espacial Hubble forneceu imagens impressionantes de galáxias distantes."
    ],
    "negócios": [
        "Iniciar um pequeno negócio requer planejamento cuidadoso, um sólido plano de negócios e pesquisa de mercado.",
        "Considere buscar conselhos de empreendedores que lançaram com sucesso seus próprios negócios.",
        "Explore opções de financiamento, como empréstimos, subsídios ou capital de risco."
    ],
    "documentário": [
        "Documentários oferecem uma ótima maneira de aprender sobre questões do mundo real, eventos históricos e pessoas fascinantes.",
        "Considere assistir a 'Planeta Terra' para uma cinematografia impressionante da natureza ou 'Blackfish' para um documentário instigante sobre a vida marinha.",
        "Documentários podem fornecer insights valiosos sobre diversos assuntos."
    ],
    "estudo": [
        "Técnicas de estudo eficazes incluem estabelecer um cronograma, criar um ambiente livre de distrações e fazer pausas.",
        "Pratique a aprendizagem ativa resumindo pontos-chave e ensinando-os a alguém.",
        "Utilize recursos como cartões de memória e guias de estudo online."
    ],
    "animais": [
        "O mundo é lar de uma vasta variedade de espécies de animais fascinantes, desde o pequeno beija-flor até o majestoso elefante.",
        "Você sabia que os polvos têm três corações e sangue azul?",
        "Alguns animais, como camaleões, podem mudar a cor da pele para se misturarem ao ambiente."
    ],
    "sucesso": [
        "O sucesso muitas vezes requer trabalho árduo, determinação e resiliência.",
        "Figuras famosas como Winston Churchill, Thomas Edison e Albert Einstein compartilharam insights valiosos sobre o sucesso.",
        "Uma frase famosa é 'O sucesso não é final, o fracasso não é fatal: é a coragem de continuar que conta.' - Winston Churchill"
    ],
    "fotografia": [
        "Melhorar suas habilidades de fotografia envolve aprender sobre composição, iluminação e configurações da câmera.",
        "A prática leva à perfeição; leve sua câmera com você e capture momentos em sua vida diária.",
        "Considere se inscrever em cursos de fotografia para aprimorar suas habilidades."
    ],
    "culinária": [
        "Fazer pizza caseira é divertido! Comece com uma receita de massa de pizza e seus ingredientes favoritos.",
        "Pré-aqueça o forno a uma temperatura alta para obter uma massa crocante e não esqueça do queijo!",
        "Experimente diferentes combinações de molho e ingredientes para criar sua pizza perfeita."
    ],
    "meditação": [
        "A meditação pode reduzir o estresse e melhorar a clareza mental. Encontre um espaço tranquilo e sente-se confortavelmente.",
        "Concentre-se na sua respiração e deixe de lado as distrações. Aplicativos de meditação podem guiá-lo em sessões.",
        "A prática regular pode levar a uma maior atenção plena e paz interior."
    ],
    "música": [
        "O rock clássico oferece sucessos atemporais de bandas como The Beatles, Led Zeppelin e Pink Floyd.",
        "Considere ouvir 'The Dark Side of the Moon' do Pink Floyd para uma experiência musical lendária.",
        "A música tem o poder de evocar emoções e memórias."
    ],
    "charada": [
        "Aqui está uma charada: Eu falo sem boca e ouço sem ouvidos. Não tenho corpo, mas ganho vida com o vento. O que sou eu?",
        "Charadas são uma maneira divertida de exercitar o cérebro e desafiar o pensamento.",
        "A resposta a essa charada é um eco!"
    ],
    "história": [
        "A Grande Muralha da China é um símbolo icônico da antiga China, construída para proteger contra invasões.",
        "A construção da Grande Muralha se estendeu por séculos e várias dinastias.",
        "A muralha se estende por mais de 21.000 quilômetros e é um Patrimônio Mundial da UNESCO."
    ],
    "mochilão": [
        "Planejar uma viagem de mochilão envolve escolher destinos, fazer as malas com itens essenciais e criar um itinerário.",
        "Pesquise as melhores trilhas, acomodações e regulamentações locais antes de embarcar em sua aventura.",
        "Mochilar permite que você se conecte com a natureza e experimente o mundo de uma maneira única."
    ],
    "gerenciamento de tempo": [
        "O gerenciamento eficaz do tempo inclui definir prioridades, estabelecer metas claras e eliminar distrações.",
        "Use técnicas como a Técnica Pomodoro para dividir o trabalho em intervalos focados.",
        "Ferramentas como listas de tarefas e calendários digitais podem ajudar você a se manter organizado."
    ],
    "escrita": [
        "O bloqueio do escritor é comum, mas pode ser superado. Tente escrever livremente ou mudar seu ambiente de escrita.",
        "Explore diferentes prompts de escrita ou faça brainstorming de ideias com amigos ou colegas.",
        "Lembre-se de que o primeiro rascunho não precisa ser perfeito; comece simplesmente a escrever."
    ],
    "ciência": [
        "A ciência revela continuamente descobertas fascinantes sobre o mundo, desde partículas subatômicas até galáxias distantes.",
        "Os cientistas estudam tópicos como genética, mudanças climáticas e os mistérios do universo.",
        "Você sabia que o maior deserto do mundo não é o Saara, mas a Antártica?"
    ],
    "cibersegurança": [
        "Uma carreira em cibersegurança envolve proteger sistemas de computador e redes contra ameaças cibernéticas.",
        "Considere buscar certificações como Certified Information Systems Security Professional (CISSP) ou Certified Ethical Hacker (CEH).",
        "Profissionais de cibersegurança desempenham um papel crucial na proteção de informações sensíveis."
    ],
    "café": [
        "Preparar a xícara de café perfeita começa com grãos de qualidade e café moído na hora.",
        "Experimente diferentes métodos de preparo, como coador, prensa francesa ou máquinas de espresso.",
        "Não se esqueça de saborear o aroma e apreciar sua xícara de café!"
    ]
})


# Respostas de Subtópicos
knowledge_base.update({

    # Subtópicos de Clima||||||||||||||||||||||||||||||||||||||||||||||||||||
    "clima_localização": [
        "Em {place}, o clima está {clima} e {temperatura} hoje.",
    ],
    
    "clima_localização_prev": [
        "Espere chuvas em {place}.",
    ],
    
    "clima_localização_temp": [
        "A temperatura atual em {place} é de {number}°C.",
    ],
    
    "clima_localização_preci": [
        "Em {place} teve {numbersmall} polegadas de precipitação nesta semana. Eu acho.",
    ],

    # Subtópicos de Filmes|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    "filme_gênero_comedia": [
        "{recommendation} assistir a uma comédia familiar como 'Procurando Nemo'.",
        "Claro! Um {adjective_good} filme de comédia para assistir é 'Superbad'.",
        "'Debi & Lóide - Dois Idiotas em Apuros' é um clássico da comédia que vai fazer você rir do início ao fim.",
        "Um {adjective_good} filme de comédia que você pode gostar é 'Se Beber Não Case 1 e 2'. É uma comédia adulta hilária.",
    ],
    
    "filme_gênero_super": [
        "Se você gosta de super-heróis, não pode perder 'Os Vingadores'. É um filme sobre um grupo de herois e muitos de seus integrantes tem seus próprios filmes individuais!.",
        "O bom filme de super-herói é 'Homem-Aranha: Sem Volta para Casa'.",
        "'Homem-Aranha no Aranhaverso' é uma animação incrível que apresenta vários Homens-Aranha de diferentes universos.",
        "'Besouro Verde' é uma excelente sátira do genero de super-herois!'.",
    ],
    
    "filme_gênero_scifi": [
        "{recommendation} assistir a uma comédia familiar como 'Procurando Nemo'.",
        "Absolutamente! 'Blade Runner 2049' é uma obra-prima de ficção científica que combina uma narrativa envolvente com visuais deslumbrantes. Será que eu sou uma replicante :o?"
        "Com certeza! 'A Chegada' é uma escolha fascinante se você gosta de ficção científica com uma abordagem cerebral e intrigante.",
        "Apesar de ser mais próximo do genero de fantasia, 'Star Wars' é um clássico com uma temática espacial incrível!",
    ],
    
    "filme_gênero_animação": [
        "'Toy Story' é um clássico dos filmes animados que é perfeito para todas as idades.",
        " 'Procurando Nemo' é uma aventura emocionante no fundo do mar que vai encantar você.",
        "'Homem-Aranha no Aranhaverso' e sua sequência são animações incríveis que ganharam vários prêmios de animação! Aranhaverso 2 é provavelmente o melhor filme de todos os tempos, papo reto. Bom",
        "'O Castelo Animado' ou 'O Castelo Vivo de Howl' é um filme de origem japonêsa que é muito amado mundialmente.",
    ],
    
    #Subtópicos Livros|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    
     "livro_charlesdickens": [
        "Um romance clássico de Charles Dickens que eu recomendo é 'Grandes Esperanças'.",
        "'Oliver Twist' é outro romance clássico de Charles Dickens que você pode desfrutar.",
        "Se você gosta de Charles Dickens, 'David Copperfield' é uma escolha atemporal.",
    ],
    "livro_pulitzer": [
        "Autores notáveis que ganharam o Prêmio Pulitzer incluem Ernest Hemingway, Harper Lee e Toni Morrison.",
        "John Steinbeck, Jennifer Egan e Jhumpa Lahiri estão entre os escritores que receberam o Prêmio Pulitzer.",
        "O Prêmio Pulitzer é uma honra literária prestigiosa concedida a autores talentosos.",
    ],
    "livro_jovens_adultos": [
        "Uma série de livros de fantasia popular para jovens leitores é 'Harry Potter' de J.K. Rowling.",
        "'Percy Jackson e os Olimpianos' de Rick Riordan é uma série fantástica para jovens.",
        "Os livros 'Bridgertons' são conhecidos por seu apelo aos leitores jovens adultos.",
    ],
    "livro_biografia": [
        "Uma biografia interessante de um cientista famoso é 'Uma Breve História do Tempo' de Stephen Hawking.",
        "'A Vida de Albert Einstein' é uma biografia cativante de um dos cientistas mais influentes da história.",
        "Para uma biografia envolvente, considere 'Steve Jobs' de Walter Isaacson.",
    ],
    "livro_orgulho_preconceito_autor": [
        "O clássico romance 'Orgulho e Preconceito' foi escrito por Jane Austen.",
        "A autora do renomado 'Orgulho e Preconceito' é Jane Austen, uma das escritoras mais queridas do século XIX.",
        "'Orgulho e Preconceito' é uma obra-prima literária de Jane Austen.",
    ],
    "livro_nobel_prêmio_literatura": [
        "Alguns dos autores notáveis que ganharam o Prêmio Nobel em Literatura incluem Gabriel García Márquez, Toni Morrison e Kazuo Ishiguro.",
        "O Prêmio Nobel em Literatura reconheceu talentos literários excepcionais como Gabriel García Márquez.",
        "Receber o Prêmio Nobel em Literatura é um dos maiores elogios para um escritor.",
    ],
    "livro_moby_dick": [
        "'Moby Dick' é uma obra-prima literária escrita por Herman Melville, conhecida por sua complexidade e simbolismo.",
        "A importância literária de 'Moby Dick' reside em sua narrativa épica e exploração de temas profundos.",
        "Herman Melville é o autor por trás da notável obra 'Moby Dick'.",
    ],
    "livro_contos": [
        "Para uma coleção de contos cativante, considere 'Contos de Canterbury' de Geoffrey Chaucer.",
        "'Contos de Edgar Allan Poe' é uma coleção clássica de contos de terror e mistério.",
        "Uma coleção de contos de F. Scott Fitzgerald, como 'Contos da Era do Jazz', oferece vislumbres da vida na década de 1920.",
    ],
    
    #Subtópico Jogos|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    
     "jogo_aventura": [
        "Um jogo de aventura emocionante que você pode gostar é 'The Legend of Zelda: Breath of the Wild'.",
        "'Uncharted 4: A Thief's End' oferece uma experiência de aventura incrível com uma história envolvente.",
        "Para aventuras épicas, 'The Witcher 3: Wild Hunt' é altamente recomendado.",
    ],
    "jogo_estratégia": [
        "'Civilization VI' é um jogo de estratégia desafiador que oferece muitas opções táticas.",
        "Experimente 'Stellaris' se você gosta de estratégia espacial e exploração de galáxias.",
        "'Total War: Three Kingdoms' combina estratégia e combate em um cenário histórico intrigante.",
    ],
    "jogo_multiplayer": [
        "Para diversão multiplayer com amigos, 'Among Us' é uma excelente escolha para traições e mistérios.",
        "'Rocket League' oferece partidas de futebol com carros e é ótimo para jogar com amigos.",
        "Experimente 'Overwatch' se você gosta de jogos de tiro em equipe com heróis únicos.",
    ],
    "jogo_rpg": [
        "'The Elder Scrolls V: Skyrim' é um RPG épico com um mundo vasto para explorar e missões cativantes.",
        "Entre em um mundo de fantasia com 'Dark Souls III', conhecido por seu desafio e atmosfera sombria.",
        "'Persona 5' é um RPG japonês aclamado por sua narrativa e personagens memoráveis.",
    ],
    "jogo_simulação": [
        "Para jogos de simulação, 'The Sims 4' oferece a experiência definitiva de criar e gerenciar vidas virtuais.",
        "Entre no mundo agrícola de 'Stardew Valley' e cultive sua fazenda.",
        "'Microsoft Flight Simulator' é uma simulação de voo incrivelmente realista para entusiastas da aviação.",
    ],
    "jogo_quebra_cabeça": [
        "'The Witness' é um quebra-cabeça em mundo aberto repleto de desafios de lógica.",
        "Experimente 'Portal 2' para quebra-cabeças criativos envolvendo portais.",
        "'Baba Is You' é um jogo de quebra-cabeça único que permite reescrever as regras.",
    ],
    "jogo_tiro_primeira_pessoa": [
        "Para tiroteio em primeira pessoa, 'Doom Eternal' oferece ação intensa contra demônios.",
        "Experimente 'Counter-Strike: Global Offensive' para partidas competitivas de tiro.",
        "'Half-Life: Alyx' leva a experiência de realidade virtual em primeira pessoa a outro nível.",
    ],
    "jogo_indie": [
        "O jogo indie 'Hollow Knight' é uma aventura subterrânea emocionante.",
        "'Undertale' é uma experiência indie única com escolhas significativas.",
        "Explore um mundo misterioso em 'Journey', um jogo indie premiado.",
    ],
    "jogo_mundo_aberto": [
        "'Red Dead Redemption 2' oferece um mundo aberto expansivo no Velho Oeste.",
        "Para um cenário pós-apocalíptico, 'Horizon Zero Dawn' é altamente recomendado.",
        "'Assassin's Creed Valhalla' leva você para a Era Viking em um mundo aberto impressionante.",
    ],
    "jogo_casual": [
        "Para um jogo relaxante e casual, 'Animal Crossing: New Horizons' é perfeito para criar sua própria ilha.",
        "Relaxe e desafie seu cérebro com 'Calm Waters: A Point and Click Adventure' para uma experiência casual.",
        "'Slime Rancher' oferece uma jogabilidade relaxante enquanto cria seu próprio rancho de slime.",
    ],
    
    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    # Subtópicos de Restaurantes
    "restaurante_cozinha": [
        "Para comida italiana, experimente o 'Paraíso da Massa' na Quinta Avenida.",
        "Um restaurante italiano romântico com área ao ar livre é o 'Ristorante Amore'.",
        "'Spice World' oferece excelente culinária mexicana no centro da cidade.",
        "Explore 'Sea Breeze' para frutos do mar à beira-mar.",
    ],
    "restaurante_ocasião": [
        "Celebre seu aniversário no 'Candlelight Cafe' com uma atmosfera aconchegante.",
        "'Jazz and Spice' oferece música ao vivo e um ambiente romântico.",
        "'Taste of India' promove noites de música ao vivo na área central da cidade.",
        "Para uma noite especial, jante no 'The Moonlit Garden' com uma vista.",
    ],
    "restaurante_característica": [
        "Experimente o 'Sizzle Fusion' para um novo restaurante com apresentações de música ao vivo.",
        "Para uma experiência única de jantar, visite o 'The Underwater Grill'.",
        "'Mingle & Munch' oferece jantar interativo com experiências lideradas pelo chef.",
        "Explore 'The Greenhouse Cafe' para uma experiência de jantar no terraço.",
    ],
    "restaurante_sobremesa": [
        "Se delicie com cheesecake no 'Sweet Delights' na Rua Principal.",
        "'Choco Bliss' serve sobremesas de chocolate divinas.",
        "Não perca 'Fruit Fantasy' para delícias frutadas.",
        "Aproveite uma fatia de torta no 'Pie Heaven' para os amantes de sobremesas.",
    ],

    # Subtópicos de Direções
    "direções_transportepúblico": [
        "Para chegar ao aeroporto do centro, pegue o metrô na Linha A.",
        "Use o sistema de bondes da cidade para chegar ao centro de convenções.",
        "A estação de carregamento de veículos elétricos mais próxima é acessível pelo ônibus na Rota 7.",
    ],
    "direções_carregamento_veículoelétrico": [
        "A estação de carregamento de veículos elétricos mais próxima fica na 'EcoCharge' na Rua 3.",
        "Você encontrará uma estação de carregamento de veículos elétricos perto do estacionamento do shopping.",
        "Use o aplicativo 'ChargeUp' para localizar estações de carregamento de veículos elétricos na área.",
    ],
    "direções_a_pé": [
        "Ande em linha reta por duas quadras para chegar ao museu de arte.",
        "Explore o centro a pé; o hotel fica a apenas 15 minutos de caminhada.",
        "Para instruções de caminhada cênicas, siga o caminho ao longo das margens do rio.",
    ],
    "direções_tráfego": [
        "Vire à direita no próximo semáforo para evitar o congestionamento de tráfego.",
        "Considere pegar a rota cênica para o centro de convenções durante o horário de pico.",
        "Use o aplicativo 'TrafficMaster' para atualizações de tráfego em tempo real e rotas alternativas.",
    ],

    # Subtópicos de Esportes
    "esportes_liga": [
        "Harry Kane é atualmente o artilheiro da Premier League nesta temporada.",
        "Na NBA, LeBron James lidera em pontos por jogo.",
        "O recente draft da NFL apresentou talentos promissores.",
    ],
    "esportes_partida": [
        "O Jogador A venceu a emocionante partida de tênis contra o Jogador B em um tie-break.",
        "A partida de futebol recente entre os Times X e Y terminou em um empate de 2 a 2.",
        "Uma final emocionante marcou o jogo de beisebol entre o Red Sox e o Yankees.",
    ],
    "esportes_jogo": [
        "Os Times X e Y estão competindo em um jogo de basquete muito disputado.",
        "Fique ligado para atualizações ao vivo na partida de hóquei entre os Kings e os Canucks.",
        "O próximo torneio de golfe apresenta os melhores jogadores do mundo.",
    ],
    "esportes_evento": [
        "As últimas Olimpíadas apresentaram performances notáveis e recordes mundiais.",
        "Não perca os próximos Jogos de Inverno na bela cidade de Milão.",
        "A Copa do Mundo está pronta para cativar os fãs de futebol com uma competição intensa.",
    ],

    # Subtópicos de Dever de Casa
    "deverdecasa_matemática": [
        "A trigonometria lida com as relações entre ângulos e lados de triângulos.",
        "Vamos abordar seu problema de matemática passo a passo; forneça os detalhes, por favor.",
    ],
    "deverdecasa_história": [
        "O Antigo Egito possui uma rica história de faraós, pirâmides e hieróglifos.",
        "Seu dever de história sobre o Antigo Egito é um tópico intrigante. Que informações específicas você precisa?",
    ],
    "deverdecasa_ciência": [
        "A química explora a composição e propriedades da matéria.",
        "Estou aqui para ajudar com suas perguntas de química. O que está desafiando você?",
    ],
    "deverdecasa_literatura": [
        "Autores famosos como William Shakespeare e Jane Austen fizeram contribuições literárias significativas.",
        "A literatura é um mundo vasto; vamos discutir seus interesses literários específicos.",
    ],

    # Adicione mais subtópicos e respostas conforme necessário...
})


context = {
    "memory": {}
}

# Define a function to generate dynamic responses with placeholders
def generate_response(intent, context):
    memory = context["memory"]
    if intent in knowledge_base:
        responses = knowledge_base[intent]
        response = random.choice(responses)
        # Introduce placeholders for dynamic content
        placeholders = {
        "{topic}": context.get("topic", ""),
        "{info}": memory.get(context.get("topic"), ""),
        "{direction}": random.choice(["direita","esquerda"]),
        "{place}": random.choice(["Nova Iorque", "Chicago", "Paris", "Pernambuco", "Carpina", "Belford Roxo", "casa da sua mãe"]),
        "{cardinal}": random.choice(["norte","sul", "leste", "oeste"]),
        "{temperatura}": random.choice(["quente","frio","congelante","pelando","quente pra carai"]),
        "{clima}": random.choice(["nublado","chuvoso","ensolarado","limpo","quente pra carai"]),
        "{research}": random.choice(["pesquise","procure informação", "encontre", "investigigue", "examine", "procure", "colete informação", "explore detalhes"]),
        "{researchAtivo}": random.choice(["pesquisar","procurar informação", "encontrar", "investigigar", "examinar", "procurar", "coletar informação", "explorar detalhes"]),
        "{recommendation}": random.choice(["Eu sugiro", "Você pode considerar","Recomendo","Considere", "Que tal"]),
        "{location}": random.choice(["no centro", "por perto", "na sua area", "na casa de sua mãe"]),
        "{time}": random.choice(["hoje", "amanhã", "pela tarde"]),
        "{number}": str(random.randint(1, 200)),
        "{numbersmall}": str(random.randint(1, 10)),
        "{numbersmal1}": str(random.randint(1, 10)),
        "{hours}": str(random.randint(1, 24)), 
        "{minutes}": str(random.randint(1, 59)), 
        "{adjective_good}": random.choice(["incrível", "ótimo", "bom",]),
        "{verbExplore}": random.choice(["explore", "descubra", "experiencie", "tente"]),
}
        # Substitui placeholders por variações para uma conversa mais dinamica
        for placeholder, value in placeholders.items():
            if value:
                response = response.replace(placeholder, value)
        return response
    elif intent == "remember":
        return "Eu posso tentar lembrar. Pode especificar o tópico da conversa?"
    elif intent == "recall":
        topic = context.get("topic")
        if topic in memory:
            return f"Isso é o que eu lembro sobre {topic}: {memory[topic]}"
        else:
            return "Eu não lembro de ter conversado sobre isso"
    else:
        return random.choice(["Eu não entendi o que você disse :/", "Pode frasear de novo sua pergunta?","Fala direito porra"])
    
# Função que lida com a conversa
def chatbot():
    print("Oi, meu nome é Mia, como posso lhe ajudar?")
    while True:
        user_input = input("> ")
        intent = classify_intent(user_input)
        response = generate_response(intent, context)
        print(response)
        if intent == "remember":
            context["topic"] = extract_context(user_input)
            
# Tentativa em um sistema de extração de tópicos
def extract_context(user_input):
    context = {}
    doc = nlp(user_input)
    for ent in doc.ents:
        if ent.label_ == "TOPIC":
            context["topic"] = ent.text
        elif ent.label_ == "INFO":
            context["info"] = ent.text
    return context         

if __name__ == "__main__":
    chatbot()
