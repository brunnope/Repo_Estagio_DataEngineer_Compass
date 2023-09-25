## É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.

<p> Sim. No geral conseguimos reutilizar containers parados através do comado: **docker start id** ou **nome** do container escolhido para reiniciar. Porém, dependendo da configuração feita na inicialização do container, como se inicializado com --rm, isso não pode ser possível. </p>

<p>Como exemplo prático, podemos inicializar um container parado da questão anteirior do carguru:
 docker start -i teste
 Onde teste é o nome escolhido para meu container</p>
