# Crawler para acessar o feed da revista auto esporte

Desafio para editora globo. Foi utilizado o framework Scrapy para contrução desse crawler



## Instalação e execução


```sh
$ git clone https://github.com/sidneysm/desafio_auto_esporte.git
$ cd globo
$ pip install -r requirements.txt
$ scrapy crawl revistaautoesporte
```

Também foi configurado o serviço Scrapyd

```sh
$ scrapdy
```

### Deploy

O projeto foi enviado para a plataforma scrapyhub está no seguinte endereço. Pode ser visto em

[https://app.scrapinghub.com/p/221248/jobs]

### Teste

Para testar o spider basta executar os contratos construído no próprio projeto.

```sh
scrapy check revistaautoesporte
```
