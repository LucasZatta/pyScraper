# pyScraper
This is a simple Python API implemented using Flask, Beautiful Soup and MongoDB. It receives a url and returns information about the product displayed(decription, image_url, price, title, url)

## Installation
The project can be executed using the following command `docker-compose up --build` inside the project folder(default port 5000).

## REST API
### Request
  `GET /scrape?<url>`
  
  Sample Urls:
  ```
  https://www.amazon.com.br/acr%C3%ADlica-Simply-Daler-Rowney-126500012/dp/B002L2JHQ8/ref=pd_ybh_a_sccl_14/133-6322060-6128910?pd_rd_w=kSFca&content-id=amzn1.sym.dcc9439f-c726-44e4-8044-f93211ff757e&pf_rd_p=dcc9439f-c726-44e4-8044-f93211ff757e&pf_rd_r=WZFHRXZS9W5KDFHBTC60&pd_rd_wg=9v5G2&pd_rd_r=46dcd4d7-f367-4267-a654-bae077337e58&pd_rd_i=B002L2JHQ8&th=1
https://www.amazon.com.br/Criando-Microsservi%C3%A7os-Projetando-Componentes-Especializados/dp/6586057884/ref=pd_ybh_a_sccl_38/133-6322060-6128910?pd_rd_w=kSFca&content-id=amzn1.sym.dcc9439f-c726-44e4-8044-f93211ff757e&pf_rd_p=dcc9439f-c726-44e4-8044-f93211ff757e&pf_rd_r=WZFHRXZS9W5KDFHBTC60&pd_rd_wg=9v5G2&pd_rd_r=46dcd4d7-f367-4267-a654-bae077337e58&pd_rd_i=6586057884&psc=1
  https://www.amazon.com.br/FIGURE-DRAGON-BALL-FIGURATION-BANPRESTO/dp/B08YFG51V1/ref=pd_ybh_a_sccl_2/133-6322060-6128910?pd_rd_w=kSFca&content-id=amzn1.sym.dcc9439f-c726-44e4-8044-f93211ff757e&pf_rd_p=dcc9439f-c726-44e4-8044-f93211ff757e&pf_rd_r=WZFHRXZS9W5KDFHBTC60&pd_rd_wg=9v5G2&pd_rd_r=46dcd4d7-f367-4267-a654-bae077337e58&pd_rd_i=B08YFG51V1&psc=1
  ```
## Expected Return:

```json
{
	"description": " \n Sobre este item    Action figure original    Colecionável produto indicado para maiores de 16+ anos    Original Bandai Banpresto    Mais informações na descrição abaixo    Produto de importação direta    \n",
	"image_url": "https://m.media-amazon.com/images/I/71VAZH2+EWL._AC_SY300_SX300_.jpg",
	"price": "$280,28",
	"title": "        Figure Bandai Banpresto Dragon Ball Super Super Sayan Broly Z Battle Ref. 34854/34855 Multicor       ",
	"url": "https://www.amazon.com.br/Figure-Bandai-Banpresto-Dragon-Multicor/dp/B07YT41YF3/ref=d_pd_sbs_sccl_2_3/133-6322060-6128910?pd_rd_w=AVKaW&content-id=amzn1.sym.d5ffa5eb-c14b-4098-a3c1-e33e4cc20b5c&pf_rd_p=d5ffa5eb-c14b-4098-a3c1-e33e4cc20b5c&pf_rd_r=KQ0P6AHH85THNZSHW5K0&pd_rd_wg=MSk30&pd_rd_r=7f6ec691-53d1-4ff4-aa58-a30c0295ccff&pd_rd_i=B07YT41YF3&psc=1"
}
```

  
## Development

The project folder structure was based on previous experiences, separating responsibilities and business rules. Overall it was a pretty fun project, had been a while since I built something using Python and it was my first time using scraping apis. I had a bit of trouble implementing date range queries inside pymongo's find_one() method, so I did the persistency time range logic separately.
The project was tested using Amazon desktop urls.

## Beautiful Soup Errors

Because of lazy reloads and the async build of the DOM tree(my guess while debugging it), sometimes the get_text() function from beautiful soup returned an error called AttributeError. Because the error ocurrance was somewhatr random, I implemented a retry system in order to minimize errors returned by the endpoint. It can retry up to 6 times.

