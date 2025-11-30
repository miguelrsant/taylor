"use client";

import { gsap } from "gsap";
import { useEffect } from "react";
import { ScrollTrigger } from "gsap/ScrollTrigger";

export default function Pilares() {
  useEffect(() => {
    gsap.registerPlugin(ScrollTrigger);
    gsap.fromTo(
      ".text-pilar-taylor",
      { y: 100, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 1.3,
        delay: 3.5,
      },
    );
    gsap.fromTo(
      ".text-pilar-paragrafo",
      { y: 100, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 2,
        scrollTrigger: {
          trigger: "text-pilar-paragrafo",
        },
      },
    );
    gsap.fromTo(
      ".card-pilar",
      { y: 300, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 2,
        scrollTrigger: {
          trigger: "card-pilar",
        },
      },
    );
  }, []);

  return (
    <div className="pilares">
      <div className="text-pilares">
        <h1 className="text-pilar-taylor">
          Três pilares para{" "}
          <strong className="text-gradient">transformar</strong> seu negócicio
        </h1>
        <p className="text-pilar-paragrafo">
          Uma plataforma completa que une automação, inteligência artificial e
          análise visual
        </p>
      </div>
      <div className="cards-pilares">
        <div className="card-pilar">
          <img src="/svg/icons/upload.svg" alt="image-pilar" />
          <div className="text-pilar-cards">
            <h2 className="text-h2-pilar">Automação por Upload</h2>
            <p className="text-p-pilar">
              Envie planilhas Excel/CSV e deixe a IA processar automaticamente.
              Dados padronizados, integrados e prontos para análise.
            </p>
          </div>
          <div className="tres-vantagens-pilares">
            <div className="vantagem-pilar">
              <div className="bolinha-pilar"></div>
              <p className="p-vantagem-pilar">Suporte CSV e XLSX</p>
            </div>
            <div className="vantagem-pilar">
              <div className="bolinha-pilar"></div>
              <p className="p-vantagem-pilar">Validação automática</p>
            </div>
            <div className="vantagem-pilar">
              <div className="bolinha-pilar"></div>
              <p className="p-vantagem-pilar">ETL inteligente</p>
            </div>
          </div>
        </div>
        <div className="card-pilar">
          <img src="/svg/icons/chat.svg" alt="image-pilar" />
          <div className="text-pilar-cards">
            <h2 className="text-h2-pilar">Chat Inteligente</h2>
            <p className="text-p-pilar">
              Converse com seus dados em linguagem natural. Peça insights,
              relatórios e análises complexas sem conhecimente técnico.
            </p>
          </div>
          <div className="tres-vantagens-pilares">
            <div className="vantagem-pilar">
              <div className="bolinha-pilar"></div>
              <p className="p-vantagem-pilar">NLP avançado</p>
            </div>
            <div className="vantagem-pilar">
              <div className="bolinha-pilar"></div>
              <p className="p-vantagem-pilar">Análises em tempo real</p>
            </div>
            <div className="vantagem-pilar">
              <div className="bolinha-pilar"></div>
              <p className="p-vantagem-pilar">Gráficos dinâmicos</p>
            </div>
          </div>
        </div>
        <div className="card-pilar">
          <img src="/svg/icons/painel-controle.svg" alt="image-pilar" />
          <div className="text-pilar-cards">
            <h2 className="text-h2-pilar">BSI Dashboard</h2>
            <p className="text-p-pilar">
              Painel adptável com visão macro do negócio, KPIs essenciais e
              açertas automáticos sobre riscos e oportunidades.
            </p>
          </div>
          <div className="tres-vantagens-pilares">
            <div className="vantagem-pilar">
              <div className="bolinha-pilar"></div>
              <p className="p-vantagem-pilar">Deshboards personalizados</p>
            </div>
            <div className="vantagem-pilar">
              <div className="bolinha-pilar"></div>
              <p className="p-vantagem-pilar">Alertas inteligentes</p>
            </div>
            <div className="vantagem-pilar">
              <div className="bolinha-pilar"></div>
              <p className="p-vantagem-pilar">Insights automatizados</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
