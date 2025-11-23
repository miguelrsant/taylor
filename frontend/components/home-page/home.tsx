import Image from "next/image"
import { gsap } from 'gsap';
import { useEffect } from 'react';

export default function Home() {

        useEffect(() => {
  
          gsap.fromTo(
              ".business",
              { x: -100,
                opacity: 0
              },
              {
              x: 0,
              opacity: 1,
              duration: 2,
              delay: 2.4,
              scrollTrigger: {
                pin: '.home',
                scrub: true
              }
              }
          );
          gsap.fromTo(
              ".taylor-principal",
              { x: 100,
                opacity: 0
              },
              {
              x: 0,
              opacity: 1,
              duration: 3.5,
              delay: 2.6,
              scrollTrigger: {
                pin: '.home',
                scrub: true
              }
              }
          );
          gsap.fromTo(
              ".taylor-secundario ",
              { y: 200,
                opacity: 0
              },
              {
              y: 0,
              opacity: 1,
              duration: 2,
              delay: 2.4,
              scrollTrigger: {
                pin: '.home',
                scrub: true
              }
              }
          );
          gsap.fromTo(
              ".taylor-paragrafo ",
              { y: 200,
                opacity: 0
              },
              {
              y: 0,
              opacity: 1,
              duration: 2,
              delay: 2.4,
              scrollTrigger: {
                pin: '.home',
                scrub: true
              }
              }
          );
          gsap.fromTo(
              ".bt-home",
              { y: 1000,
                opacity: 0,
                display: 'none'
              },
              {
              y: 0,
              opacity: 1,
              duration: 2.5,
              delay: 2.2,
              display: 'flex',
              scrollTrigger: {
                pin: '.home',
                scrub: true
              }
              }
          );
          gsap.fromTo(
              ".vantagens",
              { y: 400,
                opacity: 0
              },
              {
              y: 0,
              opacity: 1,
              duration: 2,
              delay: 3,
              scrollTrigger: {
                pin: '.home',
                scrub: true
              }
              }
          );
          }, []);
      
    return (
              <div className="home">
        <div className="home-page">
          <div className="business">
            <img src="/png/star.png" alt="Engrenagem" />
            <p>Business Super Intelligence Platform</p>
          </div>
          <div className="texto-home">
            <h1 className="taylor-principal text-gradient">TAYLOR</h1>
            <h1 className="taylor-secundario">Transforme dados em decisões estratégicas</h1>
            <p className="taylor-paragrafo">Plataforma avançada de automação operacional e análise inteligente com IA. Automatize rotinas, gere insights e acompanhe seu negócio em tempo real.</p>
          </div>
          <a className="bt-home" href="/waitingline" style={{textDecoration: "none"}} ><div className="btn-comecar"><p>Começar agora →</p></div></a>
        </div>
        <div className="vantagens">
          <div className="cards-home">
            <h1 className="cards-h1 text-gradient">99%</h1>
            <p className="cards-p">Redução do tempo</p>
          </div>
          <div className="cards-home">
            <h1 className="cards-h1 text-gradient">24/7</h1>
            <p className="cards-p">Análise automática</p>
          </div>
          <div className="cards-home">
            <h1 className="cards-h1 text-gradient">100%</h1>
            <p className="cards-p">Personalizável</p>
          </div>
        </div>
      </div>
    )
}