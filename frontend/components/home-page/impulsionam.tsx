"use client"

import { gsap } from 'gsap';
import { useEffect } from 'react';
import { ScrollTrigger } from "gsap/ScrollTrigger";

export default function Impulsionam() {

        useEffect(() => {
          gsap.registerPlugin(ScrollTrigger)
          gsap.fromTo(
              ".text-impulsionam",
              { y: 100,
                opacity: 0
              },
              {
              y: 0,
              opacity: 1,
              duration: 2,
              scrollTrigger: {
                trigger: '.text-impulsionam',
              }
              }
          );
          gsap.fromTo(
              ".card-impulsionam",
              { y: 100,
                opacity: 0
              },
              {
              y: 0,
              opacity: 1,
              duration: 1.7,
              scrollTrigger: {
                trigger: '.card-impulsionam',
              }
              }
          );
            gsap.fromTo(
              ".card-principal-impulsionam",
              { y: 120,
                opacity: 0
              },
              {
              y: 0,
              opacity: 1,
              duration: 1,
              scrollTrigger: {
                trigger: '.card-principal-impulsionam',
              }
              }
          );
          }, []);
    return (
        <div className="impulsionam">
          <div className="text-impulsionam">
            <h1>Métricas que <strong className=" text-gradient">impulsionam</strong> resultados</h1>
            <p>Acompanhe indicadores essenciais para tomada de decisão estratégica</p>
          </div>
          <div className="cards-impulsionam">
            <div className="card-impulsionam">
              <div className="img-card-impulsionam">
                <img src="/svg/icons/crescimento.svg" alt="" />
              </div>
              <div className="text-card-impulsionam">
                <h3 className="">OTIF</h3>
                <p>On Time In Full por fornecedor</p>
              </div>
            </div>
            <div className="card-impulsionam">
              <div className="img-card-impulsionam">
                <img src="/svg/icons/cronometro.svg" alt="" />
              </div>
              <div className="text-card-impulsionam">
                <h3 className="">Aging de Pedidos</h3>
                <p>Análise por faixas temporais</p>
              </div>
            </div>
            <div className="card-impulsionam">
              <div className="img-card-impulsionam">
                <img src="/svg/icons/caixa.svg" alt="" />
              </div>
              <div className="text-card-impulsionam">
                <h3 className="">Giro de Estoque</h3>
                <p>Movimentação e cobertura</p>
              </div>
            </div>
            <div className="card-impulsionam">
              <div className="img-card-impulsionam">
                <img src="/svg/icons/alerta.svg" alt="" />
              </div>
              <div className="text-card-impulsionam">
                <h3 className="">Itens parados</h3>
                <p>Identificação aotomática 30/60/90d</p>
              </div>
            </div>
          </div>
          <div className="card-principal-impulsionam">
            <div className="text-card-p-impulsionam">
              <h2>+50</h2>
              <p>Indicadores disponíveis</p>
            </div>
            <div className="text-card-p-impulsionam">
              <h2>Real-time</h2>
              <p>Atualização automática</p>
            </div>
            <div className="text-card-p-impulsionam">
              <h2>100%</h2>
              <p>Personalizável</p>
            </div>
          </div>
      </div>
    )
}