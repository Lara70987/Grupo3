from flask import Flask, request, render_template, redirect
from database import Database, Candidato
from utils import save_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processo', methods=['GET', 'POST'])
def processo():
    if request.method == "GET":
        return render_template('processo.html')
    else:
        form_data = request.form
        save_data(form_data)
        return redirect('/')

@app.route('/time')
def time():
    return render_template('time.html')

@app.route("/nucleos")
def nucleos():
    return render_template('nucleos.html')

from urllib.parse import urlparse, urlunparse

def normalize_docs_url(url: str) -> str:
    try:
        p = urlparse(url)
        if "docs.google.com" in p.netloc and "/document/" in p.path:
            parts = p.path.split("/")
            try:
                i = parts.index("d")
                file_id = parts[i+1]
                new_path = f"/document/d/{file_id}/view"
                return urlunparse((p.scheme, p.netloc, new_path, "", "", ""))
            except Exception:
                return url
        return url
    except Exception:
        return url

@app.route("/fundo")
def fundo():
    RAW_RESEARCHES = [
        (
            "Avalanche",
            2022,
            "docs.google.com/document/d/1elHJm_2-mVJG-Kll-drSWQPqbuYEthND/edit?rtpof=true&sd=true&tab=t.0",
            "A Avalanche é uma plataforma pública e open-source que conta com uma blockchain layer 1 que suporta tanto smart contracts como redes personalizáveis.",
            "Avalanche-bg",
            "img/researches/Avalanche.png",
        ),
        (
            "Solana",
            2022,
            "https://docs.google.com/document/d/1a6PEjAoEJylOxrx_TA6mwLMgsQtcKZqf/edit?tab=t.0",
            "A criptomoeda Solana (Sol) foi lançada em março de 2020, com o objetivo de rivalizar com a Ethereum, focando em capacidade de escalabilidade e com o objetivo de oferecer soluções financeiras de forma descentralizada",
            "Solana-bg",
            "img/researches/Solana.webp",
        ),
        (
            "Polygon",
            2022,
            "https://docs.google.com/document/d/1HLnSFJ03SrjskQYaBIFhF-9ZY-oADU6e/edit?tab=t.0",
            "Criada em 2017, a MATIC é a moeda base do ecossistema Polygon, originalmente chamada de Rede Matic",
            "Polygon-bg",
            "img/researches/Polygon.png",
        ),
        (
            "Polkadot",
            2022,
            "https://docs.google.com/document/d/1po8eeRmD1FlXz9PN1W7vF9M1Ckpn-uhO/edit?tab=t.0",
            "Polkadot conecta múltiplas blockchains permitindo interoperabilidade e segurança compartilhada via parachains.",
            "polkadot-bg",
            "img/researches/polkadot.jpg",
        ),
        (
            "Decentraland",
            2022,
            "https://docs.google.com/document/d/1PJY7SxIGAs4V8hOO6ks8vwT4mr15wLna/edit?tab=t.0",
            "Mundo virtual (metaverso) descentralizado onde usuários criam e monetizam conteúdo digital em LANDs.",
            "decentraland-bg",
            "img/researches/decentraland.jpg",
        ),
        (
            "Uniswap",
            2022,
            "https://docs.google.com/document/d/1p35Q9VP11IpgYawmLnRtp6XxlMM68u4q/edit?tab=t.0",
            "AMM/DEX em Ethereum que permite trocas de tokens via pools de liquidez e curvas de preço.",
            "uniswap-bg",
            "img/researches/uniswap.jpg",
        ),
        (
            "Cardano",
            2019,
            "https://drive.google.com/file/d/1bp_9Iik_oa23-CZMuMbjjAWWiBxlwhkj/view",
            "Blockchain PoS com foco acadêmico, formal verification e camadas separadas para liquidação e computação.",
            "cardano-bg",
            "img/researches/Cardano.png",
        ),
        (
            "Chainlink",
            2019,
            "https://drive.google.com/file/d/180Jjlbytnzzf6CuFurfjVZE8o7dvq-5C/view",
            "Rede de oráculos descentralizados que conecta smart contracts a dados do mundo real.",
            "chainlink-bg",
            "img/researches/Chainlink.png",
        ),
        (
            "Monero",
            2019,
            "https://drive.google.com/file/d/1e3VWdperg6dzuhWvsTBBNQjl6WJhnLSj/view",
            "Criptomoeda com foco em privacidade (RingCT, stealth addresses).",
            "monero-bg",
            "img/researches/Monero.png",
        ),
        (
            "ZCash",
            2019,
            "https://drive.google.com/file/d/1cFeVojTXAN10x64SInuLzBRBwmBDh7dh/view?usp=sharing",
            "Criptomoeda com provas zk-SNARKs para transações com privacidade opcional.",
            "zcash-bg",
            "img/researches/ZCash.jpg",
        ),
        (
            "Litecoin",
            2019,
            "https://drive.google.com/file/d/1lZ78r0MY6osoh6Mevr1BqGG6PL56wMBA/view?usp=sharing",
            "Fork do Bitcoin com tempos de bloco menores e algoritmo Scrypt.",
            "litecoin-bg",
            "img/researches/Litecoin.jpeg",
        ),
        (
            "Tezos",
            2019,
            "https://drive.google.com/file/d/1gjvQy92JAsCwSYP8Tgpz28wo07h2mc-E/view?usp=sharing",
            "Blockchain com governança on-chain e atualização sem hard forks; PoS (Liquid PoS).",
            "tezos-bg",
            "img/researches/Tezos.png",
        ),
        (
            "Dogecoin",
            2019,
            "https://drive.google.com/file/d/1KtwSyO8rE-vqVOJVfqKC3o3Y1MIGNbEL/view?usp=sharing",
            "Moeda peer-to-peer de baixa barreira, originada de um meme; foco em comunidade e gorjetas.",
            "dogecoin-bg",
            "img/researches/Dogecoin.webp",
        ),
        (
            "Ripple",
            2019,
            "https://drive.google.com/file/d/1aYR1DcfPprgULF_1U1XScJMrR0NUATL2/view?usp=sharing",
            "Rede de liquidação e protocolo (XRP Ledger) voltados a pagamentos rápidos e baratos.",
            "ripple-bg",
            "img/researches/ripple.jpg",
        ),
        (
            "Binance Coin",
            2019,
            "https://drive.google.com/file/d/161w-K0lMqIqkxjG7SyFOu3Cf9gatY8Fw/view?usp=sharing",
            "Token utilitário do ecossistema Binance (taxas, BNB Chain, queimas periódicas).",
            "binance-bg",
            "img/researches/Binance Coin.png",
        ),
        (
            "Dash",
            2019,
            "https://drive.google.com/file/d/1jJEvr_WnAMzcFYbtE0j5DMwMBCuoYY7f/view",
            "Criptomoeda focada em pagamentos com recursos como InstantSend e PrivateSend.",
            "dash-bg",
            "img/researches/Dash.jpeg",
        ),
        (
            "IOTA",
            2019,
            "https://drive.google.com/file/d/1IsJOcko-whb6qddaU3k4r4XDJjdb7bPS/view",
            "Projeto voltado para IoT, usando o Tangle (DAG) em vez de blockchain tradicional.",
            "iota-bg",
            "img/researches/iota.png",
        ),
    ]

    researches = []
    for titulo, ano, url, descricao, bg_class, img in RAW_RESEARCHES:
        researches.append({
            "slug": titulo.lower().replace(" ", "-"),
            "titulo": titulo,
            "ano": ano,
            "descricao": descricao,
            "bg_class": bg_class,
            "img": img,
            "url": normalize_docs_url(url),
        })

    return render_template("fundo.html", researches=researches)


@app.route("/parceiros")
def parceiros():
    return render_template("parceiros.html")

@app.route('/aprenda')
def aprenda():
    return render_template("aprenda.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080)
