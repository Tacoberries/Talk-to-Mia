



train_data = [
    # Sobre Mia
    ("O que você é capaz de fazer?", "mia_capacidade"),
    ("Como você funciona?", "mia_capacidade"),
    ("Sobre quais assuntos consegue responder?", "mia_assuntos"),
    ("Quais são os tópicos que você domina?", "mia_assuntos"),
    ("Em quais áreas você tem conhecimento?", "mia_assuntos"),
    ("Pode me dizer sobre quais temas você sabe?", "mia_assuntos"),
    ("Sobre quais assuntos você pode falar?", "mia_assuntos"),
    ("Quais são os temas que você entende?", "mia_assuntos"),
    ("Há alguma área específica em que você seja especialista?", "mia_assuntos"),
    ("Pode compartilhar sobre quais tópicos você tem informações?", "mia_assuntos"),
    ("Diga-me em quais assuntos você é versada?", "mia_assuntos"),
    ("Quais são os campos que você cobre?", "mia_assuntos"),
    ("Posso perguntar sobre qualquer coisa, ou há tópicos específicos que você domina?", "mia_assuntos"),  
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
     ("O que você pode | é capaz de fazer?", "mia_capacidade"),
    ("Como você funciona?", "mia_capacidade"),
    
    # Jogos
    ("Me recomende um jogo.", "jogo"),
    ("Tem alguma recomendação de jogo?", "jogo"),
    
    #Filme
    ("Me recomende um filme", "filme"),
    ("Estou procurando um bom filme para assistir. Pode me recomendar algum?", "filme"),
    ("Gostaria de ver um filme, mas estou sem ideias. Alguma sugestão?", "filme"),
    ("Quero assistir a um filme, mas estou indeciso. Tem alguma recomendação?", "filme"),
    ("Preciso de algo para assistir no fim de semana. Alguma sugestão de filme?", "filme"),
    ("Qual é o último filme que você assistiu e recomendaria? Estou em busca de boas opções!", "filme"),
    ("Adoro filmes. Alguma sugestão de filme que me surpreenderia?", "filme"),
    ("Sou fã de cinema. Conhece algum filme imperdível que ainda não vi?", "filme"),
    ("Estou no clima para um filme. Tem algo que você assistiu e adorou?", "filme"),
    ("Quais são seus filmes favoritos? Pode me indicar um que seja especial para você?", "filme"),
    ("Às vezes, é difícil escolher. Tem um filme que você acha que todos deveriam assistir?", "filme"),

    
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
    
    # Piada
    ("Me conte uma piada", "piada"),
    ("Me diga", "piada"),
    ("Você conhece alguma piada sobre tecnologia?", "piada"),
    ("Me faça rir com uma história engraçada.", "piada"),
    ("Compartilhe um trocadilho comigo.", "piada"),
    ("Diga-me algo hilário.", "piada"),
    ("Compartilhe uma piada divertida.", "piada"),
    ("Qual é a sua piada favorita?", "piada"),
    ("Estou precisando de uma boa risada, me conte algo engraçado.", "piada"),
    ("Conhece alguma piada interessante?", "piada"),
    ("Estou de bom humor, me surpreenda com uma piada.", "piada"),
    ("Estou pronto para sorrir, me solte uma piada.", "piada"),
    ("Quero algo leve, tem alguma piada para animar meu dia?", "piada"),
    ("Gosto de começar o dia com uma boa piada, pode me contar uma?", "piada"),

    # Livro
    ("Recomende um livro", "livro"),
    ("Me fale sobre livros bons", "livro"),
    ("Qual é um bom livro?", "livro"),
    ("Sugira um livro bom", "livro"),
    ("Tenho interesse em livros, você pode me sugerir algo para ler?", "livro"),
    ("Estou em busca de uma boa leitura, tem algum livro para recomendar?", "livro"),
    ("Qual é o último livro que você achou interessante?", "livro"),
    ("Me indique um livro que deixou uma impressão duradoura em você.", "livro"),
    ("Estou procurando novas ideias de leitura, pode me dar uma recomendação?", "livro"),
    ("Que livro você considera imperdível?", "livro"),
    ("Você tem alguma recomendação de livro que seja inspirador?", "livro"),
    ("Estou aberto a sugestões de leitura, me recomende um livro interessante.", "livro"),
    
    # Comida
    ("Me recomende um prato de comida.", "comida"),
    ("Qual é o seu prato favorito? Me recomende algo delicioso para experimentar.", "comida"),
    ("Pode me recomendar um prato especial?", "comida"),
    ("Tenho curiosidade em experimentar novos pratos, qual você sugeriria?", "comida"),
    ("Estou procurando por uma opção culinária única, pode me sugerir algo fora do comum?", "comida"),
    ("Que tal me recomendar um prato típico da sua região?", "comida"),
    ("Estou planejando uma refeição especial, qual prato você acha que seria uma ótima escolha?", "comida"),
    ("Gosto de variedade culinária, você tem uma recomendação saborosa?", "comida"),
    ("Estou com fome e indeciso, pode me ajudar sugerindo um prato?", "comida"),
    ("Quero experimentar algo novo no menu, qual prato você acha que eu deveria pedir?", "comida"),
    
    # Fatos Interessantes
    ("Me conte algo interessante.", "curiosidade"),
    ("Compartilhe um fato divertido", "curiosidade"),
    ("Qual é um fato interessante sobre algo?", "curiosidade"),
    ("Me fale sobre algo peculiar de todo o mundo.", "curiosidade"),
    ("Pode me contar uma curiosidade interessante?", "curiosidade"),
    ("Estou curioso para saber algo divertido. Tem alguma curiosidade para compartilhar?", "curiosidade"),
    ("Me surpreenda com um fato interessante! O que você tem para contar?", "curiosidade"),
    ("Gosto de aprender curiosidades sobre o mundo. Tem algo peculiar para compartilhar?", "curiosidade"),
    ("Quero expandir meu conhecimento. Qual é uma curiosidade interessante que você sabe?", "curiosidade"),
    ("Fatos divertidos sempre animam o dia. Pode compartilhar um comigo?", "curiosidade"),
    ("Estou pronto para uma dose de curiosidade. Tem algo interessante para contar?", "curiosidade"),
    ("Quero ser surpreendido! Me conte um fato intrigante.", "curiosidade"),
    ("Me fale sobre algo peculiar que muitas pessoas não sabem.", "curiosidade"),
    ("Estou aberto a aprender algo novo. Qual é um fato fascinante que você conhece?", "curiosidade"),
    
    # Viagem
    ("Qual um lugar bom para viajar?", "viagem"),
    ("Estou pensando em viajar. Pode recomendar um lugar interessante para visitar?", "viagem"),
    ("Qual destino de viagem você acha incrível? Preciso de sugestões!", "viagem"),
    ("Gostaria de explorar novos lugares. Alguma recomendação de viagem?", "viagem"),
    ("Estou planejando uma viagem. Pode sugerir um destino emocionante?", "viagem"),
    ("Se você pudesse viajar para qualquer lugar, para onde iria? Estou buscando ideias!", "viagem"),
    ("Estou em busca de aventuras. Onde você acha que seria um bom lugar para viajar?", "viagem"),
    ("Viagens são incríveis. Alguma sugestão de destino que vale a pena?", "viagem"),
    ("Quero escapar por um tempo. Conhece algum lugar relaxante para viajar?", "viagem"),
    ("Explorar o mundo é uma paixão. Tem algum lugar especial que você recomendaria?", "viagem"),
    ("Para quem ama viajar, qual destino você sugeriria? Estou aberto a novas experiências!", "viagem"),
    
    
    # Filosofia
    ("Me conte algo sobre filosofia", "filosofia"),
    ("Me diga algo filosófico", "filosofia"),
    ("Compartilhe pensamentos sobre a filosofia.", "filosofia"),
    ("Estou interessado em filosofia. Pode compartilhar algo sobre esse assunto?", "filosofia"),
    ("Filosofia é fascinante. O que você tem para compartilhar sobre esse campo do conhecimento?", "filosofia"),
    ("Gosto de explorar pensamentos profundos. Tem algo filosófico para compartilhar?", "filosofia"),
    ("Quero expandir minha compreensão filosófica. O que você pode me contar sobre filosofia?", "filosofia"),
    ("Me conte algo sobre a filosofia que possa me fazer refletir.", "filosofia"),
    ("Tenho interesse em pensamentos filosóficos. Qual é a sua perspectiva sobre filosofia?", "filosofia"),
    ("Filosofia é um campo vasto. Pode compartilhar um pensamento filosófico?", "filosofia"),
    ("Quero ouvir algo profundo. Tem algo filosófico para compartilhar hoje?", "filosofia"),
    ("Compartilhe insights filosóficos. Estou aberto a explorar novas ideias.", "filosofia"),
    ("Estou curioso sobre a filosofia. O que você pode me ensinar sobre esse assunto?", "filosofia"),

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
    ("Você pode recomendar um filme de sci-fi?", "filme_gênero_scifi"),
    ("Me recomende um filme de ficção científica?", "filme_gênero_scifi"),
    ("Me recomende um filme de sci-fi?", "filme_gênero_scifi"),
    
    ("Você pode recomendar um bom filme animado?.", "filme_animação"),
    ("Me recomende um bom filme animado?.", "filme_animação"),
    ("Me recomende uma boa animação?.", "filme_animação"),
    
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
    
    # Comida - Italiana
    ("Me sugira um prato autêntico da culinária italiana.", "comida_italiana"),
    ("Quero experimentar algo italiano. Alguma sugestão de prato?", "comida_italiana"),
    ("Você tem alguma recomendação para comida italiana?", "comida_italiana"),
    ("Estou com vontade de comida italiana. O que você sugere?", "comida_italiana"),
    ("Qual é o prato mais popular na culinária italiana?", "comida_italiana"),
    ("Pode me indicar algo delicioso da gastronomia italiana?", "comida_italiana"),
    ("Sugira um prato italiano clássico que eu deveria experimentar.", "comida_italiana"),
    ("Estou curioso sobre a comida italiana. Alguma recomendação?", "comida_italiana"),
    ("Quais são suas opções favoritas de comida italiana?", "comida_italiana"),
    ("Gostaria de saber mais sobre pratos típicos italianos. Alguma sugestão?", "comida_italiana"),

    # Comida - Japonesa
    ("Me recomende um prato autêntico da culinária japonesa.", "comida_japonesa"),
    ("Quero experimentar algo japonês. Alguma sugestão de prato?", "comida_japonesa"),
    ("Você tem alguma recomendação para comida japonesa?", "comida_japonesa"),
    ("Estou com vontade de comida japonesa. O que você sugere?", "comida_japonesa"),
    ("Qual é o prato mais popular na culinária japonesa?", "comida_japonesa"),
    ("Pode me indicar algo delicioso da gastronomia japonesa?", "comida_japonesa"),
    ("Sugira um prato japonês clássico que eu deveria experimentar.", "comida_japonesa"),
    ("Estou curioso sobre a comida japonesa. Alguma recomendação?", "comida_japonesa"),
    ("Quais são suas opções favoritas de comida japonesa?", "comida_japonesa"),
    ("Gostaria de saber mais sobre pratos típicos japoneses. Alguma sugestão?", "comida_japonesa"),

    # Comida - Brasileira
    ("Me sugira um prato autêntico da culinária brasileira.", "comida_brasileira"),
    ("Quero experimentar algo brasileiro. Alguma sugestão de prato?", "comida_brasileira"),
    ("Você tem alguma recomendação para comida brasileira?", "comida_brasileira"),
    ("Estou com vontade de comida brasileira. O que você sugere?", "comida_brasileira"),
    ("Qual é o prato mais popular na culinária brasileira?", "comida_brasileira"),
    ("Pode me indicar algo delicioso da gastronomia brasileira?", "comida_brasileira"),
    ("Sugira um prato brasileiro clássico que eu deveria experimentar.", "comida_brasileira"),
    ("Estou curioso sobre a comida brasileira. Alguma recomendação?", "comida_brasileira"),
    ("Quais são suas opções favoritas de comida brasileira?", "comida_brasileira"),
    ("Gostaria de saber mais sobre pratos típicos brasileiros. Alguma sugestão?", "comida_brasileira"),

    
    # Esportes
    ("Quem é o artilheiro na Premier League nesta temporada?", "esportes_liga"),
    ("Me fale sobre a partida de tênis recente entre o Jogador A e o Jogador B.", "esportes_partida"),
    ("Qual é a pontuação do jogo de basquete entre os Times X e Y?", "esportes_jogo"),
    ("Me dê os destaques das últimas Olimpíadas.", "esportes_evento"),
    
    
    # Piadas 
    ("Compartilhe um trocadilho relacionado à tecnologia.", "piada_tecnologia"),
    ("Você conhece alguma piada sobre animais?", "piada_animais"),
    ("Me faça rir com uma piada sobre comida.", "piada_comida"),
    
    # Livro
    ("Recomende um romance clássico de Charles Dickens.", "livro_charles_dickens"),
    ("Recomende um livro clássico de Charles Dickens.", "livro_charles_dickens"),
    ("Recomende um livro de Charles Dickens.", "livro_charles_dickens"),
    
    ("Me fale sobre os autores ganhadores do Prêmio Pulitzer.", "livro_pulitzer"),
    
    ("Qual é uma boa série de livros de fantasia para jovens leitores?", "livro_jovens_adultos"),
    ("Me recomende uma boa série de livros para jovens adultos.", "livro_jovens_adultos"),
    
    ("Sugira uma biografia de um cientista famoso.", "livro_biografia_cientista"),
    
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
    
    # Filosofia - Sentido da Vida
    ("Qual o significado da vida?", "filosofia_sentido_da_vida"),
    ("Você já pensou sobre o significado da vida?", "filosofia_sentido_da_vida"),
    ("A questão do sentido da vida é fascinante. O que você acha sobre isso?", "filosofia_sentido_da_vida"),
    ("Algumas pessoas buscam o significado da vida. Qual é a sua perspectiva sobre isso?", "filosofia_sentido_da_vida"),
    ("Perguntas filosóficas muitas vezes envolvem o sentido da vida. Qual é a sua filosofia pessoal?", "filosofia_sentido_da_vida"),
    ("Saber o significado da vida é uma jornada pessoal. Você já refletiu sobre isso?", "filosofia_sentido_da_vida"),
    ("A filosofia muitas vezes explora o sentido da vida. Como você interpreta essa questão?", "filosofia_sentido_da_vida"),
    ("O sentido da vida é uma pergunta complexa. Qual é a sua opinião sobre esse tema profundo?", "filosofia_sentido_da_vida"),
    ("Muitos filósofos se dedicaram a entender o significado da vida. Como você vê essa busca?", "filosofia_sentido_da_vida"),
    ("Pode ser desafiador compreender o significado da vida. Você já teve insights sobre essa questão?", "filosofia_sentido_da_vida"),
    ("Alguns encontram respostas na filosofia. Qual é a sua visão sobre o sentido da vida?", "filosofia_sentido_da_vida"),

    
    # Filosofia
    ("Discuta a filosofia existencialista de Jean-Paul Sartre.", "filosofia_existencialismo_sartre"),
    ("Quais são as principais teorias éticas na filosofia contemporânea?", "filosofia_teorias_éticas"),
    ("Compartilhe seus pensamentos sobre a filosofia da felicidade e bem-estar.", "filosofia_felicidade_filosofia"),
    ("Discuta o debate em torno do livre-arbítrio versus determinismo.", "filosofia_livre_arbítrio_determinismo")
])