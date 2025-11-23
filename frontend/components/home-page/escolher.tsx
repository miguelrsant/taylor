export default function Escolher() {
    return (
      <div className="escolher">
        <div className="text-escolher">
          <h1>Por que escolher <strong className="text-gradient">TAYLOR</strong>?</h1>
          <p>A plataforma que combina poder, flexibilidade e simplicidade</p>
        </div>
        <div className="cards-escolher">
          <div className="card-escolher">
              <div className="image-escolher">
                <img src="/svg/icons/flash.svg" alt="" />
              </div>
              <div className="text-card-escolher">
                <h2>Velocidade sem precendentes</h2>
                <p>Reduza de horas para minutos o tempo de análise e geração de relatórios com automação inteligente.</p>
              </div>
          </div>
          <div className="card-escolher">
              <div className="image-escolher">
                <img src="/svg/icons/localizacao.svg" alt="" />
              </div>
              <div className="text-card-escolher">
                <h2>Decisões precisas</h2>
                <p>Insights baseados em dados reais processados por IA, eliminando suposições e aumentando assertividade.</p>
              </div>
            </div>
            <div className="card-escolher">
              <div className="image-escolher">
                <img src="/svg/icons/escudo.svg" alt="" />
              </div>
              <div className="text-card-escolher">
                <h2>Totalmente adaptável</h2>
                <p>Configura a plataforma para qualquer segmento: varejo, logística, indústria ou serviços.</p>
              </div>
            </div>
            <div className="card-escolher">
              <div className="image-escolher">
                <img src="/svg/icons/crescimento.svg" alt="" />
              </div>
              <div className="text-card-escolher">
                <h2>Crescimento contínuo</h2>
                <p>Sistema escalável que evolui com seu negócio, sem limites de volumes ou complexidade.</p>
              </div>
            </div>
          </div>
        </div>
    )
}